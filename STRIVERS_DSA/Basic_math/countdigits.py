class Solution:
    @staticmethod
    def count_digits(num):
        # Initialize count to 0
        count = 0
        # Loop until num becomes 0
        while num > 0:
            num //= 10  # Remove the last digit
            count += 1  # Increment count
        return count

# Take user input
num = int(input("Enter a number: "))
# Print the number of digits
print("Number of digits:", Solution.count_digits(num))
