"""Some tender, loving functions"""

def love(subject: str) -> str:

    """Given a subject as a parameter, returns a loving string."""

    return f"I love you {subject}!"

print(love(""))


def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a love message n times"""
    love_note: str = ""
    i: int = 0
    while i < n:
        i += 1
        love_note += love(to) + "\n"
    return love_note

print(spread_love("Rosie", 6))