import random
user_time = 0
comp_time = 0
choice = 1
while (choice <= 9):
    comp = ["snake", "water", "gun"]
    print("let computer choose his choice")
    comp_choose = random.choice(comp)


    print("now its your turn")
    print("lets choose from them\n"
          "1.snake\n 2.water\n 3.gun")
    user_choose = input()
    print("computer choose ", comp_choose)
    print("you choose", user_choose)
    if user_choose == "snake" and comp_choose == "snake":
        print("tie")
    elif user_choose == "water" and comp_choose == "water":
        print("tie")
    elif user_choose == "gun" and comp_choose == "gun":
        print("tie")
    elif user_choose == "snake" and comp_choose == "gun":
        print("computer win")
        comp_time += 1
    elif user_choose == "gun" and comp_choose == "snake":
        print("user win")
        user_time += 1
    elif user_choose == "gun" and comp_choose == "water":
        print("computer win")
        comp_time += 1
    elif user_choose == "water" and comp_choose == "gun":
        print("user win")
        user_time += 1
    elif user_choose == "snake" and comp_choose == "water":
        print("computer win")
        comp_time += 1
    elif user_choose == "water" and comp_choose == "snake":
        print("user win")
        user_time += 1
    else:
        print("invalid")
    print("choices left ", 9 - choice)
    choice = choice + 1
if (choice > 9):
    print("time limit exceeds")
print(user_time, " times user won")
print(comp_time, " times computer won")
if user_time > comp_time:
    print("finally user win the game")
else:
    print("finally computer win the game")



