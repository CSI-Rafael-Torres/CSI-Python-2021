gt = 0
print("Welcome to the First Attack 2021 page")
print("There are three different visitors options")
print("The 1 day spectator pass is $12.14, the 2 day spectator pass is $21.11 and the competitors pass is $35 +10 dollars per game")
print("*Note: those with a competitors pass dont require a spectator pass")
dp = input("How many daily spectator passes would you like? ")
wp = input("How many 2 day spectator passes would you like? ")
cp = input("How many competitors passes would you like? ")
if int(cp) >= 1:
    n=1
    for n in range(1,int(cp)+1):
        g = input("How many games will competitor "+str(n)+" enter? ")
        gt += int(g)
        n += 1
dpp =int(dp)*12.14
wpp = int(wp)*21.11
cpp = int(cp)*35.00
gtp = gt*10.00
cgp = cpp+gtp
print("The cost of your daily spectator passes are $"+str(dpp))
print("The cost of your 2 day spectator passes are $"+str(wpp))
print("The cost of your competitors passes are $"+str(cpp))
print("You you are signed up for a total of", gt,"events")
print("Your total cost including games for competitors passes are $"+str(cgp))
print("Your total cost is $"+str(dpp+wpp+cgp))

