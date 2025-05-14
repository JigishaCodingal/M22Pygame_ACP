import numpy as np
a1=np.array([9,1,0,4,1,2,4,5,7,9,0,9])
#datatype
print("datatype of array",a1.dtype)
#shape
print("shape of array",a1.shape)
#Reshape
a2=a1.reshape(4,3)
print("Reshaping of array",a2)
#iteration
print("Display all elements of array : ")
for i in a1:
    print(i)
#Joining two arrays
a3=np.arange(2,15,4)#2,6,10,14
a4=np.concatenate((a1,a3))
print("Joining two arrays :",a4)
#searching
n=int(input("Enter element to be searched : "))
print(np.where(a4==n))
#sorting
print(np.sort(a4)[::-1])


