import numpy as np

matrix_1 = []
matrix_2 = []
matrix_3 = []
m_1 = 0
n_1 = 0
m_2 = 0
n_2 = 0

matrix_compatible = False

# Checking if matrix are compatible
while(matrix_compatible == False):

    # Checking correct rows input in first matrix
    while(1):
        try:
            m_1 = int(input("Rows in first matrix: "))
            if (m_1 <= 0):
                print("Try another value of rows in first matrix: ")
                continue
        except(ValueError):
            print("Try another value of rows in first matrix: ")
            continue
        else:
            break

    # Checking correct columns input in first matrix
    while(1):
        try:
            n_1 = int(input("Column in first matrix: "))
            if (n_1 <= 0):
                print("Try another value of columns in first matrix: ")
                continue
        except(ValueError):
            print("Try another value of columns in first matrix: ")
            continue
        else:
            break

    # Checking correct rows input in second matrix
    while(1):
        try:
            m_2 = int(input("Rows in second matrix: "))
            if (m_2 <= 0):
                print("Try another value of rows in second matrix: ")
                continue
        except(ValueError):
            print("Try another value of rows in second matrix: ")
            continue
        else:
            break

    # Checking correct columns input in second matrix
    while(1):
        try:
            n_2 = int(input("Column in second matrix: "))
            if (n_2 <= 0):
                print("Try another value of columns in second matrix: ")
                continue
        except(ValueError):
            print("Try another value of columns in second matrix: ")
            continue
        else:
            break

    if(n_1 == m_2):
        print("\nMatrix are compatible \n ")
        matrix_compatible = True
    else:
        print("\nMatrix are not compatible. Try another values \n")


def matrix_multiplication(m_1, n_1, m_2, n_2):
    # Taking first matrix from user input
    print("Enter first matrix")
    for i in range(m_1):
        a = []
        for j in range(n_1):
            # Taking element in row
            a.append(int(input()))
        # Taking row at all
        matrix_1.append(a)

    # Taking first matrix from user input
    print("Enter second matrix")
    for i in range(m_2):
        a = []
        for j in range(n_2):
            # Taking element in row
            a.append(int(input()))
        # Taking row at all
        matrix_2.append(a)

    # Printing 2 matrix
    for i in range(m_1):
        for j in range(n_1):
            print(matrix_1[i][j], end=" ")
        print()

    print()

    for i in range(m_2):
        for j in range(n_2):
            print(matrix_2[i][j], end=" ")
        print()

    # Print multiply of the matrix
    print("The multiply of the matrix is : ")
    matrix_3 = np.dot(matrix_1, matrix_2)

    for i in range(m_1):
        for j in range(n_2):
            print(matrix_3[i][j], end=" ")
        print()


matrix_multiplication(m_1, n_1, m_2, n_2)

print("\n")
print(123)