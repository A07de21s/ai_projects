import numpy as np

# 层次分析法确定各变量权重
A = np.array([[1,  5,  3,  3],\
              [1/5,1,1/3,  1/3],\
              [1/3,3,  1,  1],\
              [1/3,3,  1,  1]])
S = sum(A)
for i in range(0,len(A)):
    for j in range(0,len(A)):
        A[i,j] = A[i,j]/S[j]
feature_vector_A = list(map(sum,A))
weight_A = np.array(feature_vector_A)/len(A)

B1 = np.array([[1,  5,  7,  5,  7,  7],\
               [1/5,1,  3,  1,  3,  3],\
               [1/7,1/3,1, 1/3, 1, 1],\
               [1/5,1,  3,  1,  3,  3],\
               [1/7,1/3,1,1/3,  1,  1],
               [1/7,1/3,1,1/3,  1,  1]])
S1 = sum(B1)
for i in range(0,len(B1)):
    for j in range(0,len(B1)):
        B1[i,j] = B1[i,j]/S1[j]
feature_vector_B1 = list(map(sum,B1))
weight_B1 = np.array(feature_vector_B1)/len(B1)
weight_AB1 = weight_A[0]*weight_B1

B2 = np.array([[1,    5,  3,  9,  9,  7],\
               [1/5,  1,  3,1/5,1/5,1/3],\
               [1/3,1/3,  1,1/7,1/7,1/5],\
               [1/9,  5,  7,  1,  1,1/5],\
               [7,    3,  5,  5,  5,1/5],
               [7,    3,  5,  5,  5,  1]])
S2 = sum(B2)
for i in range(0,len(B2)):
    for j in range(0,len(B2)):
        B2[i,j] = B2[i,j]/S2[j]
feature_vector_B2 = list(map(sum,B2))
weight_B2 = np.array(feature_vector_B2)/len(B2)
weight_AB2 = weight_A[1]*weight_B2

B3 = np.array([[1, 1/3, 1/5,  1/3, 3,  5],\
               [3,  1,  1/3,  1,   5,  7],\
               [5,  3,  1,    3,   7,  9],\
               [3,  1,  1/3,  1,   5,  7],\
               [1/3,1/5,1/7,  1/5, 1,  3],\
               [1/5,1/7,1/9,  1/7, 1/3,1]])
S3 = sum(B3)
for i in range(0,len(B3)):
    for j in range(0,len(B3)):
        B3[i,j] = B3[i,j]/S3[j]
feature_vector_B3 = list(map(sum,B3))
weight_B3 = np.array(feature_vector_B3)/len(B3)
weight_AB3 = weight_A[2]*weight_B3

B4 = np.array([[1,  3,  3,  5,  5,  1/5],\
               [1/3,1,  1,  3,  3,  1/7],\
               [1/3,1,  1,  3,  3,  1/7],\
               [1/5,1/3,1/3,1,  1,  1/9],\
               [1/5,1/3,1/3,1,  1,  1/9],\
               [5,  7,  7,  9,  9,  1]])
S4 = sum(B4)
for i in range(0,len(B4)):
    for j in range(0,len(B4)):
        B4[i,j] = B4[i,j]/S4[j]
feature_vector_B4 = list(map(sum,B4))
weight_B4 = np.array(feature_vector_B4)/len(B4)
weight_AB4 = weight_A[3]*weight_B4

weight = weight_AB1 + weight_AB2 + weight_AB3 + weight_AB4
print(weight)
