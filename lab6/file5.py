l = ["apple", "banana", "orange"]
f = open("a.txt", "w")
for i in l:
    f.write(i +"\n")
f.close()