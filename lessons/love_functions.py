"""Given a name as a parameter, returns a loving string."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note


# spread_love("MOM", 100)
print(spread_love("MOM", 2))


def mystery(n: int) -> str:
    """A useless function."""
    i: int = 0
    while i < n:
        if i % 2 == 1:
            return "ooh"
        i += 1
    return "ahh"


print(mystery(4))


def main() -> None:
    print("main()")
    y: float = 5.67
    print(double(y))
    print(halve(y))


def halve(x: float) -> float:
    print(f"halve({x})")
    return x / 2.0


def double(x: float) -> float:
    print(f"double({x})")
    return x * 2.0


if __name__ == "__main__":
    print("name is '__main__'")
    main()
