import pytest


def main() -> None:
    print(max_list([1, 2, 3, -4, 6, 0]))
    print(invert({"blue": "a", "yellow": "b"}))
    with pytest.raises(KeyError):
        # my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert({'kris': 'jordan', 'michael': 'jordan'})


def max_list(a: list[int]) -> int:
    b: int = 0
    b = max(a)
    return b


def invert(a: dict[str, str]) -> dict[str, str]:
    b: dict[str, str] = dict()
    # c: dict[str, str] = dict()
    for key in a:
        # if a[key] not in b:
        b[a[key]] = key
        # else:
        #     c[key] = "could not invert because dupicate key of " + a[key]
        # raise KeyError("KeyError for duplicate values trying to invert into the same key")
    # if c != {}:
    #     print(c)
    return b


if __name__ == "__main__":
    main()
