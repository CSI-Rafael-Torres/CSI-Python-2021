def weight(e_weight,planet_g,planet) :
    weight=e_weight*planet_g
    print("your mass in kg is",e_weight)
    print("Your weight in earth is "+str(e_weight*9.81)+"kg.")
    print("Your weight in",planet,"is "+str(weight)+"kg.")
wght= input("Enter your weight ")
mass = int(wght)/9.81
mass_k = mass*2.205
planet =input("Input the planet ")
if planet == "Mercury" :
    gravity =3.7
elif planet == "Venus" :
    gravity = 8.87
elif planet == "Earth" :
    gravity = 9.81
elif planet == "Mars" :
    gravity = 3.711
elif planet == "Jupiter" :
    gravity = 24.79
elif planet == "Saturn" :
    gravity = 10.44
elif planet == "Uranus" :
    gravity = 8.69
elif planet == "Neptune" :
    gravity = 11.15
else : 
    print("please input a proper planet")
weight(int(mass_k),gravity,planet)

