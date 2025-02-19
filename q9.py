import os
import shutil
import time
import filecmp

def ensure_version_directory_exists():
    if not os.path.exists('versions'):
        os.makedirs('versions')

def get_versioned_filename(original_filename, version):
    name, extension = os.path.splitext(original_filename)
    return f"{name}_v{version}{extension}"

def save_file_version(file_path):
    ensure_version_directory_exists()
    filename = os.path.basename(file_path)
    version = int(time.time())
    versioned_filename = get_versioned_filename(filename, version)
    shutil.copy(file_path, os.path.join('versions', versioned_filename))
    print(f"Saved version: {versioned_filename}")

def restore_file_version(filename, version):
    versioned_filename = get_versioned_filename(filename, version)
    versioned_file_path = os.path.join('versions', versioned_filename)
    if os.path.exists(versioned_file_path):
        shutil.copy(versioned_file_path, filename)
        print(f"Restored {filename} to version {version}")
    else:
        print(f"Version {version} of {filename} not found.")

def compare_file_versions(filename, version1, version2):
    file1_path = os.path.join('versions', get_versioned_filename(filename, version1))
    file2_path = os.path.join('versions', get_versioned_filename(filename, version2))
    if os.path.exists(file1_path) and os.path.exists(file2_path):
        if filecmp.cmp(file1_path, file2_path, shallow=False):
            print("Files are identical.")
        else:
            print("Files differ.")
    else:
        print("One or both versions not found.")

def cleanup_old_versions(filename, keep_last_n=2):
    name, extension = os.path.splitext(filename)
    all_versions = sorted([f for f in os.listdir('versions') if f.startswith(name)], reverse=True)
    for old_version in all_versions[keep_last_n:]:
        os.remove(os.path.join('versions', old_version))
        print(f"Removed old version: {old_version}")

def monitor_directory_for_changes(directory_path):
    last_modified_times = {}
    while True:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                current_mod_time = os.path.getmtime(file_path)
                if filename not in last_modified_times or last_modified_times[filename] != current_mod_time:
                    save_file_version(file_path)
                    last_modified_times[filename] = current_mod_time
        time.sleep(5)

directory_to_monitor = './my_files'
monitor_directory_for_changes(directory_to_monitor)