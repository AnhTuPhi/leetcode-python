import sys;

from runner.solution import I, O

sys.path.append("..")
from dataclasses import dataclass
from typing import List
from runner import Solution, TestCase

@dataclass
class Input:
    nums: List[int]
    val: int

class MySolution(Solution[Input, List[int]]):

    def solve(self, input: I) -> O:
        nums: List[int] = input.nums
        val: int = input.val
        index: int = 0

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

    def test_cases(self) -> List[TestCase[I, O]]:
        return [
            TestCase.of(Input([3,2,2,3], 3), [2, 2], name="example 1"),
            TestCase.of(Input([0,1,2,2,3,0,4,2], 2), [0,1,4,0,3], name="example 2")
        ]

if __name__ == "__main__":
    solution = MySolution()
    solution.run()