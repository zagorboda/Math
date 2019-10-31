import matplotlib.pyplot as plt
import numpy as np

# t = np.arange(0., 5., 0.2)
# plt.plot(t, "D", t**2, 'bs', t**3, 'g^', t + 4*t/3, 'X')
# plt.show()

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()



# names = ['group_a', 'group_b', 'group_c']
# values = [10, 33, 100]
#
# plt.figure(figsize=(9, 3), num="Testing figure")
# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()

x = np.linspace(0, 2, 20)
plt.figure(num="Testing figure")
plt.plot(x, x, "D", label='linear')
plt.plot(x, x**2, "+", label='quadratic')
plt.plot(x, x**3, "g^", label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()
