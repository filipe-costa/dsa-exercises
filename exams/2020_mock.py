# Exercise 1 and some extras

A = [
  [1,2,3],
  [5,1,4],
  [6,7,1]
]

# Find the largest number in the main diagonal in the matrix
def LargestInDiagonal(A):
  largest = A[0][0]

  for i in range(1, len(A)):
    if A[i][i] > largest:
      largest = A[i][i]

  return largest

assert LargestInDiagonal(A) == 1, "Should be 1"

# Find the smallest number in the main diagonal in the matrix

def SmallestInDiagonal(A):
  smallest = A[0][0]

  for i in range(1, len(A)):
    if A[i][i] < smallest:
      smallest = A[i][i]

  return smallest

assert SmallestInDiagonal(A) == 1, "Should be 1"

# Find the largest number in the anti diagonal in the matrix

def LargestInAntiDiagonal(A):
  largest = A[0][len(A) - 1]

  for i in range(1, len(A)):
    if A[i][len(A) - 1 - i] > largest:
      largest = A[i][len(A) - 1 - i]

  return largest

assert LargestInAntiDiagonal(A) == 6, "Should be 6"

# Find the smallest number in the anti diagonal in the matrix
def SmallestInAntiDiagonal(A):
  smallest = A[0][len(A) - 1]

  for i in range(1, len(A)):
    if A[i][len(A) - 1 - i] < smallest:
      smallest = A[i][len(A) - 1 - i]

  return smallest

assert SmallestInAntiDiagonal(A) == 1, "Should be 1"

# Create list of all numbers in a diagonal and sort them in increasing order
def ListDiagonal(A):
  l = [A[0][0]]

  for i in range(1, len(A)):
    l.append(A[i][i])

  l.sort()

  return l

print(ListDiagonal(A), [1, 1, 1])

# Create list of all numbers in the anti-diagonal and sort them in decreasing order
def ListAntiDiagonal(A):
  l = [A[0][len(A) - 1]]

  for i in range(1, len(A)):
    l.append(A[i][len(A) - 1 - i])

  l.sort(reverse=True)

  return l

print(ListAntiDiagonal(A), [6,3,1])


# Compute the largest element above the main diagonal and the largest element below the main diagonal.

def LargestElementAboveAndBelowMainDiagonal(A):
  max_above = A[0][1]
  max_below = A[1][0]

  for i in range(0, len(A)):
    for j in range(0, len(A[i])):
      if i < j and A[i][j] > max_above:
        max_above = A[i][j]

      if j < i and A[i][j] > max_below:
        max_below = A[i][j]

  return (max_above, max_below)

print(LargestElementAboveAndBelowMainDiagonal(A))

# Compute the largest element above and below the anti diagonal.
def LargestElementAboveAndBelowAntiDiagonal(A):
  max_above = A[0][len(A[0]) - 2]
  max_below = A[1][len(A[0]) - 1]

  for i in range(0, len(A) - 1):
    for j in range(0, len(A[i]) - i - 1):
      if A[i][j] > max_above:
        max_above = A[i][j]

  for i in range(len(A) - 1, 0, -1):
    for j in range(len(A[i]) - 1, 0, -1):
      if A[i][j] > max_below:
        max_below = A[i][j]

  return (max_above, max_below)

print(LargestElementAboveAndBelowAntiDiagonal(A))

# Compute the smallest element above and below the anti diagonal.
def SmallestElementAboveAndBelowAntiDiagonal(A):
  min_above = A[0][len(A[0]) - 2]
  min_below = A[1][len(A[0]) - 1]

  for i in range(0, len(A) - 1):
    for j in range(0, len(A[i]) - i - 1):
      if A[i][j] > min_above:
        min_above = A[i][j]

  for i in range(len(A) - 1, 0, -1):
    for j in range(len(A[i]) - 1, 0, -1):
      if A[i][j] > min_below:
        min_below = A[i][j]

  return (min_above, min_below)

print(SmallestElementAboveAndBelowAntiDiagonal(A))

# Exercise 3

# Let A be a list of nonzero numbers without repetitions (the same number
# does not occur more than once). The separate sorting of positive and negative
# numbers applied to A produces an array B with the same elements as in A and
# the following two additional properties.
#   • All positive numbers are sorted in the increasing order and all the negative
# numbers are sorted in the increasing order.
#   • The elements retain their signs. That is, if A[i] < 0 then B[i] < 0 and if
# A[i] > 0 then B[i] > 0.

# Write a program that separately sorts positive and negative
# numbers of an array A

def SortPosNegNumbers(A):
  pos = []
  neg = []
  posIdx = []
  negIdx = []

  for i in range(0, len(A)):
    n = A[i]
    if n > 0:
      posIdx.append(i)
      pos.append(n)
    else:
      negIdx.append(i)
      neg.append(n)

  pos.sort()
  neg.sort()

  B = [0] * len(A)

  for i in range(0, len(posIdx)):
    B[posIdx[i]] = pos[i]

  for i in range(0, len(negIdx)):
    B[negIdx[i]] = neg[i]

  return B

A = [-5, 3, -10, 2]

print(SortPosNegNumbers(A))

# Solve the same task but this time the resulting program must
# run in O(n log n).

# O(n)
def Merge(A, B):
  R = []
  currA = 0
  currB = 0
  
  for _ in range(0, len(A) + len(B)):
    if currA < len(A) and currB < len(B):
      if A[currA] <= B[currB]:
        R.append(A[currA])
        currA += 1
      else:
        R.append(B[currB])
        currB += 1
    else:
      if currA == len(A):
        R.append(B[currB])
        currB += 1
      else:
        R.append(A[currA])
        currA += 1

  return R

# (n log n)
def MergeSort(A, i, j):
  if i == j:
    return
  mid = (i + j) // 2

  # Merge left Side
  MergeSort(A, i, mid)

  # Merge right side
  MergeSort(A, mid + 1, j)

  # This will combine the lists for every recursive call will return a bigger one from a smaller one
  A[i:j+1] = Merge(A[i:mid + 1], A[mid + 1:j + 1])
  return A

def MergeSortPosNegNumbers(A):
  pos = []
  neg = []
  posIdx = []
  negIdx = []

  for i in range(0, len(A)):
    n = A[i]
    if n > 0:
      posIdx.append(i)
      pos.append(n)
    else:
      negIdx.append(i)
      neg.append(n)

  MergeSort(pos, 0, len(pos) - 1)
  MergeSort(neg, 0, len(neg) - 1)

  B = [0] * len(A)

  for i in range(0, len(posIdx)):
    B[posIdx[i]] = pos[i]

  for i in range(0, len(negIdx)):
    B[negIdx[i]] = neg[i]

  return B

A = [-5, 3, -10, 2]

print(MergeSortPosNegNumbers(A), [-10, 2, -5, 3])

A = [-10, 2, 4, -30, 3]

print(MergeSortPosNegNumbers(A), [-30, 2, 3, -10, 4])

# Exercise 4

# Let BFS(G, i) be a function specified as follows.
# • G is a graph and i is a vertex of G.
# • BFS(G, i) performs Breadth-First Search (BFS) starting from vertex i.
# • The procedure returns the list L of the vertices it explored.

# Write a program that prints YES if graph G is connected
# and NO otherwise.


# Class BFS

def BFS(L, x):
  labelled = [0] * len(L)
  labelled[x] = 1
  Component = [x]
  curindex = 0

  while curindex < len(Component):
    y = Component[curindex]
    for i in range(0, len(L[y])):
      if (labelled[L[y][i]] == 0):
        labelled[L[y][i]] = 1
        Component.append(L[y][i])
    curindex += 1
  return Component

def isConnectedGraph(G):
  L = BFS(G, 0)
  if(len(L) == len(G)):
    return True
  else:
    return False

A = [
  [1,2,3],
  [0,2,4],
  [0,1,3,4,5],
  [0,2,6],
  [1,2,5],
  [2,4,6],
  [3,5]
]

assert isConnectedGraph(A), "Should be connected"

A = [
  [1, 2, 3],
  [0, 2],
  [0, 1, 3],
  [0, 2],
  [5],
  [4,6],
  [5]
]

assert not isConnectedGraph(A), "Should not be connected"

# Write a program that calculates the number of connected
# components of G.

def TotalNumberOfConnectedComponents(A):
  explored = [0] * len(A)
  numcomp = 0
  for i in range(0, len(A)):
    if(explored[i] == 0):

      L = BFS(A, i)

      for j in range(0, len(L)):
        explored[L[j]] = 1
      numcomp += 1

  return numcomp

A = [
  [1,2,3],
  [0,2,4],
  [0,1,3,4,5],
  [0,2,6],
  [1,2,5],
  [2,4,6],
  [3,5]
]

assert TotalNumberOfConnectedComponents(A) == 1, "Should be 1"

A = [
  [1, 2, 3],
  [0, 2],
  [0, 1, 3],
  [0, 2],
  [5],
  [4,6],
  [5]
]

assert TotalNumberOfConnectedComponents(A) == 2, "Should be 2"

# Exercise 5
# Counting the number of edges of an induced subgraph

# Write a program whose input is the following.
#   1. A graph G on vertices {0, . . . , n−1} represented by the adjacency matrix.
#   2. A subset A of vertices of G.

# The program must calculate the number of edges of the subgraph of G induced by A.

def TotalNumberOfEdges(G, A):
  numedges = 0

  for i in range(0, len(A) - 1):
    for j in range(i + 1, len(A)):
      vert1 = A[i]
      vert2 = A[j]
      
      if(G[vert1][vert2] == 1):
        numedges += 1
  
  return numedges

# Graph
#   / 1
#  /  |
# 0 - 2
#  \  |
#   \ 3
# 
G = [
  [0, 1, 1, 1],
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [1, 0, 1, 0],
]

# Induced sub-graph of G by A
#   / 1
#  /  |
# 0 - 2
# 
A = [0, 1, 2]
assert TotalNumberOfEdges(G, A) == 3, "Should be 3"

# Induced sub-graph of G by A
#   / 1
#  /  |
# 0 - 2
#  \  |
#   \ 3

A = [0, 1, 2, 3]
assert TotalNumberOfEdges(G, A) == 5, "Should be 5"
