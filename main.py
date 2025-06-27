def searchMissing(arr, size):
    start = 0
    end = size - 1
    mid = 0
    while end > start + 1:
        mid = (start + end) // 2
        if (arr[start] - start) != (arr[mid] - mid):
            end = mid
        elif (arr[end] - end) != (arr[mid] - mid):
            start = mid
    return arr[start] + 1


# Driver Code
if __name__ == '__main__':
    a = [5, 6, 7, 8, 10]
    b = [-8, -6]
    c = [1, 2, 3, 4, 6, 7, 8]
    d = [1, 2, 3, 4, 5, 6, 8, 9]
    e = [2,3,5]
    print("Missing number:", searchMissing(a, len(a)))
    print("Missing number:", searchMissing(b, len(b)))
    print("Missing number:", searchMissing(c, len(c)))
    print("Missing number:", searchMissing(d, len(d)))
    print("Missing number:", searchMissing(e, len(e)))