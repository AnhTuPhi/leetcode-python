import sys; sys.path.append("..")
from dataclasses import dataclass
from typing import List
from runner import Solution, TestCase

@dataclass
class MyInput:
    nums1: List[int]
    m: int
    nums2: List[int]
    n: int

class MySolution(Solution[MyInput, List[int]]):

    def solve(self, input: MyInput) -> List[int]:
        nums1: List[int] = input.nums1
        m: int = input.m
        nums2: List[int] = input.nums2
        n: int = input.n

        i: int = m - 1
        j: int = n - 1
        k: int = len(nums1) - 1

        while i >= 0 and j >=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1

        while j>=0:
            nums1[k] = nums2[j]
            j-=1
            k-=1

        return nums1

    def test_cases(self):
        return [
            TestCase.of(MyInput([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6], name="example 1 - basic merge"),
            TestCase.of(MyInput([1], 0, [], 0), [1], name="example 2 - nums2 all smaller"),
            TestCase.of(MyInput([0], 0, [1], 1), [1], name="example 3 - nums1 empty"),
        ]


    # tuỳ chọn — override nếu output là list/float
    def assert_equal(self, expected, actual) -> bool:
        return expected == actual

if __name__ == "__main__":
    sol = MySolution()
    sol.run()
    # sol.benchmark(warmup=100, iterations=1000)