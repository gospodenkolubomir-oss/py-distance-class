from __future__ import annotations
from numbers import Number
from functools import total_ordering


@total_ordering
class Distance:

    def __init__(self, km: int) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError("km must be a number")
        self.km = km

    def __add__(self, other: int) -> Distance:
        if isinstance(other, Distance):
            value = self.km + other.km
        elif isinstance(other, Number):
            value = self.km + other
        else:
            return NotImplemented
        return Distance(value)

    def __mul__(self, other: int) -> Distance:
        if isinstance(other, Number):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other: int) -> Distance:
        return self.__mul__(other)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __truediv__(self, other: float) -> Distance:
        if not isinstance(other, Number):
            return NotImplemented
        elif other == 0:
            raise ZeroDivisionError
        return Distance(round(self.km / other, 2))

    def __iadd__(self, other: int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, Number):
            self.km += other
        else:
            return NotImplemented
        return self

    def __eq__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, Number):
            return self.km == other
        return NotImplemented

    def __lt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, Number):
            return self.km < other
        return NotImplemented
