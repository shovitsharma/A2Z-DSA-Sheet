class Solution:
    @staticmethod
    def armstrong(num):
        # Convert the number to string to count digits
        digits = str(num)
        n = len(digits)  # Number of digits
        sum_of_powers = 0
        # Calculate the sum of each digit raised to the power of n
        for d in digits:
            sum_of_powers += int(d) ** n
        # Check if the sum equals the original number
        return sum_of_powers == num

# Take user input
num = int(input("Enter a number: "))
# Check and print if the number is an Armstrong number
if Solution.armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")