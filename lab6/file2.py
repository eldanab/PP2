import os
path = 'C:/Users/Admin/pp2'
print('Existence:', os.access(path, os.F_OK))
print('Readablility:', os.access(path, os.R_OK))
print('Writablylity:', os.access(path, os.W_OK))
print('Executability:', os.access(path, os.X_OK))