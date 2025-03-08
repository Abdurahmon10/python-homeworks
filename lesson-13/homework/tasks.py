import numpy as np
import random

#1

vector=np.array([i for i in range(10,50)])

print(vector)


#2

matrix=np.array([[i+j for i in range(0,3)] for j in range(0,8,3)])

print(matrix)

#3

identity_matrix=np.matrix([[1 if(i==j) else 0 for i in range(0,3)] for j in range(0,3)])

print(identity_matrix)

#4

threed_matrix=np.array([[[random.randint(0,100) for i in range(0,3)] for j in range(0,3)] for k in range(0,3)])

print(threed_matrix)


#5

big_matrix=np.matrix([[random.randint(0,100) for i in range(10)] for k in range(10)])

max_matrix=big_matrix.max()

min_matrix=big_matrix.min()

print(max_matrix,min_matrix)



#6

rand_vector=np.array([random.randint(0,100)for i in range(30)])

print(rand_vector.mean())


#7
random_matrix=np.random.randint(0,11,size=(5,5))

print(random_matrix)

random_matrix_min=random_matrix.min()

random_matrix_max=random_matrix.max()

norm_rand_matrix_row=np.linalg.norm(random_matrix,axis=1)

norm_rand_matrix_column=np.linalg.norm(random_matrix,axis=0)

print(norm_rand_matrix_row)

print(norm_rand_matrix_column)


#8

rand_matrix_1=np.matrix([[random.randint(0,100) for i in range(3)]for j in range(5)])
rand_matrix_2=np.matrix([[random.randint(0,100) for i in range(2)]for j in range(3)])
product_matrix=rand_matrix_1 @ rand_matrix_2
print(product_matrix)

 #9

rand_matrix_1=np.matrix([[random.randint(0,100) for i in range(3)]for j in range(3)])
rand_matrix_2=np.matrix([[random.randint(0,100) for i in range(3)]for j in range(3)])

dot_product=np.dot(rand_matrix_1,rand_matrix_2)

print(dot_product)

 #10


rand_matrix_1=np.matrix([[int(input()) for i in range(4)]for j in range(4)])

rand_matrix_1_transposed=np.transpose(rand_matrix_1)

print(rand_matrix_1_transposed,"\n",rand_matrix_1)


 #11


rand_matrix_1=np.matrix([[random.randint(0,10) for i in range(3)]for j in range(3)])
rand_matrix_1_determinant=np.linalg.det(rand_matrix_1)

print(rand_matrix_1_determinant)



 #12

rand_matrix_1=np.matrix([[random.randint(0,100) for i in range(4)]for j in range(3)])
rand_matrix_2=np.matrix([[random.randint(0,100) for i in range(3)]for j in range(4)])
product_matrix=np.dot(rand_matrix_1,rand_matrix_2)
print(product_matrix)


 #13

rand_matrix=np.matrix([[random.randint(0,10) for i in range(3)] for j in range(3)])
rand_vector=np.array([[random.randint(0,10)] for i in range(3)])

vec_matrix_product=rand_matrix @ rand_vector

print(vec_matrix_product)



 #14
rand_matrix=np.matrix([[random.randint(0,10) for i in range(3)] for j in range(3)])
rand_vector=np.array([[random.randint(0,10)] for i in range(3)])

print(rand_matrix)
print(rand_vector)

solutions=np.linalg.solve(rand_matrix,rand_vector)
print(solutions)
print("verification:\n",rand_matrix @ solutions)


#15

rand_matrix=np.matrix([[int(input()) for i in range(5)] for j in range(5)])

print(rand_matrix)

row_sums=[int(np.sum(rand_matrix[i])) for i in range(0,5)]

rand_matrix_transpose=np.transpose(rand_matrix)

column_sums=[int(np.sum(rand_matrix_transpose[i])) for i in range(0,5)]

print(row_sums)
print(column_sums)