answer = 7
guess = int(input("Enter a number between 1 to 10: "))

if guess < answer:
    print("Please guess higher!")
    guess = int(input())
    if guess == answer:
        print("You got it right!")
    else:
        print("Sorry better luck next time!")    

elif guess > answer:
    print("Please guess lower!")
    guess = int(input())
    if guess == answer:
        print("You got it right!")
    else:
        print("Better luck next time!")    

else:
    print("You got it right!!!")