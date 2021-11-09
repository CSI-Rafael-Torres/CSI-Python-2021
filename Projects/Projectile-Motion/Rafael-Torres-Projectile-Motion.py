import math
import os
from pathlib import Path
from experimentaldata import experimentaldata
import json
# experimentadata= {
#     "gun":"APB",
#     "caliber":"9x18mm Makarov",
#     "ammo":"9x18mm PM P gzh",
#     "building":"Ocean Tower",
#     "height" : 242.92,
#     "speed": 302,
#     "gravity":9.81
# }
def GProjectile(ExperimentalData:experimentaldata):
    time = math.sqrt((2*ExperimentalData.height)/ExperimentalData.gravity)
    distance=(ExperimentalData.speed*time)
    print("An",ExperimentalData.gun,"with",ExperimentalData.ammo,"ammo and",ExperimentalData.caliber,"caliber was fired out of",ExperimentalData.building,"It got to a distance of",distance,"meters and took",time," seconds")
# GProjectile("APB","9x18mm Makarov","9x18mm PM P gzh","Ocean Tower",242.92,302,9.81)
# ExperimentalData= experimentaldata("APB","9x18mm Makarov","9x18mm PM P gzh","Ocean Tower",242.92,750,9.81)
myDataSet ={
 experimentaldata("APB","9x18mm Makarov","9x18mm PM P gzh","Ocean Tower",242.92,750,9.81),
 experimentaldata("M4A1","5.56x45mm NATO","5.56x45mm FMJ","Ocean Tower",242.92,800,9.81),
 experimentaldata("TX-15 DML","5.56x45mm NATO","5.56x45mm M855","Ocean Tower",242.92,800,9.81),   
 experimentaldata("RPK-16 5.45x39 light machine gun","5.45x39mm","5.45x39mm PPBS gs Igolnik","Ocean Tower",242.92,650,9.81),
 experimentaldata("TDI KRISS Vector Gen.2 9x19 submachine gun","9x19mm Parabellum","9x19mm PBP gzh","Ocean Tower",242.92,950,9.81)
}
for data in myDataSet:
    print("\n---------------------------------\n")
    GProjectile(data)

MyOutputPath = Path(__file__).parents[0]
MyOutputFilePath = os.path.join(MyOutputPath, "Projectile.Motion.json")
print(MyOutputFilePath)
with open(MyOutputFilePath,"w") as outfile:
    json.dump([data.__dict__ for data in myDataSet],outfile)