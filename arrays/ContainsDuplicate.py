from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for i in nums:
            if i in hash_set:
                return True
            hash_set.add(i)

        return False

if __name__ == '__main__':
    obj = Solution()
    print(obj.containsDuplicate([1, 2, 3, 1]))
    print(obj.containsDuplicate([1,2,3,4]))
    print(obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))