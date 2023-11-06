"""A set of utility functions."""

__author__ = "tjschroeder23"


def all(list_1: list[int], check_int: int) -> bool:
    ct: int = 0
    # If input list is empty, quit function early and return False
    if len(list_1) == 0:
        return False
    
    while ct < len(list_1):
        if check_int != list_1[ct]:
            # If input integer does not match any item in input list, quit function early and return False
            return False
        ct += 1
    return True


def max(list_1: list[int]) -> int:
    if len(list_1) == 0:
        return 0
    # if len(list_1) == 0:
    #     raise ValueError("max() arg is an empty List")
    
    # Make max_num the first integer in the list to start
    max_num: int = list_1[0]
    ct: int = 0
    while ct < len(list_1):
        # If current list integer is larger than current max number, reassign max number to current list integer
        if max_num < list_1[ct]:
            max_num = list_1[ct]
        ct += 1
    return max_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    # If list lengths aren't equal, lists can't be equal, so return a False
    if len(list_1) != len(list_2):
        return False
    ct: int = 0
    # If list lenth is zero, it is a null list, so return a False
    if len(list_1) == 0:
        return False
    # Only need to check matching indices in two lists, so if they aren't identical there we can quit function early and return a False
    while ct < len(list_1):
        if list_1[ct] != list_2[ct]:
            return False
        ct += 1
    return True


def main() -> None:
    """Checking functionality of functions."""
    # Check functionality of 'all' function
    print(all([1, 2, 3], 1))
    print(all([1, 1, 1], 1))
    print(all([], 1))

    # Check functionality of 'max' function
    print(max([1, 2, 3, 4]))
    print(max([4, 3, 2, 1]))
    print(max([1, 5, 3, 4]))
    print(max([-1, -2, -3, -4]))
    print(max([]))

    # Check functionality of 'is_equal' function
    print(is_equal([1, 2, 3], [1, 2, 3]))
    print(is_equal([3, 2, 1], [1, 2, 3]))
    print(is_equal([1, 2, 3, 4], [1, 2, 3]))
    print(is_equal([], []))


if __name__ == "__main__":
    main()
