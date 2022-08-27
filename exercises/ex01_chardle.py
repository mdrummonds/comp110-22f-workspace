"""EX01 - Chardle - Knockoff Wordle."""

__author__ = "730482673"

first_word: str = input("Enter a 5-character word: ")

if len(first_word) != 5:
    exit("Error: Word must contain 5 letters")

initial_letter: str = input("Enter a single character: ")

if len(initial_letter) != 1:
    exit("Error: Character must be a single character.")

letter_count: int = 0



print("Searching for " + initial_letter + " in " + first_word)

if initial_letter == first_word[0]: 
    print(initial_letter + " found at index 0")
    letter_count = letter_count + 1

if initial_letter == first_word[1]:
    print(initial_letter + " found at index 1")
    letter_count = letter_count + 1

if initial_letter == first_word[2]:
    print(initial_letter + " found at index 2")
    letter_count = letter_count + 1

if initial_letter == first_word[3]:
    print(initial_letter + " found at index 3")
    letter_count = letter_count + 1

if initial_letter == first_word[4]:
    print(initial_letter + " found at index 4")
    letter_count = letter_count + 1

if letter_count < 1:
    print("No instances of " + initial_letter + " found in " + first_word)

if letter_count == 1:
    print(str(letter_count) + " instance of " + initial_letter + " found in " + first_word)

if letter_count > 1:
    print(str(letter_count) + " instances of " + initial_letter + " found in " + first_word)


    

