from functools import update_wrapper
import random

values = [1, 2, 3, 4, 5, 6]

roll_again = ["yes", "no"]

rollgame = input("Roll the dice ")

repeat = "Yes"

while repeat == "Yes":
    print("Rolling the dice")
    print(random.choice(values))
    input("do it again? ")

