import os
import shutil



def move_files(src,des,filetype):
    for glava_folder, sub_folders, files in os.walk(src):
        for sub_folder in sub_folders:
            print(os.path.join(glava_folder, sub_folder))
        for file in files:
            extract = os.path.splitext(file)[-1].lower()
            print(extract)
            if extract == filetype:
                shutil.move(os.path.join(glava_folder,file),des)
            else:
                print("No such files.")    
    print("Zavrseno.")       
            
            

#   for file in os.listdir(folder1):
#        extract = os.path.splitext(file)[-1].lower()
#        if extract == filetype:
