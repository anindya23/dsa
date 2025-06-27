memo = {}

def find_largest(a, low, high):
    # Handle base cases
    if high < low:
        return None
    if high == low:
        return a[low]

    mid = (low + high) // 2

    # Check if mid is the largest element
    if mid < high and a[mid] > a[mid+1]:
        return a[mid]
    if mid > low and a[mid-1] > a[mid]:
        return a[mid-1]

    # Recurse on the left or right side of mid based on which side is unsorted
    if a[high] > a[mid]:
        return find_largest(a, low, mid-1)
    else:
        return find_largest(a, mid+1, high)

def solve(self, i, j):
    if i>j or i>=n or j<0:
        return 0

    k = (i, j)
    if k in memo:
        return memo[k]

    option1 = arr[i] + min(solve(i+2, j), solve(i+1, j-1))
    option2 = arr[j] + min(solve(i+1, j-1), solve(i, j-2))

    memo[k] = max(option1, option2)
    return memo[k]

return solve(0, n-1)
        

if __name__ == "__main__":
    arr1 = [8, 15, 3, 7]
    arr2 = [5, 3, 7, 10]
    n = len(arr2)

