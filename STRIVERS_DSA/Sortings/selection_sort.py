# Selection Sort implementation
class Solution:
    @staticmethod
    def selection_sort(arr):
        n = len(arr)
        # Traverse through all array elements
        for i in range(n):
            min_idx = i
            # Find the minimum element in remaining unsorted array
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            # Swap the found minimum element with the first element
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = list(map(int, input("Enter numbers separated by space: ").split()))
Solution.selection_sort(arr)
print("Sorted array:", arr)