angles = []
for _i in range(3):
    angles.append(float(input()))

if sum(angles) == 180:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")
