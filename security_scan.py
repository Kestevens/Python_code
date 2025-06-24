import subprocess

def perform_vulnerability_scan(target_ip):
    print("Running vulnerability scan...")
    subprocess.run(["nmap", "-sV", target_ip])
    print("Completed vulnerability scan")

def perform_penetration_test(target_ip):
    print("Running penetration test...")
    subprocess.run(["msfconsole", "-x", f"db_nmap -sV {target_ip}; exit"])
    print("Completed penetration test...")

def perform_intrusion_detection():
    print("Running intrusion detection...")
    subprocess.run(["suricata", "-c", "/path/to/config.yaml"])
    print("Completed intrusion detection...")

if __name__ == "__main__":
    target_ip = "192.168.1.101"
    print("Choose scan type: ")
    print("1. Vulnerability scanning")
    print("2. Penetration testing")
    print("3. Intrusion detection")

    choice = input("Enter your option, 1, 2, or 3: ")

    if choice == "1":
        perform_vulnerability_scan(target_ip)
    elif choice == "2":
        perform_penetration_test(target_ip)
    elif choice == "3":
        perform_intrusion_detection(target_ip)
    else:
        print("Incorrect option")