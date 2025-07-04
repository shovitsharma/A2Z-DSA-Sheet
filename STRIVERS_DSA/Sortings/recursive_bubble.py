# Recursive Bubble Sort implementation
class Solution:
    @staticmethod
    def recursive_bubble(arr, n):
        # Base case: if only one element, return
        if n == 1:
            return
        # Perform one pass of bubble sort
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        # Recursive call for the rest of the array
        Solution.recursive_bubble(arr, n-1)

n = int(input("Enter the size of the array:"))
arr = list(map(int, input("Enter digits with space in betweeen:").split()))
if len(arr) != n:
    print("The elements in the array and the size of the array does not match with each other!!")
    exit()
Solution.recursive_bubble(arr, n)
print("The sorted array is ", arr)