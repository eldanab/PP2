import os
path = 'C:/Users/Admin/pp2'
print("Existence:", os.access(path, os.F_OK))
print(os.path.basename(path))
print(os.path.dirname(path))