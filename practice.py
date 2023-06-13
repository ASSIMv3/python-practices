import random

num = random.randint(0,100)

previous_pick = None
while True:
    pick = int(input('Pick a number between 0 and 100 :'))
    if pick > 100 or pick < 0:
        print("OUT OF BOUNDS")
    elif pick == num:
        print(f"Congratulations! your pick : {pick} is equal to the num : {num}")
        break
    if previous_pick == None:
        if pick > num-10 and pick < num+10 and pick != num:
            print("WARM!")
        elif pick < num-10 or pick > num+10:
            print("COLD!")
    else:
        if abs(num - previous_pick) < abs(num - pick):
            print("COLDER!")
        elif abs(num - previous_pick) > abs(num - pick):
            print("WARMER!")
    previous_pick = pick
    
    