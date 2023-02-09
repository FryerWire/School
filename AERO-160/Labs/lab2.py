
import numpy as np
from matplotlib import pyplot as plt

# Problem 1

# Part 1
A = [1, 3, 5]
B = [-1, 4, 8]

C = [
    (1 * (-1)),
    (3 * 4),
    (5 * 8)
]

print(f"1.A: {C}")

# Part 2
magnutude = 0
for i in range(len(C)):
    magnutude += (C[i] ** 2)

magnutude = magnutude ** (1/2)

print(f"1.B: {magnutude}")

# Part 3
unit_vector = [0, 0, 0]
for i in range(len(C)):
    unit_vector[i] = C[i] /magnutude

print(f"1.C: {unit_vector}")

# Problem 2
# Part A
A = np.array([5, 3, 5])
B = np.array([4, 2, 7])
C = A - B

print(f"2.1: {C}")

# Part B
magnutude = 0
for i in range(len(C)):
    magnutude += np.sqrt(C[i] ** 2)

print(f"2.B: {magnutude}")

# Part C
unit_vector = C / np.linalg.norm(C)

print(f"2.C: {unit_vector}")

# Problem 3
# Part 1
V_naught = 130
gravity = 9.81
theta = 40 * (np.pi / 180)
time = np.arange(0, 10, 0.1)

x = V_naught * np.cos(theta) * time
y = V_naught * np.sin(theta) * time - (1 / 2) * gravity * (time ** 2)

plt.plot(x, y)
plt.title("x vs y")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()

# Problem 4
x = np.linspace(0, 1, 100)
t = 0.3

y_t = (5 * t) * (
    (0.2969 * np.sqrt(x)) - 
    (0.1260 * x) - 
    (0.3516 * (x ** 2)) + 
    (0.2843 * (x ** 3)) -
    (0.1015 * (x ** 4))
)

plt.plot(x, y_t)
plt.plot(x, -y_t)
plt.title("x vs y")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()


