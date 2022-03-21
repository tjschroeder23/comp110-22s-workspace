"""A set of utility functions."""

__author__ = "tjschroeder23"


def evens_only(first_list: list[int]) -> list[int]:
    ret_list: list[int] = list()
    for i in first_list:
        if i % 2 == 0:
            ret_list.append(i)
    return ret_list


def only_evens(first_list: list[int]) -> list:
    ret_list: list[int] = list()
    i: int = 0
    while i < len(first_list):
        if first_list[i] % 2 == 0:
            ret_list.append(first_list[i])
        i += 1
    return ret_list


def sub(first_list: list[int], start_index: int, end_index: int) -> list:
    ret_list: list[int] = list()
    if start_index <= 0:
        start_index = 0
    if end_index >= len(first_list):
        end_index = len(first_list)
    # i: int = 0
    # while i < len(first_list):
    #     if i >= start_index and i < end_index:
    #         ret_list.append(first_list[i])
    #     i += 1
    i: int = start_index
    while i < end_index:
        ret_list.append(first_list[i])
        i += 1
    return ret_list


def concat(first_list: list[int], second_list: list[int]) -> list:
    ret_list: list[int] = list()
    i: int = 0
    while i < len(first_list):
        ret_list.append(first_list[i])
        i += 1
    i: int = 0
    while i < len(second_list):
        ret_list.append(second_list[i])
        i += 1
    return ret_list
