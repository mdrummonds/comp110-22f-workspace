"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730482673"

mystery_word: str = "python"
# can be changed to any word of any length, initial word the user is trying to guess.
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
hint: str = ""
# hint refers to the colored boxes that give the user information about the correctness of their guessed word.
guess_word: str = input(f"What is your { len(mystery_word) }-letter guess?")
# this prompts the user to guess a word

while len(guess_word) != len(mystery_word):
    print(f"That was not {len(mystery_word)} letters! Try again:")
    guess_word = input("")
# If the user does not insert the correct amount of letters, they can try again until they place the correct amount

while guess_word != mystery_word and i + 1 <= len(mystery_word):
    if guess_word[i] == mystery_word[i]:
        getting_warmer = True
        hint = hint + GREEN_BOX
        # green box prints when a letter is in the correct spot
    else:
        index_tracker: int = 0
        getting_warmer: bool = False 
        while getting_warmer == False and index_tracker + 1 <= len(mystery_word):
            if guess_word[i] == mystery_word[index_tracker]:
                getting_warmer = True
                index_tracker = index_tracker + 1
            else: 
                index_tracker = index_tracker + 1
        if getting_warmer:
            hint = hint + YELLOW_BOX
            # yellow box prints if letter is not in the right spot, but exists in the mystery word.
        else:
            hint = hint + WHITE_BOX
            # prints a white box if letter is not within the mystery word.
    i = i + 1
if guess_word != mystery_word:
    print(hint)
    print("Not quite. Play again soon!")
# whenever the word isn't guessed correctly a while loop runs to find which letters fit, if they would fit into another part of the word, or if they don't fit at all.

if guess_word == mystery_word:
    hint = GREEN_BOX * len(mystery_word)
    print(hint)
    print("Woo! you got it!")
# green boxes print when all letters are correct, meaning the user guessed the correct word.