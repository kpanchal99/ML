import numpy as np
np.__version__
# declare one varaible to strore ndarray
arr = np.array([1,2,3,4,5,6])
#type(arr)

# convert list to array
a = ["MCA",33,9.99]
ar = np.array(a)
print(type(a) , type(ar))

# convert to tuple
t = ("karan",24,99)
tar = np.array(t)
print(type(t) , type(tar))

# assignment

#create a var T1 and assign tuple to it
t1 = ("KJSIM","Somaiya","Management")
#create array from tuple
t1arr = np.array(t1)
#check the type
print(type(t1) , type(t1arr))

# Dimension in array
arr = np.array([[1,2,3],[4,5,6]])
print(type(arr))

# arr.shape = > (axis 0 )row , (axis 1 )column
arr.shape

arr = np.array([[[1,3,4],[4,5,6]] , [[2,3,4],[4,6,9]]])
print(arr)

# accessing array
arr = np.array((1,2,3,4,5))
print(arr[0], arr[2] )
print("Sum of two index is : ",arr[1] + arr[4] )

# access the elements -> row (dimensions) column(index)
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# access the first row and second column
print(arr[0,1])
# access the second row and fifth column
print(arr[1,4])

arr = np.array([[[1,3,4],[4,5,6]] , [[2,3,4],[4,6,9]]])
print(arr[0,1,2])

print("--------------")
# accessing the second element of the first array of the second array
print(arr[1,0,1])
# accessing the second element of the second array of the second array
print(arr[1,1,1])



