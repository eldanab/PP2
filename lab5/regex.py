import re
#Ex.1
s = re.compile(r'\w*a+b*\w*')
n = input("Ex.1: ")
if s.match(n):
    print("matches")
else: 
    print("doesn't match")
#Ex.2
s = re.compile(r'\w*a+b{2,3}\w*')
n = input("Ex.2: ")
if s.match(n):
    print("matches")
else: 
    print("doesn't match")
#Ex.3
s = re.compile(r'^[a-z]+_[a-z]+$')
n = input("Ex.3: ")
if s.match(n):
    print("matches")
else: 
    print("doesn't match")
#Ex.4
s = re.compile(r'^[A-Z]{1}[a-z]+$')
n = input("Ex.4: ")
if s.match(n):
    print("matches")
else: 
    print("doesn't match")
#Ex.5
s = re.compile(r'\w*a{1}\w*b{1}$')
n = input("Ex.5: ")
if s.match(n):
    print("matches")
else: 
    print("doesn't match")
#Ex.6
n = input("Ex.6: ")
print(re.sub("[., ]", ":", n))
#Ex.7
n = input("Ex.7: ")
s = n[0]
for i in range(len(n)-1):
    if n[i] == "_":
        s += n[i+1].upper()
    else:
        s += n[i+1]
print(re.sub("[_]", "", s))
#Ex.8
n = input("Ex.8: ")
print(re.findall('[A-Z][a-z]*', n))
#Ex.9
n = input("Ex.9: ")
print(re.sub(r"(\w)([A-Z])", r"\1 \2", n))
#Ex.10
n = input("Ex.10: ")
n = re.sub(r'([a-z])([A-Z])', r'\1_\2', n)
s = n[0]
for i in range(len(n) - 1):
    if n[i] == "_":
        s += n[i+1].lower()
    else:
        s += n[i+1]
print(s)
