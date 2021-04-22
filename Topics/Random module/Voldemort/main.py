import random


# work with this variable
n = int(input())
random.seed(n)
word = []
for char in "Voldemort":
    word.append(char)
index = random.randint(0, len(word))
print(word[index])
