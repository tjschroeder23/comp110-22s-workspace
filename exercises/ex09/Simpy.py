"""Utility class (Simpy) for numerical operations.

Utility class (StrArray) for string operations"""

from __future__ import annotations
from typing import Union

__author__ = "tjschroeder23"


class Simpy:
    values: list[float]
   
    def __init__(self, values: list[float]):
        """docstring."""
        self.values = values

    def __str__(self) -> str:
        """docstring."""
        return f"Simpy({self.values})"

    def fill(self, fl: float, cnt: int) -> None:
        self.values = []
        i: int = 0
        while i < cnt:
            self.values.append(fl)
            i += 1

    def arange(self, srt: float, stp: float, step: float = 1.0) -> None:
        assert step != 0.0
        self.values = []
        i: float = srt
        if step < 0.0:
            while i > stp:
                self.values.append(i)
                i += step
        else:
            while i < stp:
                self.values.append(i)
                i += step
              
    def sum(self) -> float:
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """docstring."""
        result: list[float] = []
        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """docstring."""
        result: list[float] = []
        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """docstring."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """docstring."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """docstring."""
        result_gi: Union[float, Simpy]
        if isinstance(rhs, int):
            result_gi = self.values[rhs]
            return result_gi
        else:
            result_list: list[float] = []
            assert len(self.values) == len(rhs)
            i: int = 0
            while i < len(self.values):
                if rhs[i]:
                    result_list.append(self.values[i])
                i += 1
            result_gi = Simpy(result_list)
            return result_gi

class StrArray:
    items: list[str]

    def __init__(self, items):
        """Docstring."""
        self.items = items

    def __repr__(self) -> str:
        """Docstring."""
        return f"StrArray ({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Add is a vectorized operation that applies to all items.

        When rhs is a str, it is concatenated to every item in a new StrArray.
        """
        if isinstance(rhs, str):
            result: list[str] = []
            for item in self.items:
                result.append(item + rhs)
            return StrArray(result)
        else:
            result: list[str] = []
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
            return StrArray(result)
