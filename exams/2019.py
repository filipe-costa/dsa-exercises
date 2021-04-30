# Exercise 1

# Let A be an n  n square matrix. The main diagonal of A are elements of the form
# A[i][i] (the row index equals the column index). The elements A[i][j] such that i < j
# are above the main diagonal and the elements A[i][j] such that i > j are below the
# main diagonal. For example, considered the following 3x3 matrix.

# [ [1,2,3],
# [5,1,4]
# [6,7,1]]

# Here the numbers 1 all lie on the main diagonal, numbers 2; 3; 4 lie above the main
# diagonal and numbers 5; 6; 7 lie below the main diagonal.

# (a) Write an O(n) algorithm computing the sum of elements of the main diagonal
# of a matrix A. (5 marks)
# (b) A matrix is called triangular if all the elements below the main diagonal equal
# zero. Write an O(n2) algorithm that prints 'YES' if the given matrix A is
# triangular and 'NO' otherwise.

# Exercise 4

# (a) Write an algorithm whose input is an array and the output is obtained by sorting
# the even elements of A in the increasing order while leaving the odd elements
# at their initial place. For example, if A = [5; 4; 3; 2; 1] then the resulting array
# must me [5; 2; 3; 4; 1].

# (b) Solve the same problem but with an O(n log n) algorithm. Note that if you solve
# this question correctly, it will also be a solution for question 4 a).
# Hint: Copy even elements in a separate array and apply Merge Sort. Then copy
# the element back to the initial array. In order to do the last step, you need to
# maintain an array of indices of the even elements in the initial array.

# Exercise 5

#   (a) A graph G on vertices 0,... n-1. Let A represented by the adjacency matrix.
#   (b) Two disjoint subsets A and B of vertices of G (disjoint means that they do not
# have an element in common).
# 
# The program must print all the edges of G having one end in A, the other end in B.
# The program must work in O(n2).