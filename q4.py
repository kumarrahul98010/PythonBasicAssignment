import os
import subprocess

pkg_mgr = "apt" if os.path.exists("/usr/bin/apt") else "yum"

def check_updates():
    cmd = f"sudo {pkg_mgr} list --upgradable" if pkg_mgr == "apt" else f"sudo {pkg_mgr} check-update"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    updates = result.stdout.strip().split("\n")[1:] if pkg_mgr == "apt" else result.stdout.strip().split("\n")

    if not updates:
        print("No updates available.")
        return []
    
    print("\nAvailable updates:")
    for i, line in enumerate(updates, 1):
        print(f"{i}. {line.split()[0]}")  

    return [line.split()[0] for line in updates]

def update_packages(updates):
    choice = input("\nEnter 'all' to update everything or package number: ")
    
    if choice == "all":
        cmd = f"sudo {pkg_mgr} upgrade -y" if pkg_mgr == "apt" else f"sudo {pkg_mgr} update -y"
    elif choice.isdigit() and 1 <= int(choice) <= len(updates):
        cmd = f"sudo {pkg_mgr} install -y {updates[int(choice)-1]}"
    else:
        print("Invalid choice!")
        return

    print("Updating...")
    subprocess.run(cmd, shell=True)

updates = check_updates()
if updates:
    update_packages(updates)
