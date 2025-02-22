# Detect_Hacker
I Ashitosh Ghate created a unique Python script that checks for potential system hacks by analyzing system integrity and network activity
# Detect Hack - System Security Checker

## Description
This Python script helps detect potential system compromises by verifying system file integrity and analyzing network connections for suspicious activity. It checks for unauthorized modifications to critical system files and detects unusual network connections that might indicate hacking attempts.

## Features
- Scans important system files for unauthorized modifications.
- Checks active network connections for unusual or unknown endpoints.
- Provides warnings if potential hacking activities are detected.
- Works on Linux systems with `netstat` installed.

## Requirements
- Python 3.x
- Root privileges (for checking system files and network connections)

## Usage
Run the script with:
```
python3 detect_hack.py
```
It will analyze your system and report any anomalies detected.

## Disclaimer
This script is for educational and security awareness purposes only. It does not guarantee complete protection from cyber threats. Use responsibly.
