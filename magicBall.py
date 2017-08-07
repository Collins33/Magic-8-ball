import random
print("Enter any life questions you have:")
question =input()
number =random.randint(0,3)
if number == 0:
    print("Don't count on it")
elif number == 1:
    print("Signs point to yes")
elif number ==2:
    print("Better not tell you now")
else:
    print("Most likely")            
