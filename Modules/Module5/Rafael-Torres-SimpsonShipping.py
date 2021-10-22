print("Welcome to Homers Shipping. ")
w= input("What is the weight of the packaging in pounds? ")
wf = float(w)
if wf<=2 and wf >=0:
    pgs= 1.75*wf+20
    pcs= 3.5*wf+5.00
    pds= 5.25*wf
elif wf<=6 and wf>2 :
    pgs= 3.5*wf+20
    pcs= 7*wf+8
    pds= 10.5*wf
elif wf<=10 and wf>6 :
    pgs= 4.5*wf+20
    pcs= 9*wf+12
    pds= 13.5*wf
elif wf>10 :
    pgs= 5.25*wf+20
    pcs= 10*wf+15
    pds= 15.75*wf
else:
    print("please input an actual weight")


print("The cost of the ground shipping will be "+str(pgs)+"$")
print("The cost of the premium ground shipping will be "+str(pgs+150)+"$")
print("The cost of the courier shipping will be "+str(pcs)+"$")
print("The cost of the drone shipping will be "+str(pds)+"$")
sm=input("Which would you like to choose(ground/premium/courier/drone) ")
if sm == "ground":
    print("Your bill is "+str(pgs)+"$")
    print("Thanks for using our services")
elif sm == "premium":
    print("Your bill is "+str(pgs+150)+"$")
    print("Thanks for using our services")
elif sm == "courier":
    print("Your bill is "+str(pcs)+"$")
    print("Thanks for using our services")
elif sm == "drone":
    print("Your bill is "+str(pds)+"$")
    print("Thanks for using our services")
else:
    print("Please enter a valid shipping method")