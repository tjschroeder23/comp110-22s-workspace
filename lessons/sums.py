"""Summing the elements of a list using different loops."""

__author__ = "730549837"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum
   

def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for additive in vals:
        sum += additive
    return sum
   

def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for additive in range(0, len(vals), 1):
        sum += vals[additive]
    return sum


def main() -> None:
    """Checking functionality of functions."""
    # Check functionality of 'w_sum' function
    print(w_sum([1, 2, 3]))
    print(w_sum([]))

    # Check functionality of 'f_sum' function
    print(f_sum([1, 2, 3]))
    print(f_sum([]))

    # Check functionality of 'f_range_sum' function
    print(f_range_sum([1, 2, 3]))
    print(f_range_sum([]))


if __name__ == "__main__":
    main()
