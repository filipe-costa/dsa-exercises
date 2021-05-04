# Exercise 1

# Write a program whose input is a two-dimensional matrix A (table). The
# program prints for each row the dierence between the smallest and the largest
# element of that row. For instance, for the matrix
# [[12,5,7]
# [1,2,6]
# [3,4,0]
# ]
# these differences are 7, 5, 4.


# With the same input as in the previous item, write a program that prints the
# dierence between the largest and smallest elements of the whole matrix. For
# example, for the matrix as above this dierence is 12 - 0 = 12.


# As you can see from the previous two questions the dierences between largest
# smallest elements of the individual rows and the dierence between the largest
# and smallest elements of the whole matrix are in general unrelated. In particular,
# from the former being 7; 5; 4 it is impossible to gure out the latter being 12.
# However, if the dierences 7; 5; 4 are accompanied with the maximal values of
# the respective rows in the following way (7; 12); (5; 6); (4; 4) then the dierence
# between the largest and smallest elements of the whole matrix can be recovered.
# This is the topic of this question.
# Suppose that we have a matrix A but the input to the program is not the
# matrix itself but pairs (dierence between the largest and smallest elements,
# largest element) for each row of the matrix. Write a program that recovers the
# dierence between the largest and the smallest elements of the matrix.

# Exercise 3

# Write a program whose input are two lists A and W of real numbers. The
# program should print the weighted average of A with the weights provided by
# W.

# Let MARKS be a table whose rows correspond to students and columns correspond
# to modules. MARKS[i][j] is the mark that student i received for module j.
# Let LEV ELS be a list corresponding to modules such that LEV EL[i] contains
# the level of module i, which can be 4, 5, or 6. Write a program (whose input
# is MARKS and LEV ELS) that computes the weighted average mark of each
# student such that the weights depend on the levels as follows.
#  Each module of level 4 has weight 0.
#  Each module of level 5 has wieght 1.
#  Each module of level 6 has wieght 2.

# Exercise 4

# Write a program that takes as input two sorted lists A and B of integers without
# repetition and prints the list of all those numbers that occur in A but do not
# occur in B. For example if A = [1; 2; 3] and B = [2; 3; 4] then the program
# should print [1]. The runtime of the program must be O(n).

# Write a program whose input are lists A and B as in the rst part of this
# question. The program must print the list of all numbers that occur in A only
# (that is not in B) and all numbers that occur in B only (that is not in A). For
# A = [1; 2; 3] and B = [2; 3; 4] the output must be [1; 4]. As in the rst part, the
# runtime of the program must be O(n).

# Exercise 5

# Write a program taking as input a graph G in the form of its adjacency matrix
# and a list L of vertices of G. The program must print whether L is a Hamiltonian
# cycle of G. Hint: The program must check that each vertex of G (from 0 to
# n 􀀀 1) occurs in L exactly once that every two consecutive elements of L are
# adjacent in G and that the rst and the last elements of L are adjacent in G.