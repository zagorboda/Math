import numpy as np

a = []

# Checking correct shape input
while(1):
    try:
        m = int(input("Enter shape: "))
        if (m <= 0):
            print("Your value is less then zero. Try another one: ")
            continue
    except(ValueError):
        print("Your input isn't integer. Try another one: ")
    else:
        break

# Checking matrix input
for i in range(m * m):
    while(1):
        try:
            print("Enter ", i + 1," element: ")
            b = float(input())
        except(ValueError):
            print("Your input isn't number. Try another one")
        else:
            a.append(b)
            break
np.array(a)
a = np.reshape(a, (m, m))
print(a)
print("Determinant is : %.3f" % np.linalg.det(a))
