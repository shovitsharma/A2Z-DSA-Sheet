class Solution:
    @staticmethod
    def is_prime(num):
        # 0 and 1 are not prime numbers
        if num < 2:
            return False
        # Check for factors from 2 to sqrt(num)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

# Take user input
num = int(input("Enter a number: "))
# Print if the number is prime
if Solution.is_prime(num):
    print("Prime")
else:
    print("Not Prime")
