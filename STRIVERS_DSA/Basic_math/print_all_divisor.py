class Solution:
    @staticmethod
    def print_all_divisors(num):
        # Loop from 1 to num to find all divisors
        for i in range(1, num + 1):
            if num % i == 0:
                print(i, end=' ')
        print()  # Print newline after all divisors

# Take user input
num = int(input("Enter a number: "))
# Print all divisors of the number
Solution.print_all_divisors(num)
