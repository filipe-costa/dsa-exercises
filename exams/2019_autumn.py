# Exercise 1

# Write a program whose input is a two-dimensional matrix A (table). The
# program prints for each row the difference between the smallest and the largest
# element of that row. For instance, for the matrix
# [[12,5,7]
# [1,2,6]
# [3,4,0]
# ]
# these differences are 7, 5, 4.

def PrintDifferences(A):

  for i in range(0, len(A)):
    print(max(A[i]) - min(A[i]))

A = [
  [12,5,7],
  [1,2,6],
  [3,4,0],
]

PrintDifferences(A)

# With the same input as in the previous item, write a program that prints the
# difference between the largest and smallest elements of the whole matrix. For
# example, for the matrix as above this difference is 12 - 0 = 12.

def PrintLargestMatrixDifference(A):
  largest = max(A[0])
  smallest = min(A[0])

  for i in range(1, len(A)):
    ma = max(A[i])
    mi = min(A[i])

    if ma > largest: 
      largest = ma
    
    if mi < smallest:
      smallest = mi
    
  print(largest - smallest)

A = [
  [12,5,7],
  [1,2,6],
  [3,4,0],
]

PrintLargestMatrixDifference(A)


# As you can see from the previous two questions the differences between largest
# smallest elements of the individual rows and the difference between the largest
# and smallest elements of the whole matrix are in general unrelated. In particular,
# from the former being 7, 5, 4 it is impossible to figure out the latter being 12.
# However, if the differences 7, 5, 4 are accompanied with the maximal values of
# the respective rows in the following way (7, 12), (5, 6), (4, 4) then the difference
# between the largest and smallest elements of the whole matrix can be recovered.
# This is the topic of this question.
# Suppose that we have a matrix A but the input to the program is not the
# matrix itself but pairs (difference between the largest and smallest elements,
# largest element) for each row of the matrix. Write a program that recovers the
# difference between the largest and the smallest elements of the matrix.

def PrintLargestPairDifference(B):
  largest = B[0][1]
  smallest = B[0][1] - B[0][0]

  print(B)
  for i in range(1, len(B)):
    ma = B[i][1]
    mi = B[i][1] - B[i][0]

    if ma > largest:
      largest = ma
    
    if mi < smallest:
      smallest = mi

  print(largest - smallest)

B = [(7, 12), (5, 6), (4, 4)]

PrintLargestPairDifference(B)

# Exercise 3

# Write a program whose input are two lists A and W of real numbers. The
# program should print the weighted average of A with the weights provided by
# W.

def WeightedAverage(A, W):
  num = 0
  denom = 0

  for i in range(0, len(A)):
    num += A[i] * W[i]
    denom += W[i]

  print(round(num / denom, 2))


A = [20, 30, 40]
W = [0, 2, 3]

WeightedAverage(A, W)

# Let MARKS be a table whose rows correspond to students and columns correspond
# to modules. MARKS[i][j] is the mark that student i received for module j.
# Let LEV ELS be a list corresponding to modules such that LEV EL[i] contains
# the level of module i, which can be 4, 5, or 6. Write a program (whose input
# is MARKS and LEV ELS) that computes the weighted average mark of each
# student such that the weights depend on the levels as follows.
#  Each module of level 4 has weight 0.
#  Each module of level 5 has wieght 1.
#  Each module of level 6 has wieght 2.

def Weights(Levels):
  W = [0] * len(Levels)
  for i in range(0, len(Levels)):
    if Levels[i] == 4:
      W[i] = 0
    elif Levels[i] == 5:
      W[i] = 1
    else:
      W[i] = 2
  
  return W


def WeightedMarks(Marks, Levels):
  W = Weights(Levels)
  for i in range(0, len(Marks)):
    WeightedAverage(Marks[i], W)

Marks = [[20, 30, 40], [30, 90, 40]]
Levels = [4, 5, 6]

WeightedMarks(Marks, Levels)

# Exercise 4

# Write a program that takes as input two sorted lists A and B of integers without
# repetition and prints the list of all those numbers that occur in A but do not
# occur in B. For example if A = [1, 2, 3] and B = [2, 3, 4] then the program
# should print [1]. The runtime of the program must be O(n).

def OccurrencesInANotInB(A, B):
  countA = 0
  countB = 0

  C = []

  while countA < len(A) or countB < len(B):
    if countA < len(A) and countB < len(B):
      if A[countA] < B[countB]:
        C.append(A[countA])
        countA += 1
      if A[countA] == B[countB]:
        countA += 1
        countB += 1
      else:
        countB += 1
    elif countA < len(A) and countB == len(B):
      C.append(A[countA])
      countA += 1
    else:
      break
  
  print(C)

A = [1, 2, 3]
B = [2, 3, 4]

OccurrencesInANotInB(A, B)

# Write a program whose input are lists A and B as in the first part of this
# question. The program must print the list of all numbers that occur in A only
# (that is not in B) and all numbers that occur in B only (that is not in A). For
# A = [1, 2, 3] and B = [2, 3, 4] the output must be [1, 4]. As in the first part, the
# runtime of the program must be O(n).

def DifferencesBetweenAandB(A, B):
  countA = 0
  countB = 0
  sizeA = len(A)
  sizeB = len(B)

  C = []

  while countA < sizeA or countB < sizeB:
    if countA < sizeA and countB < sizeB:
      if A[countA] < B[countB]:
        C.append(A[countA])
        countA += 1
      if A[countA] == B[countB]:
        countA += 1
        countB += 1
      else:
        C.append(B[countB])
        countB += 1
    elif countA < sizeA and countB == sizeB:
      C.append(A[countA])
      countA += 1
    else:
      C.append(B[countB])
      countB += 1

  print(C)


A = [1, 2, 3]
B = [2, 3, 4]

DifferencesBetweenAandB(A, B)


# Exercise 5

# Write a program taking as input a graph G in the form of its adjacency matrix
# and a list L of vertices of G. The program must print whether L is a Hamiltonian
# cycle of G. Hint: The program must check that each vertex of G (from 0 to
# n - 1) occurs in L exactly once that every two consecutive elements of L are
# adjacent in G and that the first and the last elements of L are adjacent in G.

def IsHamiltonianCycle(G, L):
  if len(L) < 3:
    return False

  nextVert = None
  prevVert = None

  # BFS
  visited = [0] * len(G)
  for i in range(0,len(L)):
    currVert = L[i]

    # Check if we already visited this node
    if visited[currVert] == 1:
      return False

    # Set current vertex as visited
    visited[currVert] = 1

    # Check adjacencies of the current vertex
    # First the next and previous vertices are computed
    # How to compute the previous and next vertex ?
    if i == 0:
      nextVert = L[1]
      prevVert = L[i - 1]
    elif i == 1:
      nextVert = L[i + 1]
      prevVert = L[i - 1]
    else:
      # If we are at the end of the list
      # Then we want to wrap it back to the beginning and check if last and first are adjacent
      if (i + 1) == len(L):
        nextVert = L[0]
        prevVert = L[i - 1]
      else:
        nextVert = L[i + 1]
        prevVert = L[i - 1]

    if (G[currVert][nextVert] == 0 or G[currVert][prevVert] == 0):
      return False

  return True


# Graph 1

# 1 --- 2
#   \ /
#    3
#   / \
# 5 --- 4

G1 = [
#  0, 1, 2, 3, 4, 5  
  [0, 0, 0, 0, 0, 0], # 0
  [0, 0, 1, 1, 0, 0], # 1
  [0, 1, 0, 1, 0, 0], # 2
  [0, 1, 1, 0, 1, 1], # 3
  [0, 0, 0, 1, 0, 1], # 4
  [0, 0, 0, 1, 1, 0]  # 5
]

L1 = [1, 2, 3, 4, 5]

assert not IsHamiltonianCycle(G1, L1), "Should not be a Hamiltonian Cycle"

# Graph 2

# 1 --- 2
#   \ /
#    /
#   / \
# 4 --- 3

G2 = [
#  0, 1, 2, 3, 4 
  [0, 0, 0, 0, 0], # 0
  [0, 0, 1, 1, 0], # 1
  [0, 1, 0, 0, 1], # 2
  [0, 1, 0, 0, 1], # 3
  [0, 0, 1, 1, 0], # 4
]

L2 = [1, 2, 4, 3]

IsHamiltonianCycle(G2, L2)

assert IsHamiltonianCycle(G2, L2), "Should be a Hamiltonian Cycle"

# Graph 3

# 1 --- 2
#   \ /
#    3

G3 = [
#  0, 1, 2, 3
  [0, 0, 0, 0], # 0
  [0, 0, 1, 1], # 1
  [0, 1, 0, 1], # 2
  [0, 1, 1, 0], # 3
]

L3 = [1, 2, 3]

assert IsHamiltonianCycle(G3, L3), "Should be a Hamiltonian Cycle"