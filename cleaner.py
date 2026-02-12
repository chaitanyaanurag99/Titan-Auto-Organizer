import os
import shutil

folder_path ="C:\\Users\\Chaitanya\\OneDrive\\Desktop\\titan_test"


files = os.listdir(folder_path)

images = {".jpg", ".png", ".gif" ,".jpeg", ".bmp", ".svg", ".webp"}

documents = {".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".odt", ".rtf"}

videos = {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"}

software = {".exe", ".msi", ".dmg", ".rar", ".zip" ,".tar", ".gz"}

for file_name in files:

    src_path = os.path.join(folder_path, file_name)

    if os.path.isdir(src_path):
        continue


    
    file_extension = os.path.splitext(file_name)[1].lower()
    
    if file_extension in images: target_folder = os.path.join(folder_path, "Images")
    elif file_extension in documents: target_folder = os.path.join(folder_path, "Documents") 
    elif file_extension in videos: target_folder = os.path.join(folder_path, "Videos")
    elif file_extension in software: target_folder = os.path.join(folder_path, "Software")
    else: continue
    
    target_folder  = os.path.join(folder_path, target_folder)        
    os.makedirs(target_folder, exist_ok=True)


    dst_path = os.path.join(target_folder, file_name)
    shutil.move(os.path.join(folder_path, file_name), dst_path)
    print(f"Moved: {file_name} to {target_folder}")
    print("--------------------------------------------------")
    print("File organization complete.")