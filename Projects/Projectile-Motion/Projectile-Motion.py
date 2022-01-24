import math
import os
from pathlib import Path
from experimentalData import ExperimentalData
import json

def GProjectile(experimentaldata: ExperimentalData):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]
    planet = planets.index(experimentaldata.planet)
    time = math.sqrt((2*experimentaldata.height)/g_ms2[planet])
    distance=(experimentaldata.speed*time)
    print("An",experimentaldata.gun,"with",experimentaldata.ammo,"ammo and",experimentaldata.caliber,"caliber was fired out of",experimentaldata.building,"It got to a distance of",distance,"meters and took",time," seconds")
    print("The experiment is done on",experimentaldata.planet,"With a gravity of",g_ms2[planet])
# GProjectile("APB","9x18mm Makarov","9x18mm PM P gzh","Ocean Tower",242.92,302,9.81)
# ExperimentalData= experimentaldata("APB","9x18mm Makarov","9x18mm PM P gzh","Ocean Tower",242.92,750,9.81)
myDataSet = [
ExperimentalData("APB","9x18mm Makarov","9x18mm PM P gzh","Ocean Tower",242.92,750,"Earth"),
ExperimentalData("M4A1","5.56x45mm NATO","5.56x45mm FMJ","Ocean Tower",242.92,800,"Mars"),
ExperimentalData("TX-15 DML","5.56x45mm NATO","5.56x45mm M855","Ocean Tower",242.92,800,"Venus"),   
ExperimentalData("RPK-16 5.45x39 light machine gun","5.45x39mm","5.45x39mm PPBS gs Igolnik","Ocean Tower",242.92,650,"Earth"),
ExperimentalData("TDI KRISS Vector Gen.2 9x19 submachine gun","9x19mm Parabellum","9x19mm PBP gzh","Ocean Tower",242.92,950,"Jupiter")
]
for data in myDataSet:
    print("\n---------------------------------\n")
    GProjectile(data)

MyOutputPath = Path(__file__).parents[0]
MyOutputFilePath = os.path.join(MyOutputPath, 'Projectile-Motion.json')
print(MyOutputFilePath)
with open(MyOutputFilePath,'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)
deserialize = open(MyOutputFilePath)
experimentJson = json.load(deserialize)
for e in experimentJson:
    print("\n---------------------------------\n")
    GProjectile(ExperimentalData(**e))
