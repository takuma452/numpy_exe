import numpy as np

#1
a = np.ones((1,5))
print(a)

#2
a[0,1] = 3.14
print(a)

#3
b = np.copy(a)
b = b.T
print(b)

#4
ab_dot = np.dot(a,b)
print(ab_dot)

#5
c = np.random.rand(1,10)
print(c)

#6
d = np.random.normal(10,2,(2,5))
print('#6')
print(d)

#7
print('#7')
print(d[:,1])

#8
print('#8')
print(d[:,2:4])

#9
e = np.random.rand(5,2)
print('#9')
print(np.dot(d,e))