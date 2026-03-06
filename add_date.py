import os
import argparse
from datetime import datetime

def add_date_to_filenames(folder_path):
    # Get today's date in YYYY-MM-DD format
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Construct the old and new file paths
        old_path = os.path.join(folder_path, filename)
        
        # Skip if it's a directory
        if os.path.isdir(old_path):
            continue
            
        # Avoid double-prefixing if the script is run twice
        if filename.startswith(today_str):
            print(f"Skipping '{filename}' - already prefixed.")
            continue

        new_filename = f"{today_str}_{filename}"
        new_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

def main():
    parser = argparse.ArgumentParser(description="Add today's date (YYYY-MM-DD) to the beginning of every filename in a folder.")
    parser.add_argument("folder", type=str, help="Path to the folder containing files to rename")
    
    args = parser.parse_args()
    add_date_to_filenames(args.folder)

if __name__ == "__main__":
    main()
