import math
import experimentaldata
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
    Time = math.sqrt((2*ExperimentalData.height)/ExperimentalData.gravity)
    distance=(ExperimentalData.speed*Time)
    print("An",ExperimentalData.gun,"with",ExperimentalData.ammo,"ammo and",ExperimentalData.caliber,"caliber was fired out of",ExperimentalData.building,"with a velocity of",ExperimentalData.speed,"This program with find its time and distance")
# GProjectile("APB","9x18mm Makarov","9x18mm PM P gzh","Ocean Tower",242.92,302,9.81)
ExperimentalData= experimentaldata("APB","9x18mm Makarov","9x18mm PM P gzh","Ocean Tower",242.92,302,9.81)
