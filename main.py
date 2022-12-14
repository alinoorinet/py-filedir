import os
from pathlib import Path

path = "G:/ican projects/کنترل تولید/مستندات"
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        #append the file name to the list
	    filelist.append(os.path.join(root,file))

#print all the file names

dest = "G:/GitHub/py-filedir/dest/"
fileCounter = 0
for name in filelist:
    filename, extension, = os.path.splitext(name)
    split_name = filename.split("\\")
    newFile    = dest + split_name[1] + extension
    checkExistsTarget = Path(newFile[len(newFile) - len(extension):len(newFile)])
    if not checkExistsTarget.exists():
        file_to_open = Path(name)
        # if file_to_open.exists():
        with open(newFile, 'wb+') as destination:
            destination.write(file_to_open.read_bytes())
        fileCounter += 1
print(fileCounter)
