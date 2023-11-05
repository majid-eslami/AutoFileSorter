# Majid Eslami
import os
import shutil

path = r'C:/Users/MAJID\Desktop/New folder/'

folder_names = ['csv files', 'image files', 'text files']

for f in range(3):                               # create desired folders
    if not os.path.exists(path + folder_names[f]):
        os.makedirs(path + folder_names[f])

ls_of_files = os.listdir(path)                  # returns list of exist file in path

for file in ls_of_files:                        # move and put each file in appropriate folder
    if '.xlsx' in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif '.jpg' in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif '.docx' in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
