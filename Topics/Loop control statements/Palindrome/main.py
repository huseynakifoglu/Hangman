def split(word):
    return [char for char in word]


text = split(input())
is_palindrome = True
for i in range(0, int(len(text) / 2)):
    if text[i] == text[len(text) - i - 1]:
        continue
    else:
        is_palindrome = False

if is_palindrome:
    print("Palindrome")
else:
    print("Not palindrome")
