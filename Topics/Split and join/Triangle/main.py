height = int(input())
my_row = "#"
print(my_row.center(2*height-1))

for _i in range(1, height):
    my_row = (my_row + "#" * 2)
    print(my_row.center(2 * height - 1))
