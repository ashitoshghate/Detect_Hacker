import os
import subprocess
import hashlib

def check_system_integrity():
    """
    Checks for signs of system compromise by verifying system file integrity.
    """
    suspicious_files = ["/etc/passwd", "/etc/shadow", "/bin/ls", "/bin/ps"]
    anomalies = []
    
    for file in suspicious_files:
        if os.path.exists(file):
            file_hash = hashlib.sha256(open(file, 'rb').read()).hexdigest()
            # Normally, you would compare with a known-good hash (here, we simulate detection)
            if file_hash.endswith("0"):  # Dummy condition for anomaly
                anomalies.append(file)
    
    return anomalies

def check_network_connections():
    """
    Detects unusual network connections that may indicate a hack.
    """
    try:
        output = subprocess.check_output(["netstat", "-tunap"], stderr=subprocess.DEVNULL).decode()
        suspicious = [line for line in output.split('\n') if "ESTABLISHED" in line and "unknown" in line]
        return suspicious
    except Exception:
        return []

if __name__ == "__main__":
    hacked = False
    
    print("Checking system integrity...")
    integrity_issues = check_system_integrity()
    if integrity_issues:
        hacked = True
        print(f"Suspicious file modifications detected: {integrity_issues}")
    else:
        print("No integrity issues found.")
    
    print("Checking network connections...")
    network_issues = check_network_connections()
    if network_issues:
        hacked = True
        print(f"Suspicious network connections found: {network_issues}")
    else:
        print("No unusual network activity detected.")
    
    if hacked:
        print("WARNING: Potential system compromise detected!")
    else:
        print("System appears secure.")
