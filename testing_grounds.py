import random
ask= input("say y to start")
item = {
    "vr1": 1,
    "vr2": 2,
    "vr3": 3,
    "vr4": 4,
    "vr5": 5,
    "vr6": 6,
    "vr7": 7,
    "vr8": 8,
    "vr9": 9,
    "vr10": 10,
    "vr11": 11,
    "vr12": 12,
    "vr13": 13,
    "vr14": 14,
    "vr15": 15,
    "vr16": 16,
    "vr17": 17,
    "vr18": 18,
    "vr19": 19,
    "vr20": 20,
}
if ask == "y":
    starting_itm = random.sample(list(item.keys()), 5)
    starting_val=40
    while ask == "y":

        print(starting_itm)
        ask1=input("choose first combo ")
        ask2=input("choose second combo ")
        val1=item.get(ask1)
        val2=item.get(ask2)
        combine = val1 +val2
        print(combine)
        if combine in item.values():
            starting_itm.pop(0)
            for key, value in item.items():
                if value == combine:
                    starting_itm.append random.sample(list(item.keys()),1),
                    print(starting_itm),
        if combine >= starting_val:
            print("you won")
            break




else:
    print("bye")







'''if items["vr20"]+items["vr20"]==40:
    print("you have won")'''
