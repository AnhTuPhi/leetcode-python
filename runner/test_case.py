from dataclasses import dataclass
from typing import Optional, TypeVar, Generic

I = TypeVar("I")
O = TypeVar("O")

@dataclass()
class TestCase(Generic[I, O]):
    input: I
    expected: O
    name: str = ""

    @staticmethod
    def of(input: I, expected: O, name: str = "") -> "TestCase[I, O]":
        return TestCase(input=input, expected=expected, name=name)