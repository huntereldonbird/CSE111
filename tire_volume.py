import math
from datetime import datetime


width = input("Enter the width of the tire in mm (ex 205): ")

AspectR = input("Enter the aspect ratio of the tire (ex 60): ")

Diameter = input("Enter the diameter of the wheel in inches (ex 15): ")

width = float(width)

AspectR = float(AspectR)

Diameter = float(Diameter)


volume = (math.pi * (width * width) * AspectR * (width * AspectR + (2540 * Diameter)))/ 10000000000

volume = round(volume, 2)

currentDateTime = datetime.now()


print(str(volume))

with open("volumes.txt", "at") as file:

    print(f"{currentDateTime:%Y-%m-%d}, {width}, {AspectR}, {Diameter}, {volume}", file=file)