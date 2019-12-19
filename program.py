#programs on linear algebraic functions
import numpy as np
from scipy import linalg
a=np.matrix([[1,2,],[3,4,]])
l=np.matrix([[11,12],[13,14]])
b=np.linalg.det(a)
#determinant of a matrix
print ("\nDeterminant of a=",b)
#inverse of a matrix
c=np.linalg.inv(a)
print ("\ninverse of a=\n",c)
#trace of a matrix
d=np.trace(a)
print ("\ntrace of a=",d)
#rank of a matrix
e=np.linalg.matrix_rank(a)
print ("\nrank of a=",e)
#dot product of two matrices
f=np.dot(a,l)
print ("\ndot product of two matrices=\n",f)
#eigen values of a matrix
g= np.linalg.eig(a)
print("\neigen value oa a=\n",g)
#addition of two matrices
h=np.add(a,l)
print("\naddition of two matrices=\n",h)
#subraction of two matrices
i=np.subtract(a,l)
print("\nsubtraction  of two matrices=\n",i)
#multiplication of two matrices
j=np.multiply(a,l)
print("\nmultiplication of two matrices=\n",j)
#division of two matrices
k=np.divide(a,l)
print("\ndivision  of two matrices=\n",k)
#transpose of a matrix
m=np.transpose(a)
print("\ntranspose of a matrix=\n",m)














