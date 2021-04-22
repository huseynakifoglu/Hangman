# Write your code here
import random

words = {'python', 'java', 'kotlin', 'javascript'}

print("H A N G M A N")

chosen_word = random.choice(tuple(words))
# in order to split the string with space I used "- " so after split it will look like
# --------- something like that after removing space with split
# as by default split() function makes list based on spaces.
hidden_part = ("- " * len(chosen_word)).split()

open_part = chosen_word[:]
answers = set()
tries = 8

# print("""Type "play" to play the game, "exit" to quit:""")
state = True
while True:
    choice = input("""Type "play" to play the game, "exit" to quit:""")
    if choice == "play":
        state = True
        break
    if choice == "exit":
        state = False
        break
    else:
        continue

if state:
    while tries > 0:
        print("\n" + ''.join(str(e) for e in hidden_part))
        answer = input("Input a letter: ")

        if len(answer) > 1:
            print("You should input a single letter")
            continue
        if not answer.islower():
            print("Please enter a lowercase English letter")
            continue

        if answer in chosen_word and answer not in hidden_part:
        # this code below finds the indices of the character given as x
        # and adds them into the indices list so I can check it with answer
            indices = [i for i, x in enumerate(chosen_word) if x == answer]
            for index in range(len(indices)):
                hidden_part[indices[index]] = answer
        elif answer in answers:
            print("You've already guessed this letter")
            continue
        # tries -= 1
        elif answer not in chosen_word:
            print("That letter doesn't appear in the word")
        # after each input the chances decreases by 1
            tries -= 1
        answers.add(answer)
        # print(answers)
        if hidden_part.count("-") == 0:
            print("You guessed the word!" + "\n" + "You survived!")
            break
        if tries == 0:
            print("You lost!")
            break
if not state:
    exit()
