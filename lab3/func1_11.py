def palindrome(s):
    for i in range(int(len(s)/2)):
        if(s[i] != s[len(s) - 1 - i]):
            return False
    return True

a = "madam"
b = "123321"
c = "abbc"
print(palindrome(a), palindrome(b), palindrome(c))