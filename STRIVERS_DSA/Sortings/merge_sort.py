# Merge Sort implementation
class Solution:
    @staticmethod
    def merge_sort(arr):
        # Base case: if array has 1 or 0 elements, it's already sorted
        if len(arr) <= 1:
            return arr
        # Find the middle index
        mid = len(arr) // 2
        # Recursively sort the left and right halves
        left_half = Solution.merge_sort(arr[:mid])
        right_half = Solution.merge_sort(arr[mid:])
        # Merge the sorted halves
        return Solution.merge(left_half, right_half)

    @staticmethod
    def merge(left, right):
        merged = []
        i = j = 0
        # Merge the two sorted lists
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # Add any remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

arr = list(map(int, input("Enter the digits with a space in between: ").split()))
sorted_arr = Solution.merge_sort(arr)
print("Sorted array:", sorted_arr)