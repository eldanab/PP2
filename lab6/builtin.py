# #Ex.1
import math
num = [2, 5, 3, 8, 1]
prod = math.prod(num)
print(prod)
# #Ex.2
s = input()
num_up = 0
num_low = 0
for i in s:
    if i.islower():
        num_low += 1
    else:
        num_up += 1
print("Uppercase:", num_up, " Lowercase:", num_low)
# #Ex.3
s = input()
l = int(len(s)/2)
for i in range(l):
    ispal = True
    if s[i]!= s[len(s) - 1 - i]:
        ispal = False
        print("Not palindrome")
        break
if ispal:
    print("Palindrome")  
# Ex.4     
import time
num = int(input())
ms = int(input())
time.sleep(ms / 1000) 
res = math.sqrt(num)
print(f"Square root of {num} after {ms} milliseconds is {res}")
#Ex.5
a = (1,3, 0, 1, 6)
if all(a):
    print(True)
else:
    print(False)
