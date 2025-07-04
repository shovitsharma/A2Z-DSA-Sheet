# Reverse an array using recursion
class solution:
    @staticmethod
    def reverse_of_array(arr, start, end):
        # Base case: if start index is greater than or equal to end, stop recursion
        if start >= end:
            return
        # Swap the elements at start and end
        arr[start], arr[end] = arr[end], arr[start]
        # Recursive call for the next pair
        solution.reverse_of_array(arr, start + 1, end - 1)

arr = list(map(int, input().split()))
solution.reverse_of_array(arr, 0, len(arr) - 1)
print(arr)