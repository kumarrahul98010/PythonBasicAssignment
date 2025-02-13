import os
import hashlib
import shutil

def get_file_hash(file_path):
    with open(file_path, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()

def find_duplicate_files(folder_path):
    file_hashes = {}
    duplicate_files = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)

            if file_hash in file_hashes:
                duplicate_files.append(file_path)
            else:
                file_hashes[file_hash] = file_path

    return duplicate_files

def handle_duplicates(duplicate_files):
    if not duplicate_files:
        print("No duplicate files found.")
        return

    print("\nDuplicate Files:")
    for file in duplicate_files:
        print(file)

    choice = input("\nDelete (d) / Move (m) / Skip (s)? ").strip().lower()
    
    if choice == "d":
        for file in duplicate_files:
            os.remove(file)
        print("Duplicates deleted.")
    elif choice == "m":
        target_folder = input("Enter folder to move duplicates: ").strip()
        os.makedirs(target_folder, exist_ok=True)
        for file in duplicate_files:
            shutil.move(file, target_folder)
        print("Duplicates moved.")

folder_path = input("Enter folder path: ").strip()
duplicates = find_duplicate_files(folder_path)
handle_duplicates(duplicates)
