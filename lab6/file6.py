import string
for i in string.ascii_uppercase:
    f = open(f"{i}.txt", 'w')
    f.close()