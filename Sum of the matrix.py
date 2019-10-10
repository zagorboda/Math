matrix_1 = []
matrix_2 = []
m = 0
n = 0
# Checking correct rows input
while(1):
    try:
        m = int(input("Rows: "))
        if (m <= 0):
            print("Try another value of rows:1 ")
            continue
    except(ValueError):
        print("Try another value of rows:2 ")
        continue
    else:
        break

# Checking correct columns input
while(1):
    try:
        n = int(input("Column: "))
        if (n <= 0):
            print("Try another value of columns: ")
            continue
    except(ValueError):
        print("Try another value of columns: ")
        continue
    else:
        break

def matrix_sum(n,m):
    # Taking first matrix from user input
    print("Enter first matrix")
    for i in range(m):
        a = []
        for j in range(n):
            # Taking element in row
            a.append(int(input()))
        # Taking row at all
        matrix_1.append(a)

    # Taking first matrix from user input
    print("Enter second matrix")
    for i in range(m):
        a = []
        for j in range(n):
            # Taking element in row
            a.append(int(input()))
        # Taking row at all
        matrix_2.append(a)

    # Printing 2 matrix
    for i in range(m):
        for j in range(n):
            print(matrix_1[i][j], end=" ")
        print()

    print()

    for i in range(m):
        for j in range(n):
            print(matrix_2[i][j], end=" ")
        print()

    # Print sum of the matrix
    print("The sum of the matrix is : ")
    for i in range(m):
        for j in range(n):
            print(matrix_1[i][j] + matrix_2[i][j], end=" ")
        print()


matrix_sum(n, m)
