a = int(input())
b = int(input())
# ternary operator first_alternative if condition else second_alternative 
# used "\n" for printing in the new line
print(str(a) + "\n" + str(b) if a > b else str(b) + "\n" + str(a))
