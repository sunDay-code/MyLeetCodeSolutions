#Create a folder with a txt file and a py file in it

import os
folder="088. Merge Sorted Array"
if not os.path.exists(folder):
    os.makedirs(folder)
    write_path=f'{folder}/{folder}.txt'
    f=open(write_path, 'w')
    f.write("Auto Generate")
    f.close()
    write_path=f'{folder}/{folder}.py'
    f=open(write_path, 'w')
    f.write("#Auto Generate")
    f.close()
    print("Folder Created")
else:
    print("Folder exist")
