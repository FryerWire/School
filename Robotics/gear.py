
"""
Gear calculations for input and output gears
"""

import numpy as np

# Constants
DSM = 200 # DSM = Max Diameter System
shell_wall = 5 # mm
track_length = 20 # mm
# OGDR = DSM - shell_wall - track_length # Output Gear Diameter Root
OGDR = (69 * 2)
OGT = 100 # OGT = Output Gear Teeth
MODULE = OGDR / (OGT + 2.5) 

def gear(tooth_division, radius):
    z = OGT / tooth_division
    diameter = MODULE * z
    tooth_height = 2.25 * (MODULE)
    pitch = (np.pi * MODULE) # / 2 gives the actual tooth and gap space
    theta = pitch / (radius / 2)

    print(theta)

    return [z, diameter, tooth_height, pitch, theta]

data = [gear(4, 34), gear(1, 135)]
naming_convention = ["Input", "Output"]
data_naming = [
    "Teeth Number     ",
    "Reference Diamter",
    "Tooth Height     ",
    "Pitch            ",
    "Theta            "
]

print("")

for i in range(len(data)):
    for j in range(len(data[i])):
        if (i == 0):
            # print(f"{naming_convention[i]} Gear {data_naming[j]}  : {data[i][j]}")
            print(f"{naming_convention[i]} Gear {data_naming[j]}  : {round(data[i][j])}")
        else:
            # print(f"{naming_convention[i]} Gear {data_naming[j]} : {data[i][j]}")
            print(f"{naming_convention[i]} Gear {data_naming[j]} : {round(data[i][j])}")
    
    print("")

gear_ratio = data[0][0] / data[1][0]
input_RPM = 500 # Originally 200
output_RPM = input_RPM * gear_ratio

print(f"Gear Ratio (O/I)              : {gear_ratio}")
print(f"Input RPM                     : {input_RPM}")
print(f"Input RPS                     : {round(input_RPM / 60, 3)}")
print(f"Output RPM                    : {output_RPM}")
print(f"Output RPS                    : {round(output_RPM / 60, 3)}")

print(f"\nWorking Space                 : {round(OGDR - (2 * data[0][1]), 3)}")



        
