import os
if os.path.exists("input.txt"):
  os.remove("input.txt")
else:
  print("The file does not exist")