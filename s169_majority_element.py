import sys;

from runner.solution import I, O

sys.path.append("..")
from dataclasses import dataclass
from typing import List
from runner import Solution, TestCase

@dataclass
class Input:
    nums: List[int]

class MySolution(Solution[Input, int]):

    def solve(self, input: I) -> O:
        nums := List[int] = input.nums
        n = len(nums)
        index = n // 2

        mapper := dict[int, int] = {}
        for num in nums:
            mapper[num] = mapper.get(num, 0) + 1

        for key, value in mapper.items():
            if value > index:
                return value

        return 0

    def test_cases(self) -> List[TestCase[I, O]]:
        return [
            TestCase.of(Input([3,2,3]), 3, name="example 1"),
            TestCase.of(Input([2,2,1,1,1,2,2]), 2, name="example 2")
        ]