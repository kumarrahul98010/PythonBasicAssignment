import os
import subprocess

package_manager = "apt" if os.path.exists("/usr/bin/apt") else "yum"

def get_available_updates():
    command = f"sudo {package_manager} list --upgradable" if package_manager == "apt" else f"sudo {package_manager} check-update"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    updates_list = result.stdout.strip().split("\n")[1:] if package_manager == "apt" else result.stdout.strip().split("\n")
    
    if not updates_list:
        print("No updates available.")
        return []
    
    print("\nAvailable Updates:")
    for index, update in enumerate(updates_list, 1):
        print(f"{index}. {update.split()[0]}")
    
    return [update.split()[0] for update in updates_list]

def update_selected_packages(updates):
    choice = input("\nEnter 'all' to update everything or select a package number: ")
    
    if choice == "all":
        command = f"sudo {package_manager} upgrade -y" if package_manager == "apt" else f"sudo {package_manager} update -y"
    elif choice.isdigit() and 1 <= int(choice) <= len(updates):
        command = f"sudo {package_manager} install -y {updates[int(choice)-1]}"
    else:
        print("Invalid choice!")
        return

    print("Updating your pakage")
    subprocess.run(command, shell=True)

available_updates = get_available_updates()
if available_updates:
    update_selected_packages(available_updates)
