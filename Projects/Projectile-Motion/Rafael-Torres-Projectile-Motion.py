import math
# time =0
# gravity =9.81
# Gun = "APB"
# AW=0.011#kg
# PS=302#m/s
# Caliber= "9x18mm Makarov"
# Ammo= "9x18mm PM P gzh"
# Building= "Ocean Tower"
# Height =242.92#ft
# d= PS*time
def GProjectile(Gun:str, Caliber:str, Ammo:str,Building:str,Height:int,Speed:int,Gravity:int):
    Time = math.sqrt((2*Height)/Gravity)
    distance=(Speed*Time)
    print("An",Gun,"with",Ammo,"ammo and",Caliber,"caliber was fired out of",Building,"with a velocity of",Speed,"This program with find its time and distance")
GProjectile("APB","9x18mm Makarov","9x18mm PM P gzh","Ocean Tower",242.92,302,9.81)