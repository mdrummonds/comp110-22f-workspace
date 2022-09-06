"""A tracing challenge question."""

i: int = 0
s: str = ""

while i < 4:
    if i % 2 == 0:
        s = s + "h" # then block
    else:
        if i % 3 == 0:
            s = s + "!"
        else:
            s = s + "e"
    i = i + 1 # end of repeat block

print(s)