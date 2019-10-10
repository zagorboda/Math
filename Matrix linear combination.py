print("Linear combination is matrix C = A*c + B*d")

matrix_1 = []
matrix_2 = []
m = 0
n = 0
c = 0
d = 0

# Checking correct rows input
while(1):
    try:
        m = int(input("Rows: "))
        if (m <= 0):
            print("Try another value of rows: ")
            continue
    except(ValueError):
        print("Try another value of rows: ")
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

# Checking correct coefficients input
while(1):
    try:
        c = int(input("Coefficient c: "))
    except(ValueError):
        print("Try another value of c: ")
        continue
    else:
        break

while(1):
    try:
        d = int(input("Coefficient d: "))
    except(ValueError):
        print("Try another value of d: ")
        continue
    else:
        break


def linear_combination(n, m, c, d):
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
    print()

    # Printing 2 matrix multiplied by their coefficients
    print("A*c is : ")
    for i in range(m):
        for j in range(n):
            print(matrix_1[i][j] * c, end=" ")
        print()
    print()

    print("B*d is : ")
    for i in range(m):
        for j in range(n):
            print(matrix_2[i][j] * d, end=" ")
        print()
    print()

    print("Linear combination of A and B is : ")
    for i in range(m):
        for j in range(n):
            print(matrix_1[i][j] * c + matrix_2[i][j] * d, end=" ")
        print()
    print()


linear_combination(n, m, c, d)
