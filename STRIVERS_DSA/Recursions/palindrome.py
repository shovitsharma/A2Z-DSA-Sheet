# Check if a number is a palindrome using recursion
class Solution:
    @staticmethod
    def palindrome(num):
        # Helper function to reverse the number
        def reverse(n, rev):
            if n == 0:
                return rev
            return reverse(n // 10, rev * 10 + n % 10)
        # Compare original number with its reverse
        return num == reverse(num, 0)

num = int(input("Enter a number: "))
if Solution.palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")