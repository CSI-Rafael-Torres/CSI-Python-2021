import random
pa=0
print("This code lets you play with a magic 8ball. ")
while pa <= 0:
    input("Please ask the 8 ball a question. \n")
    pr=random.randint(1,12)
    if pr == 1:
        print("Not gonna lie, no chance ")
    elif pr == 2:
        print("0 percent chance  ")
    elif pr == 3:
        print("Of course not ")
    elif pr == 4:
        print("Nah ")
    elif pr == 5:
        print("No. ")
    elif pr == 6:
        print("Never ")
    elif pr == 7:
        print("100 percent chance at it not happening ")
    elif pr == 8:
        print("No way")
    elif pr == 9:
        print("Would say yeah but thats lying so no ")
    elif pr == 10:
        print("Nope ")
    elif pr == 11:
        print("Sure? ")
    elif pr == 12:
        print(" ")
    else:
        print("How did you even get here")
    pag =input("Would you like to play again ")
    if pag =="y":
        pa=0
    elif pag == "n":
        pa=1
    else:
        print("Enter a right answer ")