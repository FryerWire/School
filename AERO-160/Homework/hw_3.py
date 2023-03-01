
"""
Homework 3
Maxwell Seery
"""

# Constants
R = 287 # [J / (kg * K)]
GRAVITY_M = 9.81 # [m / (s^2)]
GRAIVTY_I = 32.2 # [ft / (s^2)]

# Lambda functions
rho_PT = lambda Pressure, Temperature: Pressure / (R * Temperature) # [kg / (M^3)]
rho_mV = lambda mass, Volume: mass / Volume # [kg / (M^3)]

# Question 2.1 and 2.8
def question_1_and_4():
    """
    Density and Specific Volume calculcations
    Used for Problems 2.1 and 2.8

    Returns
        - rho (float)             : Density (rho) [kg / (M^3)]
        - specific_volume (float) : Specific volume (v)
    """

    Pressure_air = 1.2 # [atm]
    Temperature = 300 # [K]

    rho = rho_PT(Pressure_air, Temperature) # [kg / (M^3)]
    specific_volume = rho ** (-1) # {1 / [kg / (M^3)]}

    return rho, specific_volume

# Question 2.3
def question_2():
    """
    Weight measurement calculator from Pressure, Temperature, and Volume
    Used for Problem 2.3

    Returns
        - Weight (float) : Weight (W) [lb_f]
    """

    length = 20 # [ft]
    width = 15 # [ft]
    height = 8 # [ft]

    Volume = length * width * height
    Pressure = 2116 # [lb / (ft^2)]
    Temperature = 59 # [deg F]
    rho = rho_PT(Pressure, Temperature) # [slug / (ft^3)]

    Weight = (rho * Volume) * GRAIVTY_I # [lb_f]

    return Weight

# Question 2.5
def question_3():
    """
    Pressure calculator from Temperature, Volume, and Mass

    Returns
        - Pressure (float) : Pressure (P) [psi]
    """

    pound_mass = 1500 # [lb_m]
    Volume = 900 # [ft^3]
    Temperature = 70 + 459.67 # [deg_R]
    rho = rho_mV(pound_mass, Volume) # [lb_m / (ft^3)]

    Pressure = rho * R * Temperature # [psi]

    return Pressure

# Question 3.16
def question_5():
    """
    Gravity strength at 70k ft vs gravity strength at sea level calculator

    Returns
        - g_70k (float)      : Gravity (g) [ft / (s^2)]
        - g_sealevel (float) : Gravity (g) [ft / (s^2)]
    """
    
    # Constants
    G = 6.67430e-11  # [ft^3/lb s^2] Gravitational Constant
    M = 5.9722e24  # [lb_m] Mass of the Earth 
    R = 3959e3  # [ft] Radius of the Earth
    h = 70000 # [feet] Altitude

    # Altitudes
    g_sealevel = (G * M) / (R ** 2) # Acceleration due to gravity at sea level
    g_70k = (G * M) / ((R + h) ** 2) # Acceleration due to gravity at altitude h
    delta_g = g_70k - g_sealevel

    return g_70k, g_sealevel, delta_g

# Question 2.1 and 2.8
print("\nQuestion 2.1")
print(f"Density (rho): {question_1_and_4()[0]:.3e} [kg / m^3]")
print(f"Specific Volume (v): {round(question_1_and_4()[1], 3)} [m^3 / kg]")

print("\nQuestion 2.3")
print(f"Weight (W): {round(question_2(), 3)} [lb_f]")

print("\nQuestion 2.5")
print(f"Pressure (P): {round(question_3(), 3)} [psi]")

print("\nQuestion 2.8")
print(f"Specific Volume (v): {round(question_1_and_4()[1], 3)} [m^3 / kg]")

print("\nQuestion 3.16")
print(f"Gravity at 70,000 ft (h_G) differs by: {round(32.2 - question_5()[1], 3)} [ft / (s^2)]")


question_5()
