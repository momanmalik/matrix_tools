"""
------------------------------------------------------------------------
[functions]
------------------------------------------------------------------------
Author: Moman Malik
Email:  momanziamalik@gmail.com    
__updated__ = "2020-05-14"
------------------------------------------------------------------------
"""
#Imports
def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    total = 0
    small = a[0][0]
    large = a[0][0]
    count = 0 
    for i in range(len(a)):
        for j in range(len(a[i])):
            count += 1 
            total += a[i][j]
            if a[i][j] < small:
                small = a[i][j] 
            if a[i][j] > large:  
                large = a[i][j]
    average = total / count
    return small, large, total, average

def matrix_flatten(a):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list a. A 'flattened' list is a
    2D list that is converted into a 1D list.
    Use: b = matrix_flatten(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the flattened version of a (list of ?)
    -------------------------------------------------------
    """
    b = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            b.append(a[i][j])
    return b

def matrixes_add(a, b):
    """
    -------------------------------------------------------
    Sums the contents of matrixes a and b. a and b must have
    the same number of rows and columns.
    Use: c = matrixes_add(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix sum of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(a[i])):
            c[i].append(a[i][j]+b[i][j])
    return c
def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    assert len(a) == len(b[0]) and len(a[0]) == len(b)
    
    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(b[0])):
            current_sum = 0
            for x in range(len(a[i])):
                product = a[i][x] * b[x][j]
                current_sum += product
            c[i].append(current_sum)
    return c

def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    b = []
    for i in range(len(a[0])):
        b.append([])
        for j in range(len(a)-1,-1,-1):
            b[i].append(a[j][i])
    return b