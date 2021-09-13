import numpy as np

x = np.array([[1, 2]]).reshape(2, 1)
y = np.array([[2, 1]])
z = np.matmul(x, y)

print(z)
print(x@y)

exit()