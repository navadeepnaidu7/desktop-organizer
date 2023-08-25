import os
import shutil

# Define the path to the "files" folder
files_path = os.path.join(os.path.join(os.path.expanduser("~")), "Downloads", "DesktopCleaner", "files") 
# Files that you put inside DesktopCleaner folder gets sorted into filse folder inside the DesktopCleaner folder according to it's type

# Define the mapping of file types to corresponding subfolders
file_types = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.pdf': 'Documents',
    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.exe': 'Executables',
    '.ppt': 'Presentations',
    '.msi': 'Installers',
    '.torrent': 'Torrents',
   
}


SMALL_SIZE = 5 * 1024 * 1024  # 5 MB
MEDIUM_SIZE = 25 * 1024 * 1024  # 25 MB

def get_file_size(filepath):
    return os.path.getsize(filepath)

def organize_files_by_size():
    for root, _, files in os.walk(files_path):
        for filename in files:
            file_extension = os.path.splitext(filename)[-1].lower()
            if file_extension in file_types:
                source_path = os.path.join(root, filename)
                file_size = get_file_size(source_path)

                if file_size <= SMALL_SIZE:
                    target_subfolder = 'Small'
                elif SMALL_SIZE < file_size <= MEDIUM_SIZE:
                    target_subfolder = 'Medium'
                else:
                    target_subfolder = 'Large'

                target_folder = os.path.join(files_path, file_types[file_extension], target_subfolder)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                target_path = os.path.join(target_folder, filename)
                shutil.move(source_path, target_path)
                print(f"Moved {filename} to {target_folder}")

if __name__ == "__main__":
    organize_files_by_size()
