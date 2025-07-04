class Solution:
    @staticmethod
    def palindrome(num):
        # Store the original number
        original = num
        reversed_num = 0
        # Reverse the number
        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num //= 10
        # Check if the reversed number is equal to the original
        return original == reversed_num

# Take user input
num = int(input("Enter a number: "))
# Print if the number is a palindrome
if Solution.palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")


