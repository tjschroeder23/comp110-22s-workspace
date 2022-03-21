"""test print characters."""

WHITE_BOX: str = "\U00002B1C" + " "
GREEN_BOX: str = "\U0001F7E9" + " "
YELLOW_BOX: str = "\U0001F7E8" + " "

x: int = 1

while x < 128:
    print(f"{x}  {chr(x)}")
    x = x + 1
