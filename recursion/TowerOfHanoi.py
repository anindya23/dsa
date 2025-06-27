class Solution:
    def tower(self, n, A, B, C):
        if n == 0: return
        self.tower(n-1, A, C, B)
        print(A, "->", B)
        self.tower(n-1, C, B, A)


if __name__ == '__main__':
    obj = Solution()
    print(obj.tower(3, "A", "B", "C"))