"""JSS Dictionary."""


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Switches the keys and the values."""
    invert_dict: dict[str, str] = dict()
    for key in given_dict:
        invert_dict[given_dict[key]] = key
    if len(invert_dict) != len(given_dict):
        raise KeyError("You cannot input multiple of the same key.")
    return invert_dict


def favorite_color(person_fav_color: dict[str, str]) -> str:
    """Finding most common favorite color from dictionary."""
    temp_dict: dict[str, int] = dict()
    for person in person_fav_color:
        if person_fav_color[person] in temp_dict:
            temp_dict[person_fav_color[person]] += 1
        else:
            temp_dict[person_fav_color[person]] = 1
    fav_color_return: str = ""
    max_count: int = 0
    for fav_color in temp_dict:
        if temp_dict[fav_color] > max_count:
            fav_color_return = fav_color
            max_count = temp_dict[fav_color]
    return fav_color_return


def count(given_list: list[str]) -> dict[str, int]:
    """Counting frequency of values in a list."""
    return_dict: dict[str, int] = dict()
    idx: int = 0
    while idx < len(given_list):
        if given_list[idx] in return_dict:
            return_dict[given_list[idx]] += 1
        else:
            return_dict[given_list[idx]] = 1
        idx = idx + 1
    return return_dict


def alphabetizer(given_list: list[str]) -> dict[str, list[str]]:
    """Categorizing a list by first letter."""
    return_dict: dict[str, list[str]] = dict()
    for item in given_list:
        if item[0].lower() in return_dict:
            return_dict[item[0].lower()].append(item)
        else:
            return_dict[item[0].lower()] = []
            return_dict[item[0].lower()].append(item)
    return return_dict


def update_attendance(attend_report: dict[str, list[str]], wkday: str, student: str) -> dict[str, list[str]]:
    """Mutating weekly attendance report."""
    if wkday in attend_report:
        attend_report[wkday].append(student)
    else:
        attend_report[wkday] = []
        attend_report[wkday].append(student)
    return attend_report
