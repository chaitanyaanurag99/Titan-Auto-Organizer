import os
import shutil

# ==========================================
# 🦁 Titan Auto-Organizer (Universal Version)
# ==========================================

print("--------------------------------------------------")
print("   🦁 TITAN FILE ORGANIZER - CLEAN YOUR MESS 🦁   ")
print("--------------------------------------------------")


folder_path = input("Enter the path of the folder to organize: ").strip()

if not os.path.exists(folder_path):
    print(f"❌ Error: The folder '{folder_path}' does not exist.")
    print("Please check the path and try again.")
    exit()

print(f"\n📂 Scanning: {folder_path}...\n")

files = os.listdir(folder_path)

extensions = {
    "Images": [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".odt", ".rtf"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Software": [".exe", ".msi", ".dmg", ".pkg", ".deb"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"]
}

for file_name in files:
    src_path = os.path.join(folder_path, file_name)

    if os.path.isdir(src_path):
        continue

    _, file_extension = os.path.splitext(file_name)
    file_extension = file_extension.lower()

    target_folder = "Others"
    found = False
    
    for category, ext_list in extensions.items():
        if file_extension in ext_list:
            target_folder = category
            found = True
            break
            
    final_target_path = os.path.join(folder_path, target_folder)
    
    if not os.path.exists(final_target_path):
        os.makedirs(final_target_path)
        print(f"📁 Created Folder: {target_folder}")

    dst_path = os.path.join(final_target_path, file_name)
    
    try:
        shutil.move(src_path, dst_path)
        print(f"✅ Moved: {file_name} -> {target_folder}")
    except Exception as e:
        print(f"❌ Error moving {file_name}: {e}")

print("--------------------------------------------------")
print("🦁 Organization Complete!")