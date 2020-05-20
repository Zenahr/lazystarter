import os
import shutil

def copyrecursively(source_folder, destination_folder):
    for root, dirs, files in os.walk("data"):
        for item in files:
            src_path = os.path.join(root, item)
            dst_path = os.path.join("new-project", src_path.replace(source_folder, ""))
            if os.path.exists(dst_path):
                if os.stat(src_path).st_mtime > os.stat(dst_path).st_mtime:
                    shutil.copy2(src_path, dst_path)
            else:
                shutil.copy2(src_path, dst_path)
        for item in dirs:
            src_path = os.path.join(root, item)
            dst_path = os.path.join(destination_folder, src_path.replace(source_folder, ""))
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)

# template_folder = "\data"
# current_directory = os.getcwd()
# target_directory = current_directory + template_folder
# print(target_directory)
os.mkdir("new-project")
print(os.getcwd("new-project"))
