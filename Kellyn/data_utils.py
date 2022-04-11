"""Dictionary related utility functions."""

__author__ = "730308418"

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
    """Produces table with a certain number of rows of data from original."""
    result: dict[str, list[str]] = {}
    for key in table:
        starting_list: list[str] = []
        if n > len(table[key]):
            n = len(table[key])
        i: int = 0
        while i < n:
            starting_list.append(table[key][i])
            i += 1
        result[key] = starting_list
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Function selects certain columns, used to look at only certain parts of data."""
    result: dict[str, list[str]] = {}
    for item in names:
        result[item] = table[item]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combining two dictionaries together."""
    result: dict[str, list[str]] = {}
    for key in table_1:
        result[key] = table_1[key]
    for key in table_2:
        if key in result:
            i: int = 0
            while i < len(table_2[key]):
                result[key].append(table_2[key][i])
                i += 1
        else:
            result[key] = table_2[key]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times a piece of data appears in a list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def order_key(table: dict[str, int]) -> dict[str, int]:
    """Will order the keys of the dictionary to be in numerical order."""
    result: dict[str, int] = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0}
    for item in table:
        if item == "7":
            result["7"] = table["7"]
        elif item == "6":
            result["6"] = table["6"]
        elif item == "5":
            result["5"] = table["5"]
        elif item == "4":
            result["4"] = table["4"]
        elif item == "3":
            result["3"] = table["3"]
        elif item == "2":
            result["2"] = table["2"]
        elif item == "1":
            result["1"] = table["1"]

    return result


def order_social_media(table: dict[str, int]) -> dict[str, int]:
    """Will order the keys for the social media data."""
    result: dict[str, int] = {"None": 0, "0 to 2 hours": 0, "3 to 5 hours": 0, "5 to 10 hours": 0, "10+ hours": 0}
    for item in table:
        if item == "None":
            result["None"] = table["None"]
        elif item == "0 to 2 hours":
            result["0 to 2 hours"] = table["0 to 2 hours"]
        elif item == "3 to 5 hours":
            result["3 to 5 hours"] = table["3 to 5 hours"]
        elif item == "5 to 10 hours":
            result["5 to 10 hours"] = table["5 to 10 hours"]
        elif item == "10+ hours":
            result["10+ hours"] = table["10+ hours"]

    return result


def slice_count(key_list: list[str], b_list: list[str]) -> dict[int, dict[str, int]]:
    result: dict[int, dict[str, int]] = {}
    for index in key_list:

    return result
