a: str = "xy"
print(a)
a += "x"
print(a)


def ch_str(b: str) -> None:
    b += "z"
    return None


ch_str(a)
print(a)

b: list[str] = ["x", "y"]
print(b)
b.append("z")
print(b)


def chg_lst(c: list[str]) -> None:
    c.append("q")
    return None


chg_lst(b)

print(b)
