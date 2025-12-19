print("Please think of a number between 1 and 100")
low = 1
high = 100
medium =((high+low)/2)
state = True
while state:
    print("Is ur secret number",int(medium))
    guess =input("enter 'h' to indicate the guess is too high. enter 'l' to indicate the guess is too low")
    if guess =='c':
     print("Game over,Your secret number was",int(medium))
     state = False
    elif guess =='h':
       high = medium
       medium = ((high + low)/2)
    elif guess =='l':
       low = medium
       medium = ((high + low)/2)
    else:
       print("sorry i didn't understand ur input")   
       








    

