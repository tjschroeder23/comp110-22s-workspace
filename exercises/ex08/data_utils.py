"""Dictionary related utility functions."""

__author__ = "tjschroeder23"
# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    column: list[str]
    z: int = n
    for key in table:
        column = table[key]
        start_list: list[str] = []
        if n > len(table[key]):
            z = len(table[key])
        i: int = 0
        while i < z:
            start_list.append(column[i])
            i += 1
        # for i in range(n):
        #     # start_list.append(table[key][i])
        #     start_list.append(column[i])
        result[key] = start_list
    return result


def select(table: dict[str, list[str]], headers: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for key in headers:
        result[key] = table[key]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for key in table_1:
        result[key] = table_1[key]
    for key in table_2:
        if key in result:
            i: int = 0
            while i < len(table_2[key]):
                result[key].append(table_2[key][i])
                i += 1
            # result[key] += table_2[key]
        else:
            result[key] = table_2[key]
    return result


def count(a: list[str]) -> dict[str, int]:
    result: dict[str, int] = dict()
    for item in a:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def choice_order(a: list[str], b: dict[str, int]) -> dict[str, int]:
    result: dict[str, int] = dict()
    for item in a:
        result[item] = 0
    for key in b:
        result[key] = b[key]
    return result


def slice_count(a: list[str], b: list[str], c: list[str], d: list[str]) -> dict[str, dict[str, int]]:
    result: dict[str, dict[str, int]] = dict()
    tempdict: dict[str, list[str]] = dict()
    for slice in a:
        tempdict[slice] = []
        i: int = 0
        while i < len(c):
            if c[i] == slice:
                tempdict[slice].append(d[i])
            i += 1
        result[slice] = choice_order(b, count(tempdict[slice]))
    return result
