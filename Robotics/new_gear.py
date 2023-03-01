
import numpy as np

# Constants
OUTPUT_TEETH = 27 * 3
OUTPUT_GEAR_REFERENCE_DIAMETER = 150
MODULE = OUTPUT_GEAR_REFERENCE_DIAMETER / OUTPUT_TEETH

input_gear_reference_diameter = OUTPUT_GEAR_REFERENCE_DIAMETER / 3
input_teeth = input_gear_reference_diameter / MODULE
system_height = 32 + input_gear_reference_diameter
tire_diameter = 1.5 * system_height
usable_space = OUTPUT_GEAR_REFERENCE_DIAMETER - 10

# System Checks
print(f"\nUsable Space Diameter : {round(usable_space / 25.4, 1)} [in]")
print(f"Tire Diameter         : {round(tire_diameter / 25.4, 1)} [in]")
print(f"System Height         : {round(system_height  / 25.4, 1)} [in]")
print(f"OG Reference Diameter : {round(OUTPUT_GEAR_REFERENCE_DIAMETER  / 25.4, 1)} [in]")
print(f"IG Reference Diameter : {round(input_gear_reference_diameter  / 25.4, 1)} [in]")

print(f"\nUsable Space Radius   : {round(usable_space / 2, 1)} [mm]")
print(f"Tire Diameter         : {round(tire_diameter, 1)} [mm]")
print(f"Tire Radius           : {round(tire_diameter / 2, 1)} [mm]")
print(f"System Height         : {round(system_height, 1)} [mm]")
print(f"\nOG Reference Diameter : {round(OUTPUT_GEAR_REFERENCE_DIAMETER, 1)} [mm]")
print(f"OG Reference Radius   : {round(OUTPUT_GEAR_REFERENCE_DIAMETER / 2, 1)} [mm]")
print(f"IG Reference Diameter : {round(input_gear_reference_diameter, 1)} [mm]")
print(f"IG Reference Radius   : {round(input_gear_reference_diameter / 2, 1)} [mm]")
print(f"Input Teeth           : {round(input_teeth)}")
