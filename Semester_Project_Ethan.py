
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
        else:
            print(f"{self.age} years old")


enter_name = Name("0", 0)
enter_name.username()
enter_name.years()

wood = 1
stone = 2




def Ask():
    ask = input("Want to check an item? (y/n) : ")
    if ask == "y":

        x = int(input(f"Which item do you want to check? ( 1, 2) : "))
        if x == 1:
            print(f"wood is {wood} value")
        elif x == 2:
            print(f"stone is {stone} value")

    elif ask == "n":
        print("ok")

    else:
        print("Error incorrect input")
        Ask()

Ask()
