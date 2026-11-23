#CramersRule.py

"""
This program will use a function called det3 that will recieve a 3x3 array
and find the deterimate of the array. While giving the solution of three
linear equations in three variables.
"""


def det3(matrix):
    detA = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])) - (matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])) + (matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] *  matrix[2][0]))
    return detA
    
print("This program uses Cramer's Rule to solve a linear system.\nEnter each of 3 linear equations as four integers separated by spaces.\nFor example, x - 2y + 3z = 4 should be entered as 1 -2 3 4.\n")




row00, row01, row02, row03 = input("Enter equation 1: ").split()     #.split = put space between inputs
row10, row11, row12, row13 = input("Enter equation 2: ").split()
row20, row21, row22, row23 = input("Enter equation 3: ").split()     
     



row00 = float(row00)
row01 = float(row01)
row02 = float(row02)
row03 = float(row03)
row10 = float(row10)
row11 = float(row11)
row12 = float(row12)
row13 = float(row13)
row20 = float(row20)
row21 = float(row21)
row22 = float(row22)
row23 = float(row23)

matrix1 = [[row00, row01, row02, row03],              #2d list
           [row10, row11, row12, row13],
           [row20, row21, row22, row23]]

determinate_A = det3(matrix1)

variable1_matrix = [[matrix1[0][3], matrix1[0][1], matrix1[0][2]],
                    [matrix1[1][3], matrix1[1][1], matrix1[1][2]],
                    [matrix1[2][3], matrix1[2][1], matrix1[2][2]]]

variable2_matrix = [[matrix1[0][0], matrix1[0][3], matrix1[0][2]],
                    [matrix1[1][0], matrix1[1][3], matrix1[1][2]],
                    [matrix1[2][0], matrix1[2][3], matrix1[2][2]]]

variable3_matrix = [[matrix1[0][0], matrix1[0][1], matrix1[0][3]],
                    [matrix1[1][0], matrix1[1][1], matrix1[1][3]],
                    [matrix1[2][0], matrix1[2][1], matrix1[2][3]]]


if determinate_A == 0:
    print("\nThe system does not have a unique solution because the determinant is 0.")

if determinate_A != 0:
    
    variable1 = det3(variable1_matrix) / determinate_A
    variable2 = det3(variable2_matrix) / determinate_A
    variable3 = det3(variable3_matrix) / determinate_A
    print(f"\nThe system has a unique solution ({variable1}, {variable2} ,{variable3})")