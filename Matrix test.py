matrix_1 = []
matrix_2 = []

m = int(input("Rows: "))
n = int(input("Column: "))

print("Enter first matrix")
for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix_1.append(a)
a = []

print("Enter second matrix")
for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix_2.append(a)

for i in range(m):
    for j in range(n):
        print(matrix_1[i][j], end=" ")
    print()

print()

for i in range(m):
    for j in range(n):
        print(matrix_2[i][j], end=" ")
    print()

print("The sum of the matrix is : ")
for i in range(m):
    for j in range(n):
        print(matrix_1[i][j] + matrix_2[i][j], end=" ")
    print()
