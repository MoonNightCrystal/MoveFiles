import os
import shutil

from_dir = "C:/Users/jhari/Downloads"
to_dir = "C:/Users/jhari/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx','.pdf', '.htm', '.html']:
        
        path1 = from_dir + '/' + file_name
        path2 = to_dir
        path3 = to_dir + '/' + file_name
        
        if os.path.exists(path2):
            print("\nMoving" + file_name + "...\n")
            shutil.move(path1, path3)
            if os.path.exists(path3):
                print("" + file_name + "has been moved.\n")
        else:
            os.mkdir(path2)
            print("Moving" + file_name + "...")
            shutil.move(path1, path3)
            if os.path.exists(path3):
                print("" + file_name + "has been moved.\n")
            
