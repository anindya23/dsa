class MergeSort:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        leftArr = self.merge_sort(left)
        rightArr = self.merge_sort(right)

        return self.merge(leftArr, rightArr)

    def merge(self, leftArr, rightArr):
        result = []
        i = j = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] <= rightArr[j]:
                result.append(leftArr[i])
                i += 1
            else:
                result.append(rightArr[j])
                j += 1

        while i < len(leftArr):
            result.append(leftArr[i])
            i += 1

        while j < len(rightArr):
            result.append(rightArr[j])
            j += 1

        return result
