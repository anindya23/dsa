from typing import List

class TwoSum:
    def isTwoSum(self, nums: List[int], target) -> List[int]:
        hashMap = {}

        for num in nums:
            diff = target - num

            # if diff in