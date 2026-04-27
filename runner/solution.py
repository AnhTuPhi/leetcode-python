from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
from .test_case import TestCase
from . import leetcode_runner as _engine

I = TypeVar("I")
O = TypeVar("O")

class Solution(ABC, Generic[I, O]):

    @abstractmethod
    def solve(self, input: I) -> O:
        """Implement logic handle"""
        ...

    @abstractmethod
    def test_cases(self) -> List[TestCase[I, O]]:
        """Return a list of test cases"""
        ...

    def assert_equal(self, expected: O, actual: O) -> bool:
        return expected == actual

    def run(self) -> None:
        _engine.run(self)

    def benchmark(self, warmup: int = 100, iterations: int = 1000) -> None:
        _engine.benchmark(self, warmup, iterations)