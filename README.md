# Python File Integrity Monitor

## Project Overview
A Python-based defensive cybersecurity tool designed to detect unexpected changes to monitored files using SHA-256 cryptographic hashing.

The tool creates a trusted baseline of file hashes and compares them against current files to identify modifications, deletions, and newly created files. 

This project demonstrates foundational Blue Team cybersecurity skills relevant to SOC Analyst, Cybersecurity Analyst, and Defence cybersecurity roles.  

## Technologies Used
- Python 3
- SHA-256 hashing (hashlib)
- JSON baseline storage
- CSV security reporting
- Visual Studio Code
- GitHub

## Project Objectives
- Establish a trusted baseline of monitored files.
- Detect unexpected modifications to file contents.
- Identify deleted and newly created files.
- Generate security alerts with timestamps and severity classifications.
- Export detected changes into CSV reports.
- Validate detection functionality through simulated security incidents.

## How It Works
1. The program scans the `monitored_files` directory.
2. It calculates SHA-256 hashes for each file.
3. The original hashes are stored in `baseline.json`.
4. Current file hashes are compared against the baseline.
5. Files are classified as OK, MODIFIED, DELETED, or NEW.
6. Detected changes are exported to `security_report.csv`.

## Detection Capabilities

| Status | Description | Severity |
|---|---|---|
| MODIFIED | File contents differ from baseline | HIGH |
| DELETED | Previously monitored file is missing | HIGH |
| NEW | File was not present in baseline | MEDIUM |
| OK | File matches baseline | No alert |

Severity labels are predefined for demonstration purposes.

## Example Security Alert
```text
=== File Integrity Report ===
[MODIFIED] config.txt
[OK] users.txt

[INFO] Security report saved to security_report.csv
```

Example CSV output:

```csv
timestamp,filename,status,severity
2026-11-05T17:02:10,config.txt,MODIFIED,HIGH
```

## Testing and Validation

| Test Scenario | Expected Result | Outcome |
|---|---|---|
| Baseline creation | Two files recorded | Passed |
| Unmodified files | Both files marked OK | Passed |
| Firewall configuration changed | MODIFIED alert | Passed |
| Unexpected file created | NEW alert | Passed |
| Monitored file deleted | DELETED alert | Passed |
| CSV report generation | Alert saved to CSV | Passed |

All six test scenarios produced the expected results.

## Testing Evidence
All testing screenshots are available in the [Screenshots Folder](screenshots/).

The folder contains:

1. `01-baseline-created.png` - SHA-256 baseline creation
2. `02-original-files.png` - Original files verified
3. `03-modified-file.png` - Modified configuration detected
4. `04-new-file.png` - Unexpected file detected
5. `05-deleted-file.png` - Deleted file detected
6. `06-csv-report.png` - Generated CSV security report

## How to Run

**Requirements:** Python 3. No third-party packages required.

1. Clone or download this repository.
2. Open the project directory in a terminal.
3. Run `python3 monitor.py check` to check the included sample files.
4. Run `python3 monitor.py baseline` to create a baseline if one does not already exist.
5. Review the terminal output and `security_report.csv`.

**Note:** The repository includes a sample `baseline.json`. To establish a new trusted baseline, remove or rename the existing baseline first, then run `python3 monitor.py baseline` after confirming the monitored files are in their intended trusted state.

## Project Structure
```text
Python-File-Integrity-Monitor/
├── monitor.py
├── baseline.json
├── security_report.csv
├── example_security_report.csv
├── README.md
├── monitored_files/
│   ├── config.txt
│   └── users.txt
└── screenshots/
    ├── 01-baseline-created.png
    ├── 02-original-files.png
    ├── 03-modified-file.png
    ├── 04-new-file.png
    ├── 05-deleted-file.png
    └── 06-csv-report.png
```

## Limitations
- Integrity checks are performed manually rather than continuously.
- The tool cannot identify who modified a file.
- File permissions and ownership changes are not monitored.
- The local baseline is not protected against tampering.
- Legitimate file changes may trigger alerts.
- Severity classifications are predefined rather than based on contextual risk.

## Future Improvements
- Real-time file monitoring
- Email and webhook notifications
- SIEM integration
- Protected baseline storage
- Automated unit testing
- Docker containerisation

## Skills Demonstrated
- Python scripting and automation
- SHA-256 cryptographic hashing
- File integrity monitoring
- Security log and alert reporting
- Baseline management
- Defensive cybersecurity testing
- Blue Team security monitoring

## Conclusion
This project demonstrates how Python can be used to detect unexpected changes to security-sensitive files through SHA-256 hashing and baseline comparison.

It provides practical experience with integrity verification, security monitoring, and automated reporting relevant to defensive cybersecurity environments. 
