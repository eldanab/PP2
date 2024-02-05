def reverse(str):
    a = str.split()
    s = ""
    for i in range(len(a) - 1, -1, -1):
        s += a[i] + ' '
    print(s)
str = "We are ready"
reverse(str)