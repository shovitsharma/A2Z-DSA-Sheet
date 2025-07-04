class Solution:
    @staticmethod
    def int_hashing(arr):
        # Find the maximum value in the array to size the hash array
        max_val = max(arr) if arr else 0
        hash_array = [0] * (max_val + 1)
        for num in arr:
            hash_array[num] += 1  # Increment the count for the number
        return hash_array

# Take user input for the size of the array
n = int(input("Enter size of array: "))
# Take user input for the numbers and convert to a list of integers
arr = list(map(int, input("Enter numbers separated by space: ").split()))

# Check if the number of elements matches the specified size
if len(arr) != n:
    print(f"Error: You entered {len(arr)} numbers, but expected {n}.")
    exit(1)

# Get the hash array using the static method
hash_array = Solution.int_hashing(arr)

# Take user input for the number of queries
q = int(input("How many queries you want to know: "))
for i in range(q):
    number = int(input(f"num[{i}]: "))
    # Print the frequency of the queried number, or 0 if out of range
    if 0 <= number < len(hash_array):
        print(hash_array[number])
    else:
        print(0)
