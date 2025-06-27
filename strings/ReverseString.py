from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> str:
        l, r = 0, len(s) - 1

        while l<r:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1

        return s

    def reverseStrStack(self, s: List[str]) -> str:
        stck = []

        for item in s:
            stck.append(item)

        i = 0
        while stck:
            s[i] = stck.pop()
            i += 1
        return s

if __name__ == '__main__':
    obj = Solution()
    print(obj.reverseStrStack(['A', 'n', 'i', 'n', 'd', 'y', 'a']))