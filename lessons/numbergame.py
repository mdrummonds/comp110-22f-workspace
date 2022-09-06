

low: int = 1
high: int = 100

print("Think of a number between 1 and 100")
input("Press enter to continue...")
playing: bool = True

while playing and low <= high:
    guess: int = (high + low) // 2
    print(str(guess) + "?")
    result : str = input("Reply yes, lower, or higher")
    if result == "yes":
        print("Nice")
    elif result == "higher":
        low = guess + 1
    else: 
        high = guess -1 