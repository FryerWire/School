
# Constants
ELECTRONIC_MASS = 0.127573 # [kg]
PLA_density = 1240 # [kg/m^3]

# Structure volume
cap = 182017.7946 # [mm^3]
chassis = 49640.8229 # [mm^3]
drive_wheel_mount_caps = 4829.0774 # [mm^3]

# Volume and mass calculations
total_volume = (cap + chassis + drive_wheel_mount_caps) / (1e9) # [m^3]
total_mass = PLA_density * total_volume # [kg]

# System prints
print(f"\nElectrical Mass : {round(ELECTRONIC_MASS, 3)} [kg]")
print(f"Electrical Mass : {round(ELECTRONIC_MASS * 2.20462, 3)} [lbs]")
print(f"\nStructure Mass  : {round(total_mass, 3)} [kg]")
print(f"Structure Mass  : {round(total_mass * 2.20462, 3)} [lbs]")
print(f"\nTotal Mass      : {round(total_mass + ELECTRONIC_MASS, 3)} [kg]")
print(f"Total Mass      : {round((total_mass + ELECTRONIC_MASS) * 2.20462, 3)} [lbs]")

# Outputs
# Electrical Mass : 0.128 [kg]
# Electrical Mass : 0.281 [lbs]

# Structure Mass  : 0.293 [kg] 
# Structure Mass  : 0.646 [lbs]

# Total Mass      : 0.421 [kg] 
# Total Mass      : 0.928 [lbs]



