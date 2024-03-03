import os
dirs = []
files = []
path = 'C:/Users/Admin/pp2'
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        dirs.append(i)
    else:
        files.append(i)
d_and_f = dirs + files
print(dirs)
print(files)
print(d_and_f)