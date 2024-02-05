def perm(str1, str2 = ''):
    if not str1:
        print(str2)
    else:
        for i in range(len(str1)):
            ch = str1[:i] + str1[i + 1:]
            perm(ch, str2 + str1[i])

str1 = input()
perm(str1)
