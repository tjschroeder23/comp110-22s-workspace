"""A set of dictionary functions."""

__author__ = "tjschroeder23"


def main() -> None:
    a: dict[str, str] = {"tim": "great", "jaidyn": "super", "kellyn": "super great"}
    print(a)
    print(invert(a))
    a = {"tim": "blue", "jaidyn": "white", "keisa": "green", "kellyn": "green"}
    print(a)
    print(favorite_color(a))
    c: list[str] = ["tim", "jaidyn", "keisa", "jaidyn", "kellyn"]
    print(count(c))
    

def invert(a: dict[str, str]) -> dict[str, str]:
    c: dict[str, str] = dict()
    b: dict[str, int] = {}
    for key in a:
        if a[key] in b:
            b[a[key]] += 1
            raise KeyError("Duplicate values trying to invert into the same key")
        else:
            b[a[key]] = 1
    for key in a:
        if a[key] not in c:
            c[a[key]] = key
    return c


def favorite_color(a: dict[str, str]) -> str:
    b: dict[str, int] = {}
    for key in a:
        if a[key] in b:
            b[a[key]] += 1
        else:
            b[a[key]] = 1
    i: int = 0
    fav_color: str = ""
    for key in b:
        if b[key] > i:
            i = b[key]
            fav_color = key
    return fav_color
  

def count(a: list[str]) -> dict[str, int]:
    b: dict[str, int] = dict()
    for item in a:
        if item in b:
            b[item] += 1
        else:
            b[item] = 1
    return b


if __name__ == "__main__":
    main()
