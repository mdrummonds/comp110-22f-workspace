"""Choose your own adventure project--Speed Dating."""

__author__ = "730482673"

from random import randint

HEARTBROKEN_EMOJI: str = "\U0001F494"
FIRE_EMOJI: str = "\U0001F525"
player: str = ""
points: int = 0


def greet() -> None: 
    """Greets the player and prompts for a name."""
    global player
    print("Welcome to speed dating!")
    player = input("What is your name?")


def first_choice() -> int:
    """Player makes the first decision based on three choices."""
    global player
    first_decision: int = int(input(f"Let's get started {player}. Would you rather go on a date with Simon (1), Callie (2), or die alone (3). Type the corresponding number."))
    return first_decision


def second_choice(first_decision: int) -> int:
    """Player makes second decision based on first decision and is given three new choices."""
    global points
    if first_decision == 1:
        points += 5
        print(f"Great choice, {player}. You now have {points} love points")
        decision_2: int = int(input("Should you talk about your obsession with cats (1), discuss your love for computer science (2), or insult Simon's outfit (3)? Type the corresponding number."))
    if first_decision == 2:
        points += 5
        print(f"Interesting decision {player}. You now have {points} love points")
        decision_2: int = int(input("Should you talk about National Geographic's shark week (1), your favorite episode of spongebob (2), or ask about Callie's day (3)?"))
    return decision_2


def num_return_high(love_points: int) -> int:
    """Returns the new value of points based on the best decision."""
    global points
    love_points += 25
    print(f"You now have {love_points} love points")
    return love_points


def num_return_random(love_points: int) -> int:
    """Returns points with an added random value for an average choice."""
    global points
    love_points += randint(0, 10)
    print(f"You now have {love_points} love points")
    return love_points


def num_return_negative(love_points: int) -> int:
    """Takes away points for a bad response."""
    global points
    love_points -= 15
    print(f"You now have {love_points} love points")
    return love_points


def main() -> None:
    """The main entrypoint of the speed dating program."""
    global points
    global player
    speedy: bool = True 
    greet()
    while speedy:
        decision: int = first_choice()
        if decision == 1:
            decision_2: int = second_choice(decision)
            if decision_2 == 1:
                print(f"Great choice! Simon also has a weird obsession with cats.{FIRE_EMOJI}")
                points = num_return_high(points)
            elif decision_2 == 2:
                print("Simon says he doesn't like nerds.")
                points = num_return_negative(points)
            elif decision_2 == 3:
                print("Simon also hates his outfit, his mom made him wear it.")
                points = num_return_random(points)
            else: 
                print("That wasn't an option.")
        if decision == 2:
            decision_2: int = second_choice(decision)
            if decision_2 == 1:
                print("Bad choice, Callie is scared of sharks. She left the date crying.")
                points = num_return_negative(points)
            elif decision_2 == 2:
                print(f"Great choice! Who doesn't like spongebob?{FIRE_EMOJI}")
                points = num_return_high(points)
            elif decision_2 == 3:
                print("Good, but not the best option. Try spicing things up.")
                points = num_return_random(points)
        if decision == 3:
            points -= 25
            print(f"{player} leaves and eventually dies alone with {points} love points.{HEARTBROKEN_EMOJI}")
        more_rounds: str = input("Play again? (Type Yes or No)")
        if more_rounds == "Yes":
            speedy = True
        else: 
            speedy = False

    else: 
        print(f"{player} gave up on love at {points} love points.")


if __name__ == "__main__":
    main()