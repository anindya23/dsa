from typing import List

class Solution:
    def rearrange(self, nums: List[int]) -> List[int]:
        rightMax = -1

        for i in range(len(nums) - 1, -1, -1):
            newMax = max(nums[i], rightMax)
            nums[i] = rightMax
            rightMax = newMax

        return nums

if __name__ == '__main__':
    obj = Solution()
    print(obj.rearrange([17, 18, 5, 4, 6, 1]))