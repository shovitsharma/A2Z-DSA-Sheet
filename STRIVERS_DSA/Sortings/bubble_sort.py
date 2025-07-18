# Bubble Sort implementation
class Solution:
    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n-i-1):
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

arr = list(map(int, input("Enter numbers separated by space: ").split()))
Solution.bubble_sort(arr)
print("Sorted array:", arr)

