import sys; sys.path.append("..")
from dataclasses import dataclass
from typing import List
from runner import Solution, TestCase

@dataclass
class MyInput:
    nums: List[int]
    target: int

class MySolution(Solution[MyInput, int]):

    def solve(self, input: MyInput) -> int:
        pass

    def test_cases(self):
        return [
            TestCase.of(MyInput([1,2,3], 6), 2, name="case 1"),
        ]

    # tuỳ chọn — override nếu output là list/float
    def assert_equal(self, expected, actual) -> bool:
        return expected == actual

if __name__ == "__main__":
    sol = MySolution()
    sol.run()
    sol.benchmark(warmup=100, iterations=1000)