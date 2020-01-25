#Nested list comprehension
matrix=[[j for j in range(3)]for i in range(5)]
print(matrix)

#Flatten a 2d list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
flatten_matrix=[val for sublist in matrix for val in sublist]
print(flatten_matrix)

#Flatten a list with some restriction
flatten_res=[val for sublist in matrix for val in sublist if val%2==00]
print(flatten_res)
