import numpy as np

a = []

# Checking correct shape input
while(1):
    try:
        m = int(input("Enter number of rows: "))
        if (m <= 0):
            print("Your value is less then zero. Try another one: ")
            continue
    except(ValueError):
        print("Your input isn't integer. Try another one: ")
    else:
        break

while(1):
    try:
        n = int(input("Enter number of columns: "))
        if (n <= 0):
            print("Your value is less then zero. Try another one: ")
            continue
    except(ValueError):
        print("Your input isn't integer. Try another one: ")
    else:
        break

# Checking matrix input
for i in range(m):
    for j in range(n):
        while(1):
            try:
                print("Enter element: ")
                b = float(input())
            except(ValueError):
                print("Your input isn't number. Try another one")
            else:
                a.append(b)
                break
np.array(a)
a = np.reshape(a, (m, n))
print(a)
print("Matrix rank is :", np.linalg.matrix_rank(a))
