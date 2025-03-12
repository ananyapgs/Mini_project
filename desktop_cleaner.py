import os
import shutil

def create_subfolder_if_needed(folder_path, subfolder_name):
    """Creates a subfolder inside the given folder path if it doesn't exist."""
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)  # Fixed bug here
    return subfolder_path

def clean_folder(folder_path):
    """Organizes files in the given folder by moving them into subfolders based on file extensions."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if not os.path.isfile(file_path):
            continue  

        # Extract file extension
        file_extension = filename.split('.')[-1].lower() if '.' in filename else None

        if file_extension:
            subfolder_name = f"{file_extension.upper()} Files"
        else:
            subfolder_name = "Miscellaneous"  # Handle files with no extension

        subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)

        # Move file to corresponding subfolder
        shutil.move(file_path, subfolder_path)
        print(f"Moved: {filename} -> {subfolder_name}/")

if __name__ == "__main__":
    print("Desktop Files Orgainzer Script")
    
    folder_path = r"Python Project\Folder for project"  # Using raw string (r"") for Windows paths

    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Cleaning completed successfully!")
    else:
        print("Invalid folder path. Please ensure the path is correct and try again.")
