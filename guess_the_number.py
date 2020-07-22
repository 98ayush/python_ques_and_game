n=18
print("user your hava to guess a number and for that u only have 8 chances")
number_of_guess=1
while(number_of_guess<=9):
    guess_number = int(input("enter the number "))
    if guess_number > 18:
        print("you guessed an larger number pls guess low number")
    elif guess_number < 18:
        print("you guess a lower number pls guess a high number")
    else:
        print("you won the game")
        print("you guessed the number in ",number_of_guess," times")
        break
    number_of_guess=number_of_guess+1
if(number_of_guess>9):
    print("you did not guessed the number even in 9 times ")
    print("game over")

