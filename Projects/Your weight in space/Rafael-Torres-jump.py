def jump(jump,planet_g,planet,unit) :
    jumped = jump*planet_g
    print("You would jump for",jumped,unit,"on",planet)
    print("and you jumped for",jump,unit,"on Earth")

print("This code calculates your jump length on another planet ")
planet =input("Please input the planet ")
if planet == "Mercury" :
    gravity =2.65
elif planet == "Venus" :
    gravity = 1.11
elif planet == "Earth" :
    gravity = 1
elif planet == "Mars" :
    gravity = 2.64
elif planet == "Jupiter" :
    gravity = 0.40
elif planet == "Saturn" :
    gravity = 0.94
elif planet == "Uranus" :
    gravity = 1.13
elif planet == "Neptune" :
    gravity = 0.88
else : 
    print("Please input a proper planet")
unit=input("Will you use meters or inches? ")
if unit =="inches":
    jump_d= input("Enter the jump length in inches ")
    jump(float(jump_d),gravity,planet,unit)
elif unit == "meters":
    jump_d= input("Enter the jump length in meters ")
    jump(float(jump_d),gravity,planet,unit)
else:
    print("Input a proper unit")
