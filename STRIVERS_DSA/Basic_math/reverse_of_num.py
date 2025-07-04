class Solution:
    @staticmethod
    def reverse_number(num):
        # Initialize reversed number to 0
        reversed_num = 0
        # Reverse the digits of the number
        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num //= 10
        return reversed_num

# Take user input
num = int(input("Enter a number: "))
# Print the reversed number
print("Reversed number:", Solution.reverse_number(num))