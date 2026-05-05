#Scrum Document: https://docs.google.com/document/d/1mCz1kTVHPCIYNKEsr3tRNkpy2MMk_BBCFa3kTtJkTCw/edit?tab=t.0
import random
from Semester_test_byConnor import *
from Semester_Project_Ethan import Name

user = Name()

print(f"Welcome {user.name}")
if user.age <= 5:
    print("want a popsicle")
starting_val=500
points = 0
def game():
    global points
    while points <= starting_val:
        starting_itm = random.sample(list(item.keys()), 5)

        if points >= starting_val:

            break
        while True:

            def combine():
                try:
                    global points
                    global ask1
                    global ask2


                    print(starting_itm)
                    ask1 = input("choose first combo : ")
                    ask2 = input("choose second combo : ")
                    val1 = item.get(ask1)
                    val2 = item.get(ask2)
                    points += val1 + val2

                except:
                    print("you chose the wrong thing retry")
                    combine()

            combine()
            print(points)

            if ask1 in starting_itm:
                starting_itm.remove(ask1)

            if ask2 in starting_itm:
                starting_itm.remove(ask2)

            starting_itm.append(random.choice(list(item)))
            starting_itm.append(random.choice(list(item)))
            if points >= starting_val:
                play_again=input("play again y/n? : ")
                if play_again == "y":
                    points = 0
                    starting_itm = ()
                    game()
                else:
                    print("bye")
                    break

game()














