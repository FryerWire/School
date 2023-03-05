
while True:
    prtemps = int(input("Enter a Celsius value that is in the range from -16 to 20: "))

    if ((prtemps < -16) or (prtemps > 20)):
        print(f"\nERROR: Please enter a number withjin the range of -16 to 20 please. \n\n")
        continue
    else:
        F_max = float(prtemps * (9 / 5) + 32)
        F = [0.0]
        C = []

        while (F[-1] < F_max):
            if ((F[-1] + 5) > F_max):
                break
            else:
                F.append(F[-1] + 5)
                C.append((5 / 9) * (F[-1] - 32))

        print(f"F: {F}\tC: {C}")
        