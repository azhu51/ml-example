import numpy as np

x = np.array([1, 2])
y = np.array([10, 20])
x_mat = np.mat([[1, 2], [3, 4]])
y_mat = np.mat([10, 20])

# inner product or scalar product or dot product
print("Array inner product:")
print(np.inner(x, y))
print("Matrix inner product:")
print(np.inner(x_mat, y_mat))

''' 
Array inner product:
50
Matrix inner product:
[[ 50]
 [110]]
'''

# outer product
print("Array outer product:")
print(np.outer(x,y))
print("Matrix outer product:")
print(np.outer(x_mat, y_mat))

'''
Array outer product:
[[10 20]
 [20 40]]
Matrix outer product:
[[10 20]
 [20 40]
 [30 60]
 [40 80]]
'''

x = np.array([1, 2])
y = np.array([10, 20])
x_mat = np.mat([[1, 2], [3, 4]])
y_mat = np.mat([[10, 20],[10,20]])

#element-wise product / point-wise product / Hadamard product
print("Array element-wise product:")
print(x * y)
print("Matrix element-wise product:")
print(x_mat * y_mat)

'''
Array element-wise product:
[10 40]
Matrix element-wise product:
[[ 30  60]
 [ 70 140]]
'''