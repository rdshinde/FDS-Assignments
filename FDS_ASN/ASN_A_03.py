from numpy import matrix

#1. Function for addition of two matrices.
def matrix_add(m1,m2):
    return matrix(m1) + matrix(m2)

#2. Function for substraction of two matrices.
def matrix_sub(m1,m2):
    return matrix(m1) - matrix(m2)

#3. Function for multiplication of two matrices.
def matrix_multiplication(m1,m2):
    return matrix(m1) * matrix(m2)

#4. Function to find transpose of matrix.
def matrx_transpose(m):
    sample = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return matrix(sample)



print('Addition Of Matrices is: \n',matrix_add([
    [1,2,3],
    [4,5,6],
    [7,8,9]
],[
    [1,0,3],
    [2,8,0],
    [4,6,1]
]))
print('Substraction Of Matrices is: \n',matrix_sub([
    [1,2,3],
    [4,5,6],
    [7,8,9]
],[
    [1,0,3],
    [2,8,0],
    [4,6,1]
]))
print('Multiplication Of Matrices is: \n',matrix_multiplication([
    [1,2,3],
    [4,5,6],
    [7,8,9]
],[
    [1,0,3],
    [2,8,0],
    [4,6,1]
]))
print('Transpose Of Matrix is: \n',matrx_transpose([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))
