#numpy-numerical python library,provides more speed fewer loops,clearer code better quality.it is used for operastions on multi dimentional arrays
#used in filed of data science
import numpy as np
#
# digits=np.array([
#     [1,2,3],
#     [2,3,4],
#     [5,6,7]
# ])
# print(digits.shape)#size of array-3X3 Matrix
#
# odd_number_list=[1,3,5,7,9,11]
# ol_numpy=np.array(odd_number_list)
# print(ol_numpy)#1-D array
# print("shape of an array",ol_numpy.shape)
# col_vector=digits[np.newaxis,:]
# print(col_vector)
# row_vector=digits[:,np.newaxis]
# print(row_vector)
# col_vector=ol_numpy[np.newaxis,:]#-column wise converting
# print(col_vector)
# row_vector=ol_numpy[:,np.newaxis]#-row wise converting
# print(row_vector)
# CURVE_CENTER=80
# grades=np.array([72,35,64,88,90,74,12])
# def curve(grades):
#     average=grades.mean();
#     change=CURVE_CENTER-average
#     new_grades=change+grades
#     return np.clip(new_grades,grades,100)
# print("orginal grade",grades)
# print("curved grades",curve(grades))

#vectorisation is the process of performing the same opersation in the same way in each element of array-removes for loop

#Broadcasting-it is the process of extending 2 arrays of different shape and figuring out how to perform a vectorise calculation between them

# batting_averages=np.array([53.3,35.5,88.39,38.0,49.9,38.6,77.6,34.5,19.6,20.8,19.6,20.8]).reshape(2,6)#array ,column,row(if 2 givving c,rowol)
# print(batting_averages)
# print(batting_averages.max(),"max batting")
# print(batting_averages.max(axis=1),"max batting")#row wise if axis=1 column wise

# sample_array=np.zeros(10)
# print(sample_array.reshape(2,5))
# dummy_array=np.ones(10,dtype=int)
# print(dummy_array.reshape(5,2))
#
# dynamic_array_1=np.arange(10,100,5,dtype=int).reshape(3,6)#-default is float so chnage to int
# print(dynamic_array_1)
# dynamic_array_2=np.arange(10,100,5,dtype=int).reshape(3,6)#-default is float so chnage to int
# print(dynamic_array_2)
# print(dynamic_array_2+dynamic_array_1)
# print(dynamic_array_2*dynamic_array_1)
# print(dynamic_array_2-dynamic_array_1)


# squre =np.array([[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]])
# print(squre)
# for i in range(4):
#     print( squre[:,i].sum()==34)
#     print(squre[i,:].sum()==34)
# print(squre[:2,:2].sum())
# print(squre[2:,:2].sum())
#
# numbers = np.linspace(5,50,24,dtype=int).reshape(4,-1)
# print(numbers)
# mask=numbers%5==0
# print(mask)#mask to a property
#
# print(numbers[mask])#filtering of the numbers
# print(numbers.T)#taking transpose
# print("sorted",np.sort(numbers,axis=0))#sort
# print("sorted",np.sort(numbers,axis=1))#sort

# a=np.array([[4,8],[6,1]])
# b=np.array([[3,5],[7,2]])
#
# print(np.hstack((a,b)))#horizontal merging of 2 or more arrays concatenate-axis=1
# print(np.vstack((a,b)))#vertical merging of two or more arrays concatenate-axis=0
# print(np.concatenate((a,b)))#merging of 2 or more arrays
# print(np.concatenate((a,b),axis=0))`


 #*********************QUSTION 1******************************
# array=np.array([[1,2,3,4],
#                 [22,33,55,44],
#                 [33,11,88,22]
#                 ])
# a=array.max(axis=1)
# print("max",a)
#
#
# #***********************QUSTION 2******************
# array=np.array([[1,2,3,4],
#                 [22,33,55,44],
#                 [33,11,88,22]
#                 ])
# ar=array.min(axis=1)
# print("min",ar)
#
#
# #*******************Qustion 3**********
#
# array=np.array([[1,2,3,4],
#                 [22,33,55,44],
#                 [33,11,88,22]
#                 ])
# print(array.mean(axis=1,dtype=float))
#
# #*************Qustion 4**********
# array=np.array([[1,2,3,4],
#                 [22,33,55,44],
#                 [33,11,88,22]
#                 ])
#
# array2=np.array([[1,2,3,4],
#                 [22,33,55,44],
#                 [33,11,88,22]
#                 ])
# new=np.concatenate((array,array2),axis=0)
# print(new)
#
# #******************Qustion-5***********
#
# array=np.array([[1,2,3,4],
#                 [22,33,55,44],
#                 [33,11,88,22]
#                 ])
# new=np.flipud(array)
# print(new)
#
# #****************8Qustion -6**********
# array=np.array([[1,2,3,4],
#                 [22,33,55,44],
#                 [33,11,88,22]
#                 ])
# array2=np.array([[1,2,3,4],
#                 [22,33,55,44],
#                 [33,11,88,22]
#                 ])
# new=np.multiply(array,array2)
# print(new)
#
# #*************************Qustion-7**************
# array=np.ones([4,4],dtype=int)
# for i in range(0,5):
#     array[:i,:1]=0
#     array[:i,2:3]=0
# print(array)
# array[array%2==0]=0
# array[array%2==0]=0
# print(array)
# # array[:1,:1]=0
# # array[:1,2:3]=0
# # array[:2,:1]=0
# # array[:2,2:3]=0
# # array[:3,:1]=0
# # array[:3,2:3]=0
# # array[:4,:1]=0
# # array[:4,2:3]=0
# # print(array)
#
# mask=array%2==0
# print(mask)
#










