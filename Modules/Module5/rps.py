import random
x=0
for x in range(0,2) :
    x=0
    print("This program lets you play rock paper scissors." )
    p_rps= input("Please choose between rock paper scissors. ")
    bn_rps = random.randint(1,3)
    if bn_rps == 1:
        b_rps = "rock"
    elif bn_rps == 2:
        b_rps = "paper"
    else:
        b_rps = "scissors"
    print("You chose",p_rps,"your opponent chose",b_rps)
    if p_rps == b_rps:
        print("Please try again, you chose the same ")
    else:
        if p_rps == "rock" and b_rps == "paper" :
            print("you lost")
        elif p_rps == "rock" and b_rps == "scissors" :
            print("you win")
        elif p_rps == "paper" and b_rps == "rock" :
            print("you win")
        elif p_rps == "paper" and b_rps == "scissors" :
            print("you lose")
        elif p_rps == "scissors" and b_rps == "rock" :
            print("you lost")
        elif p_rps == "scissors" and b_rps == "paper" :
            print("you win")
    for l in range(0,1) :
        rr = input("Would you like to play again y/n? ")
        l=0
        if rr=="y":
            l+=1
        elif rr=="n":
            x +=1
            l+=1
        else :
            print("Please put a valid statement")