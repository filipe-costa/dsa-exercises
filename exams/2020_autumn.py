# Exercise 1

# Write a program that computes the smallest element of each column and then
# prints the largest one out of these smallest elements.
# For example, these smallest column elements for the above matrix are 1; 2; 2
# while the largest is 2.

# Write a program that prints 'YES' if in each column of A all the values are
# distinct and 'NO' otherwise. For example, for the matrix above, the answer
# should be 'YES'. If for instance we change the bottom-right element to 3 then
# the answer becomes 'NO' as the last column has repeated elements.

# Exercise 2

# Let A be an array sorted in the increasing order. Design an O(n) algorithm that
# prints 'YES' if all the elements of A are distinct and 'NO' otherwise.

# A way to formaly dene a sorted array A of n elements is to say that for each i
# between 0 and n 􀀀 2, A[i]  A[i + 1]. Let us say that A is almost sorted if this
# rule is correct for all but one number k between 0 and n 􀀀 2. In other words,
# A[k] > A[k+1] but for each i such that i 6= k and 0  i  n􀀀2, A[i]  A[i+1].
# Design an O(n) algorithm whose input is an almost sorted array A and that
# solves the same task as for the rst part: prints 'YES' if all the elements of A
# are distinct and 'NO' if there are repetitions.

# Exercise 4

# Let G be a graph on vertices 0; : : : n 􀀀 1. Let A be the adjacency matrix of G. A
# triangle of G is a set of three distinct vertices i; j; k such that i is adjacent to j, i is
# adjacent to k and j is adjacent to k

# Use the function of the rst part to design an algorithm whose input is A
# and that prints the number of triangles of G. Note that you need to take
# necessary precautions to avoid the same triangle being counted more than once.

# Exercise 5

# Write a program whose input is A and S. The program must print 'YES' if G
# has a vertex v, not contained in S such that v is adjacent to all the vertices of
# S. Otherwise the program must print 'NO'.

# Write a program whose input is A and S. The program must print 'YES' if G
# has two vertices v1, and v2, neither of them contained in S such that each vertex
# of S is adjacent either to v1 or to v2. Otherwise, the program must print 'NO'.