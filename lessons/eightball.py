from random import randint

question: str = input("What is your yes/no question")
response: int = randint(0, 3)

if response == 0:
    print("Yes, def")

elif response == 1:
    print("Sure buddy")
elif response == 2:
    print("My sources say no")
elif response == 3:
    print("Yes sir")
else:
    print("Nah bitch")