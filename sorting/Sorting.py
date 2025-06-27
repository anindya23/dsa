from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stack = []
        for n in nums:
            node = TreeNode(n)
            while stack and stack[-1].val < n:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

