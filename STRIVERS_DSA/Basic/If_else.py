class Solution:
    @staticmethod
    def printGrade(s):
        # Check the score and print the corresponding grade
        if s >= 90:
            print("your grade is 'A'!")
        elif s >= 80:
            print("your grade is 'B'!")
        elif s >= 70:
            print("your grade is 'c'!")  # Note: 'c' should be 'C' for consistency
        elif s >= 60:
            print("your grade is 'D'!")
        elif s >= 50:
            print("your grade is 'E'!")
        else:
            print("your grade is 'F'!")
        
# Take user input for the score
score = int(input("Enter your score:"))
# Call the function to print the grade
Solution.printGrade(score)

"""
class solution:
    def printGrade(s):
        # Assign grade based on score
        if s >= 90:
            grade = 'A'
        elif s >= 80:
            grade = 'B'
        elif s >= 70:
            grade = 'C'
        elif s >= 60:
            grade = 'D'
        elif s >= 50:
            grade = 'E'
        else:
            grade = 'F'
        
        print(grade)
        return grade

# Take user input and print grade
score = int(input().strip())
Solution.printGrade(score)
"""