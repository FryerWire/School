
"""
Lab 3
Maxwell Seery
"""

import numpy as np
import pint
from matplotlib import pyplot as plt
ur = pint.UnitRegistry()

def question1():
    ur.define("dollar = [currency]")
    ur.define('dollars = dollar')

    dol0 = 2000.0 * ur.dollars
    s = 5000 * ur.dollars / ur.year
    r = 0.02 / ur.year

    dt = 0.1 * ur.year 

    t = np.arange(0, 30, dt.to(ur.year).magnitude) * ur.year

    dol_history = np.zeros(len(t)) * ur.dollars

    dol = dol0
    for i in range(len(t)):
        dol_history[i] = dol

        ddol = (s + (r * dol)) * dt
        dol = dol + ddol

    plt.figure()
    plt.plot(t.to(ur.year).magnitude, dol_history.to(ur.dollars).magnitude / 1000, '--')

    math_class_formula = s * (np.exp(r * t) - 1) / r + dol0 * np.exp(r * t)

    plt.plot(t.to(ur.year).magnitude, math_class_formula.to(ur.dollars).magnitude / 1000)
    plt.xlabel("Time (years)")
    plt.ylabel("Total savings (thousands of dollars)")
    plt.legend(("Calculated by numerical integration", "Math class formula"))
    plt.show()

def question2():
    emass = 20000 * ur.kg
    pmass = 750 * ur.kg
    fmass = 450000 * ur.kg
    TSFC = 3 * 10**(-4) * ur.s/ur.m
    tmassL = emass + pmass + fmass
    tmass = tmassL
    fThrust = 6750000 * ur.N
    print("The starting mass of the rocket is: " + str(tmassL))
    masses = np.array([tmassL.magnitude]) * ur.kg
    times = np.array([0]) * ur.kg
    times = np.array([0]) * ur.s
    dt = 1 * ur.s
    t = 0 * ur.s

    while fmass > 0:
        t = t + dt
        fmass = fmass - (fThrust * TSFC) * dt
        tmass = emass + pmass + fmass
        masses = np.append(masses, tmass)
        times = np.append(times, t)

    print("ROcket is out of fuel, final mass of the rocket: " + str(tmass))
    print("this took: + str(t + 1)")
    plt.plot(times.magnitude, masses.magnitude)
    plt.title("Time vs. Mass")
    plt.xlabel("Time (s)")
    plt.ylabel("Mass (kg)")

    plt.show()

question1()
question2()


    




    


