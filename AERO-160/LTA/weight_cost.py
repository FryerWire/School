
import math
import json

WIDTH = [
    6, 6, 6, 6,
    4, 4, 4, 
    3, 3, 3, 3,
    2, 2, 2, 2,
    1, 1, 1, 1, 1, 1, 1,
    (3 / 4), (3 / 4), (3 / 4), (3 / 4),
    (1 / 2), (1 / 2), (1 / 2),
    (3 / 8), (3 / 8),
    (1 / 4), (1 / 4),
    (3 / 16)
]

HEIGHT = [    
    (1 / 4), (1 / 8), (1 / 16), (1 / 32),    
    (1 / 4), (1 / 8), (1 / 16),    
    (1 / 4), (1 / 8), (1 / 16), (1 / 32),   
    (1 / 1), (1 / 4), (1 / 8), (1 / 16),    
    (1 / 1), (3 / 4), (1 / 2), (1 / 4), (1 / 8), (1 / 6), (1 / 32),    
    (3 / 4), (1 / 2), (3 / 8), (1 / 4),    
    (1 / 2), (3 / 8), (1 / 4),    
    (3 / 8), (1 / 4),    
    (1 / 4), (5 / 16),    
    (3 / 16)
]

COST = [
    6.13, 4.79, 2.94, 2.94,
    4.24, 2.51, 1.85,
    2.67, 1.67, 1.15, 1.15,
    6.24, 1.78, 1.27, 0.96,
    2.91, 2.34, 1.70, 1.27, 0.93, 0.79, 0.79,
    1.36, 1.35, 0.98, 0.96,
    1.10, 0.72, 0.66,
    0.69, 0.61,
    0.48, 0.52, 0.35
]

data = {"Width": {}}

for i, width in enumerate(WIDTH):
    if width not in data["Width"]:
        data["Width"][width] = {"Height": [], "Cost": []}
    data["Width"][width]["Height"].append(HEIGHT[i])
    data["Width"][width]["Cost"].append(COST[i])

json_str = json.dumps(data, indent=4)
print(json_str)

parts_list = [
    [24, 2, (1 / 8)],
    [12, 1, (1 / 8)],
    [64, (1 / 2), (1 / 4)],
    [12, (1 / 4), (1 / 4)],
    [40, (3 / 4), (1 / 2)],
    [18.4, 1, 1],
    [273.2, (1 / 2), (1 / 2)],
]

print("")

updated_parts_list = []
for part in parts_list:
    part_amount = math.ceil(part[0] / 36)
    part_width = part[1]
    part_height = part[2]

    if part_width in data["Width"]:
        height_index = data["Width"][part_width]["Height"].index(part_height)
        price = data["Width"][part_width]["Cost"][height_index]
    else:
        print(f"ERROR: {part_width} has no data for width")

    # Appends to updated_parts_list
    part_names = [36, part_width, part_height, part_amount, price]
    updated_parts_list.append(part_names)

total_cost = 0
for part in updated_parts_list:
    price = part[4] * part[3]
    total_cost += price

    print(f"\n      Part : {part[0:3]} x ({part[3]})")
    print(f"           : ${price:.2f}")
    
print(f"\nTotal Cost : ${total_cost:.2f}")











