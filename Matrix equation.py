import numpy as np

a = []
b = []
x = []

print("Entering matrix of coefficients.")
while(1):
    try:
        m_1 = int(input("Enter number of rows: "))
        if (m_1 <= 0):
            print("Your value is less then zero. Try another one: ")
            continue
    except(ValueError):
        print("Your input isn't integer. Try another one: ")
    else:
        break
while(1):
    try:
        n_1 = int(input("Enter number of columns: "))
        if (n_1 <= 0):
            print("Your value is less then zero. Try another one: ")
            continue
    except(ValueError):
        print("Your input isn't integer. Try another one: ")
    else:
        break

for i in range(m_1):
    for j in range(n_1):
        while(1):
            try:
                print("Enter element: ")
                a_1 = float(input())
            except(ValueError):
                print("Your input isn't number. Try another one")
            else:
                a.append(a_1)
                break

a = np.array(a)
a = np.reshape(a, (m_1, n_1))

print("Entering matrix of values.")

for i in range(m_1):
    while (1):
        try:
            print("Enter element: ")
            b_1 = float(input())
        except(ValueError):
            print("Your input isn't number. Try another one")
        else:
            b.append(b_1)
            break

b = np.array(b)
print(a)
print(np.reshape(b, (m_1, 1)))
x = np.linalg.solve(a, b)
print("The answer is : \n", x)
# print(np.allclose(np.dot(a,x), b))
