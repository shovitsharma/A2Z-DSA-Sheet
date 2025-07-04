# Recursive Insertion Sort implementation
class Solution:
    @staticmethod
    def recursive_insertion(arr, n):
        # Base case: if only one element, return the array
        if n <= 1:
            return arr
        # Recursively sort the first n-1 elements
        Solution.recursive_insertion(arr, n-1)
        # Insert the nth element at its correct position
        j = n - 1
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        return arr

n = int(input("Enter the size of the array:"))
arr = list(map(int, input("Enter digits with space in betweeen:").split()))
if len(arr) != n:
    print("The elements in the array and the size of the array does not match with each other!!")
    exit()
sorted_arr = Solution.recursive_insertion(arr, n)
print("The sorted array is ", sorted_arr)