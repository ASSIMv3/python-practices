import random

num = random.randint(0,100)

print("")
previous_pick = None
while True:
    pick = int(input('pick a number betwen 0 and 100 :'))
    if pick > 100 or pick < 0:
        print("OUT OF BOUNDS")
    elif pick == num:
        print(f"your pick : {pick} is equal to the num : {num}")
        break
    if previous_pick == None:
        if pick > num-10 and pick < num+10 and pick != num:
            print("WARM!")
        elif pick < num-10 or pick > num+10:
            print("COLD!")
    else:
        if num - previous_pick < num - pick:
            print("COLDER!")
        elif num - previous_pick > num - pick:
            print("WARMER!")
    previous_pick = pick
    
    