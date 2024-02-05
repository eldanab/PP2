import random
print("Hello! What is your name?")
name = input()
num1 = random.randint(1, 20)
print(num1)
print("Well,", name ,", I am thinking of a number between 1 and 20. Take a guess.")
num2 = int(input())
cnt = 1
while(num1 != num2):
    if num2 > num1:
        print("Your guess is too high.")
        print("Take a guess.")
    else:   
        print("Your guess is too low.")
        print("Take a guess.") 
    num2 = int(input())
    cnt += 1
else:
    print("Good job,", name, "! You guessed my number in", cnt, "guesses!")
