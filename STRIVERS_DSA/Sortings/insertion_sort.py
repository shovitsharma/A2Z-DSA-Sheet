# Insertion Sort implementation
class Solution:
    @staticmethod
    def insertion_sort(arr):
        n = len(arr)
        # Traverse from 1 to n-1
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            # Move elements of arr[0..i-1], that are greater than key, to one position ahead
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

arr = list(map(int, input("Enter numbers separated by space: ").split()))
Solution.insertion_sort(arr)
print("Sorted array:", arr)