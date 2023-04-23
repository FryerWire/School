
"""
Visualizing Emotional Intensity Over Time Using Contour Plots
Maxwell Seery
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the source function
def source(x, y, strength):
    u = strength / (2 * np.pi) * (x / ((x ** 2) + (y ** 2)))
    v = strength / (2 * np.pi) * (y / ((x ** 2) + (y ** 2)))
    phi = strength / (2 * np.pi) * np.log(np.sqrt((x ** 2) + (y ** 2)))

    return u, v, phi

# Define the sink function
def sink(x, y, strength):
    u = -strength / (2 * np.pi) * (x / ((x ** 2) + (y ** 2)))
    v = -strength / (2 * np.pi) * (y / ((x ** 2) + (y ** 2)))
    phi = -strength / (2 * np.pi) * np.log(np.sqrt((x ** 2) + (y ** 2)))
    
    return u, v, phi

# Collect emotion data from the user
def get_emotion_data():
    print("\nVisualizing Emotional Intensity Over Time Using Contour Plots")
    emotion_data = []
    day = 1
    while True:
        emotion = input(f"\nEnter emotion for day {day} (Happy/Sad) or 'quit' to finish: ").lower()
        if emotion.lower() == "quit":
            break

        while emotion not in ("happy", "sad"):
            emotion = input("Invalid input. Enter 'Happy' or 'Sad': ")

        intensity = int(input(f"Enter intensity for day {day} (1-10): "))
        while (intensity < 1) or (intensity > 10):
            intensity = int(input("Invalid input. Enter an intensity between 1 and 10: "))

        emotion_data.append((day, emotion, intensity))
        day += 1

    return emotion_data

emotion_data = get_emotion_data()
days = len(emotion_data)

# Assign sources to Happy and sinks to Sad
sources = [(day * 10, 0.0, -intensity) for day, emotion, intensity in emotion_data if emotion == "happy"] 
sinks = [(day * 10, 0.0, -intensity) for day, emotion, intensity in emotion_data if emotion == "sad"]

# Set plot boundaries
x_coords = [day * 10 for day, _, _ in emotion_data]
min_x = max(min(x_coords) - 15, 0)
max_x = max(x_coords) + 15

# Set grid resolution
N = 30
x = np.linspace(min_x, max_x, N)
y = np.linspace(-20, 20, N)
X, Y = np.meshgrid(x, y)

# Calculate the total velocities and potentials
u_total, v_total, phi_total = np.zeros_like(X), np.zeros_like(Y), np.zeros_like(X)
for x_coord, y_coord, strength in sources:
    u, v, phi = source(X - x_coord, Y - y_coord, strength)
    u_total += u
    v_total += v
    phi_total += phi

for x_coord, y_coord, strength in sinks:
    u, v, phi = sink(X - x_coord, Y - y_coord, strength)
    u_total += u
    v_total += v
    phi_total += phi

# Normalize potentials
phi_norm = (phi_total - np.min(phi_total)) / (np.max(phi_total) - np.min(phi_total)) * 20 - 10

# Create the contour plot
plt.figure(figsize = (20, 8))
contour_levels = np.linspace(-10, 10, 100)
contour = plt.contourf(X, Y, phi_norm, levels = contour_levels, cmap = plt.cm.coolwarm)

# Customize plot appearance
plt.title("Visualizing Emotional Intensity Over Time Using Contour Plots")
plt.gca().yaxis.set_ticklabels([])
plt.xticks(np.arange(0, (days + 1) * 10, 10), [str(int(x // 10)) for x in np.arange(0, (days + 1) * 10, 10)])
plt.yticks([])

# Print the emotion data to the terminal
print("\nDay\tEmotion\tIntensity")
for day, emotion, intensity in emotion_data:
    print(f"{day}\t{emotion}\t{intensity}")

# Set plot limits
plt.xlim(min_x, max_x)
plt.ylim(-20, 20)

# Add streamlines
stream = plt.streamplot(X, Y, u_total, v_total, density = 2, color = 'white', linewidth = 0.5, zorder = 1)

# Add the color bar
plt.colorbar(contour)

# Show the plot
plt.show()

