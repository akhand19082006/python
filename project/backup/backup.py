import os
import shutil
import time
def main():
    deletedfiles=0
    deletedfolder=0
    path="E:\Class 8 NCERT Book"
    days=30
    second=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if second>= get_fileage(root_folder):
                remove_folder(root_folder)
                deletedfolder+=1
                break
            else:
                for x in folders:
                    folderpath=os.path.join(root_folder,x)
                     if second>= get_fileage(folderpath):
                        remove_folder(folderpath)
                        deletedfolder+=1
                for y in files:
                     filepath=os.path.join(root_folder,y)
                     if second>= get_fileage(filepath):
                        remove_file(filepath)
                        deletedfiles+=1
    else:
        print("Path not found")
    print("deletedfiles: ",deletedfiles,"Deletedfolders: ",deletedfolder )
