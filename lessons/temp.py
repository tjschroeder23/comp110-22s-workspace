"""References Practice."""
 
 
def create() -> list[int]:
    """An obnoxious way to make a list."""
    list_1: list[int] = []
    i: int = 0
    while i < 3:
        list_1.append(i)
        i += 1
    return list_1


def increase(a_list: list[int], x: int) -> None:
    """Lets pump it up!"""
    i: int = 0
    while i < len(a_list):
        a_list[i] += x
        i += 1
    x += 1
    return None


def main() -> None:
    """Entrypoint of the program."""
    list_1: list[int] = create()
    list_2: list[int] = list_1
    x1: int = 2
    x2: int = x1
    # x1 = 2
    # list_1 = create()
    increase(list_1, x1)

    print(list_1)
    print(x1)
    print(list_2)
    print(x2)


if __name__ == "__main__":
    main()
