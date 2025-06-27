class Recursion:
    def sumN(self, n):
        if n <= 0:
            # print("Please give some numbers")
            return
        if n == 1:
            return 1
        return n + self.sumN(n-1)

    def factorial(self, n):
        if n < 0:
            print("No factorial for negative integers")
            return
        if n <=1:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self, idx):
        if idx <= 0:
            return 0
        if idx == 1:
            return 1
        return self.fibonacci(idx - 1) + self.fibonacci(idx - 2)

    def allEvens(self, n):
        print(n)
        if n % 2 != 0:
            return -1
        if n == 2:
            return n
        return self.allEvens(n-2)

    def towerOfHanoi(self):
        return 0

