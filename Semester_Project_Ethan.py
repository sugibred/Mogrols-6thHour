
import random

class Name:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def username(self):
        self.name = input("Enter your name: ")
        print(f"Your name is {self.name}")

    def years(self):
        self.age = int(input("Enter your age: "))
        if self.age <= 14:
            print("What are you doing here????")
        elif self.age > 14:
            print(f"{self.age} years old")
        else:
            print("Error")


enter_name = Name("0", 0)
enter_name.username()
enter_name.years()

item={
    "headphones":1,
    "ice bucket":2,
    "mouse": 3,
    "microwave": 4,
    "sponge": 5,
    "fan": 6,
    "toothpaste": 7,
    "remote control": 8,
    "toaster": 9,
    "magnet" : 10,
    "plastic fork": 11,
    "baby bottle": 12,
    "teddy bear": 13,
    "frying pan": 14,
    "car key": 15,
    "egg": 16,
    "battery": 17,
    "plushie": 18,
    "cookie": 19,
    "toilet": 20
}

starting_itm = random.sample(list(item.keys()), 5)

def check():
    ask = input("Want to check an item? (y/n) : ")


    if ask == "y" or ask == "Y":
        print(starting_itm)


        x = int(input(f"Which item do you want to check? (1, 2, 3, 4, 5) : "))
        if x == 1:
            print(f"{starting_itm[0]} has {item[starting_itm[0]]} value")
        elif x == 2:
            print(f"{starting_itm[1]} has {item[starting_itm[1]]} value")
        elif x == 3:
            print(f"{starting_itm[2]} has {item[starting_itm[2]]} value")
        elif x == 4:
            print(f"{starting_itm[3]} has {item[starting_itm[3]]} value")
        elif x == 5:
            print(f"{starting_itm[4]} has {item[starting_itm[4]]} value")

        check()




    elif ask == "n" or ask == "N":
        print("ok")


    else:
        print("Error incorrect input")
        check()




check()