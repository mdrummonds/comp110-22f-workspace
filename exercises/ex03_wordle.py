"""Wordle -- the real one this time!"""
__author__ = "730482673"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word_search: str, character: str) -> bool:
    """Returns true or false depending on whether or not the character matches a letter in word_search."""
    assert len(character) == 1
    i: int = 0
    while i + 1 <= len(word_search):
        if character != word_search[i]:
            i = i + 1
        else:
            return True
    return False
            

def emojified(guess_word: str, secret: str) -> str:
    """Returns colored boxes depending on the correctedness of the character."""
    assert len(guess_word) == len(secret)
    index: int = 0
    index_tracker: int = 0
    hint: str = ""
    while index < len(secret):
        if not contains_char(secret, guess_word[index]):
            hint = hint + WHITE_BOX
            index_tracker += 1
        elif contains_char(secret, guess_word[index]) and guess_word[index] != secret[index_tracker]:
            hint = hint + YELLOW_BOX
            index_tracker += 1
        else:
            hint = hint + GREEN_BOX
            index_tracker += 1
        index += 1
    return hint

def input_guess(length: int) -> int:
    """Prompt for a guess of the correct length."""
    guess_word: str = input(f"Enter a {length} character word: ")
    while len(guess_word) != length:
        guess_word = input(f"That wasn't {length} chars! Try again: ")
    else:
        return guess_word

# Ensures word is correct length


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 1
    secret: str = "codes"
    guess_word: str = ""
    # imported emojified function for boxes
    while turn_number < len(secret) + 1:
        print(f"=== Turn {turn_number}/6 ===")
        guess_word = input_guess(len(secret))
        if guess_word != secret: 
            turn_number += 1
            print(emojified(guess_word, secret))
        elif guess_word == secret:
            print(emojified(guess_word, secret))
            exit((f"You won in {turn_number}/6 turns!"))
    else:
        exit("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()