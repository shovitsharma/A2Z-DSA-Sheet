class Solution:
    @staticmethod
    def char_map_hash(arr):
        frq_map = {}
        # Count frequency of each character using its ASCII value as key
        for ch in arr:
            key = ord(ch)
            if key in frq_map:
                frq_map[key] += 1
            else:
                frq_map[key] = 1
        return frq_map
    
# Take user input for the size of the array
n = int(input("Enter size of array: "))    
# Take user input for the characters and split into a list
arr = list(input("Enter characters separated by space: ").split())
# Check if the number of characters matches the specified size
if len(arr) != n:
    print(f"Error: You entered {len(arr)} characters, but expected {n}.")
    exit(1)
# Get the frequency map
frq_map = Solution.char_map_hash(arr)
# Take user input for the number of queries
q = int(input("How many queries you want to know: "))
for i in range(q):
    ch = input(f"char[{i}]: ")
    # Print the frequency of the queried character
    print(frq_map.get(ord(ch), 0))