import numpy as np

# #1
def f_to_c(f):
    return (f-32)*5/9

f=[32, 68, 100, 212, 77]
far_to_cel=np.vectorize(f_to_c)
print(far_to_cel(f))

# #2

def pow(a,b):
    return a**b

power=np.vectorize(pow)

bases=[2, 3, 4, 5]

powers=[1, 2, 3, 4]

print(power(bases,powers))

# #3

matrix=np.matrix(
    [
        [4,5,6],
        [3,-1,1],
        [2,1,-2]
    ]
)

vector=np.array([[7],[4],[5]])

solutions=np.linalg.solve(matrix,vector)

print("x:",solutions[0][0],"y:",solutions[1][0],"z:",solutions[2][0])

#4

matrix=np.matrix(
    [
        [10,-2,3],
        [-2,8,-1],
        [3,-1,6]
    ]
)

vector=np.array([[12],[-5],[15]])

solutions=np.linalg.solve(matrix,vector)

print("I1:",solutions[0][0],"I2:",solutions[1][0],"I3:",solutions[2][0])
