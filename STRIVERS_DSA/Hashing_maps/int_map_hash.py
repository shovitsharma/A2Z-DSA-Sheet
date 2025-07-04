class Solution:
    @staticmethod
    def int_map_hash(arr):
        frq_map = {}
        # Count frequency of each number in the array
        for num in arr:
            if num in frq_map:
                frq_map[num] += 1  # Increment count if number already exists
            else:
                frq_map[num] = 1   # Initialize count if number is seen first time
        return frq_map

# Take user input for the size of the array
n = int(input("Enter size of array: "))    
# Take user input for the numbers and convert to a list of integers
arr = list(map(int, input("Enter numbers separated by space: ").split()))

# Check if the number of elements matches the specified size
if len(arr) != n:
    print(f"Error: You entered {len(arr)} numbers, but expected {n}.")
    exit(1)

# Get the frequency map using the static method
freq_map = Solution.int_map_hash(arr)

# Take user input for the number of queries
q = int(input("How many queries you want to know: "))
for i in range(q):
    number = int(input(f"num[{i}]: "))
    # Print the frequency of the queried number, or 0 if not present
    print(freq_map.get(number, 0))