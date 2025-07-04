class Solution:
    @staticmethod
    def high_low_freqmap(arr):
        frq_map = {}
        # Count frequency of each number
        for num in arr:
            if num in frq_map:
                frq_map[num] += 1
            else:
                frq_map[num] = 1
        return frq_map

# Take user input for the size of the array
n = int(input("Enter size of array: "))    
arr = list(map(int, input("Enter numbers separated by space: ").split()))
if len(arr) != n:
    print(f"Error: You entered {len(arr)} numbers, but expected {n}.")
    exit(1)

# Get the frequency map
freq_map = Solution.high_low_freqmap(arr)

# Find highest and lowest frequency without using min/max
highest = None
lowest = None
for freq in freq_map.values():
    if highest is None or freq > highest:
        highest = freq
    if lowest is None or freq < lowest:
        lowest = freq

# Print the highest and lowest frequencies
print("Highest frequency:", highest)
print("Lowest frequency:", lowest)