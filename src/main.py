"""
------------------------------------------------------------------------
[main file]
------------------------------------------------------------------------
Author: Moman Malik
Email:  momanziamalik@gmail.com    
__updated__ = "2020-05-14"
------------------------------------------------------------------------
"""
from functions import matrix_flatten,matrix_rotate_right,matrix_stats,matrixes_add,matrixes_multiply
import ast
def print_matrix(c):
    for i in range(len(c)):
        for j in range(len(c[i])):
            print("\t{:>2}".format(c[i][j]),end=" ")
        print()
c = [[1,2],[3,4],[5,6]]
print("Formatting Method")
print("Example: {}\n       =".format(c))
print_matrix(c)
print()
mode = input("Please enter one of the following: 'matrix_flatten', 'matrix_rotate_right', 'matrix_stats', 'matrixes_add', 'matrixes_multiply': ")
if mode == "matrix_flatten":
    matrix_str = input("Please enter a matrix as a 2D list: ")
    matrix = ast.literal_eval(matrix_str)
    print(matrix_flatten(matrix))
elif mode == "matrix_rotate_right":
    matrix_str = input("Please enter a matrix as a 2D list: ")
    matrix = ast.literal_eval(matrix_str)
    output = matrix_rotate_right(matrix)
    print("You entered: ")
    print_matrix(matrix)
    print("Output: ")
    print_matrix(output)
    print(output)
elif mode == "matrix_stats":
    matrix_str = input("Please enter a matrix as a 2D list: ")
    matrix = ast.literal_eval(matrix_str)
    small, large, total, average = matrix_stats(matrix)
    print("\nSmall: {}, Large: {}, Total: {}, Average: {:.2f}".format(small,large,total,average))

elif mode == "matrixes_add":
    print("Please enter two matrices as a 2D list: ")
    matrix1_str = input("Matrix 1: ")
    matrix2_str = input("Matrix 2: ")
    
    matrix1 = ast.literal_eval(matrix1_str)
    matrix2 = ast.literal_eval(matrix2_str)
    print("You entered: ")
    print_matrix(matrix1)
    print("And: ")
    print_matrix(matrix2)
    print('Output: ')
    output = matrixes_add(matrix1,matrix2)
    print_matrix(output)
    print(output)
elif mode == "matrixes_multiply":
    print("Please enter two matrices as a 2D list: ")
    matrix1_str = input("Matrix 1: ")
    matrix2_str = input("Matrix 2: ")
    
    matrix1 = ast.literal_eval(matrix1_str)
    matrix2 = ast.literal_eval(matrix2_str)
    print("\nYou entered: ")
    print_matrix(matrix1)
    print("And: ")
    print_matrix(matrix2)
    print('Output: ')
    output = matrixes_multiply(matrix1,matrix2)
    print_matrix(output)
    print(output)
    
