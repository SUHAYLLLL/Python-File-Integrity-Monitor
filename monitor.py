import hashlib
import json
import sys
import csv
from datetime import datetime
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
MONITORED_DIR = BASE_DIR / "monitored_files"
BASELINE_FILE = BASE_DIR / "baseline.json"
REPORT_FILE = BASE_DIR / "security_report.csv"


# Calculate SHA-256 hash
def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


# Scan monitored files
def scan_files():
    results = {}

    for file_path in sorted(MONITORED_DIR.rglob("*")):
        if file_path.is_file():
            relative_path = str(file_path.relative_to(MONITORED_DIR))
            results[relative_path] = calculate_hash(file_path)

    return results


# Create original baseline
def create_baseline():
    if BASELINE_FILE.exists():
        print("[WARNING] Baseline already exists. Not overwriting.")
        return

    baseline = scan_files()

    with open(BASELINE_FILE, "w") as file:
        json.dump(baseline, file, indent=4)

    print(f"[SUCCESS] Baseline created for {len(baseline)} files.")


# Generate CSV security report
def generate_report(alerts):
    with open(REPORT_FILE, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "timestamp",
            "filename",
            "status",
            "severity"
        ])

        for alert in alerts:
            writer.writerow([
                alert["timestamp"],
                alert["filename"],
                alert["status"],
                alert["severity"]
            ])

    print(f"\n[INFO] Security report saved to {REPORT_FILE.name}")


# Compare files against baseline
def check_integrity():
    if not BASELINE_FILE.exists():
        print("[ERROR] Baseline not found. Run baseline first.")
        return

    with open(BASELINE_FILE, "r") as file:
        baseline = json.load(file)

    current = scan_files()
    alerts = []

    print("=== File Integrity Report ===")

    for filename in baseline:
        if filename not in current:
            status = "DELETED"
        elif baseline[filename] != current[filename]:
            status = "MODIFIED"
        else:
            print(f"[OK] {filename}")
            continue

        print(f"[{status}] {filename}")

        alerts.append({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "filename": filename,
            "status": status,
            "severity": "HIGH"
        })

    for filename in current:
        if filename not in baseline:
            print(f"[NEW] {filename}")

            alerts.append({
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                "filename": filename,
                "status": "NEW",
                "severity": "MEDIUM"
            })

    generate_report(alerts)


# Command-line interface
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 monitor.py [baseline|check]")
    elif sys.argv[1] == "baseline":
        create_baseline()
    elif sys.argv[1] == "check":
        check_integrity()
    else:
        print("Invalid command. Use baseline or check.")


