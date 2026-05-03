import sys;

from runner.solution import I, O

sys.path.append("..")
from dataclasses import dataclass
from typing import List
from runner import Solution, TestCase

@dataclass
class Input:
    nums: List[int]

class MySolution(Solution[Input, List[int]]):

    def solve(self, input: I) -> O:
        nums: List[int] = input.nums
        i: int = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        i += 1
        return input

    def test_cases(self) -> List[TestCase[I, O]]:
        return [
            TestCase.of(Input([1,2,2]), [1,2,2], name="example 1"),
            TestCase.of(Input([0, 1,1 ,2,2,3,3,4,4]), [0, 1, 2, 3, 4], name="example 2")
        ]

