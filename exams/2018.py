# Exercise 3

# Write a program whose input is an array A of positive numbers and a positive
# number x. The program should print the smallest element of A that is greater
# than x. If such an element does not exist, the program should print 1. For
# example, if A = [1, 3, 5, 3, 6, 5] and x = 3 then the program should print 5. You
# may not use recursion for this particular task.
def findSmallestGreaterThanX(A, x):
  foundFirstGreatest = False
  smallest = 1

  for i in range(0, len(A)):
    n = A[i]
    if not foundFirstGreatest and n > x:
      foundFirstGreatest = True
      smallest = n
    elif n < smallest and n > x:
      smallest = n

  return smallest

A = [1, 3, 5, 4, 6, 5]

print(findSmallestGreaterThanX(A, 3))

# Write a recursive program for the same task as in first part.
def findSmallestGreaterThanXRec(A, x, i, foundGreatest = False, smallest = 1):

  if i >= 0:
    n = A[i]

    if not foundGreatest and n > x:
      return findSmallestGreaterThanXRec(A, x, i - 1, True, n)
    elif n < smallest and n > x:
      return findSmallestGreaterThanXRec(A, x, i - 1, foundGreatest, n)

  return smallest

A = [1, 3, 3]
print(findSmallestGreaterThanXRec(A, 1, len(A) - 1))

# Exercise 4
# The dot product of two arrays of length n is the sum of the products of the
# corresponding elements. That is, the dot product of arrays A[0], ..., A[n - 1]
# and B[0], ..., B[n - 1] is A[0]  B[0] + ... + A[n - 1]  B[n - 1]. For example,
# the dot product of [5, 1, 8] and [1, 2, 3]= 5 * 1 + 1  2 + 8 + 3 = 5 + 2 + 24 = 31.
# Write a program whose input is two arrays A and B of the same length that
# computes their dot product.

def DotProductOfLists(A, B):
  total = 0

  for i in range(0, len(A)):
    total = total + A[i] * B[i]
  return total


A = [5, 1, 8]
B = [1, 2, 3]

print(DotProductOfLists(A, B), 31)


# Write a program whose input is two nxn matrices A and B and two numbers i
# and j, both between 0 and n-1. The output of this program is the dot product
# of the i-th row of A and the j-th column of B.

def DotProductOfMatrices(A, B, i, j):
  total = 0

  k = 0
  z = 0

  while k < len(A[i]):
    total += A[i][k] * B[z][j]
    z += 1
    k += 1

  return total

A = [
  [1, 2, 3],
  [4, 5, 6],
]
B = [
  [7, 8],
  [9, 10],
  [11, 12],
]

print(DotProductOfMatrices(A, B, 0, 0), 2)

# The product of two nxn matrices A and B is an nxn matrix C such that
# that C[i,j] equals the dot product of the i-th row of A and the j-th column of
# B. Write a program whose input is two nn matrices A and B and the output
# is the product of A and B.

def DotProductOfMatrices(A, B):
  C = [[0 for j in range(len(B[i]))] for i in range(len(A))]

  for i in range(0, len(C)):
    for j in range(0, len(C[i])):
      t = 0
      for k in range(len(B)):
        t += A[i][k] * B[k][j]

      C[i][j] = t

  return C

A = [
  [1, 2, 3],
  [4, 5, 6],
]

B = [
  [7, 8],
  [9, 10],
  [11, 12],
]

print(DotProductOfMatrices(A, B))

# Exercise 5

# The independence number of a graph G is the largest number of vertices no two of which are connected by an edge.  
# Determine the independence numbers of the two graphs G1 and G2 shown below.

#    G1
#     0
#     |\
#     |  \
# 1   |   5
# | \ |  /|
# |  \| / |
# |   6   | 
# | / | \ |
# 2   |   4
#  \  |  /
#   \ | /
#     3

G1 = [
  [0, 0, 0, 0, 0, 1, 1],
  [0, 0, 1, 0, 0, 0, 1],
  [0, 1, 0, 1, 0, 0, 1],
  [0, 0, 1, 0, 1, 0, 1],
  [0, 0, 0, 1, 0, 1, 1],
  [1, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 0]
]

# Valid sets
# [0, 1, 3]
# [1, 3, 5]
# [0, 4, 1]

#    G2
#     0
#       \
#        \
# 1       5
# |       |
# |       |
# 2       4
#  \      /
#   \    /
#     3

# Valid sets:
# [0, 1, 3]
# [1, 3, 5]
# [0, 4, 1]

G2 = [
  [0, 0, 0, 0, 0, 1],
  [0, 0, 1, 0, 0, 0],
  [0, 1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1, 0],
  [0, 0, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0]
]

def isClique(G, S, j):
  if len(S) < 1:
    return False
  
  for i in range(0, len(S)):
    vertex = S[i]
    if G[vertex][j] == 1:
      return True
  return False

def IndependenceNumberOfGraphClique(G):

  # Assuming starting at 0
  S = [0]

  visited = [0] * len(G)
  visited[0] = 1

  for i in range(0, len(G)):
    for j in range(i + 1, len(G[i])):
      if not isClique(G, S, j) and visited[j] == 0:
        S.append(j)
        visited[j] = 1

  return len(S)


assert IndependenceNumberOfGraphClique(G1) == 3, "Should be 3"
assert IndependenceNumberOfGraphClique(G2) == 3, "Should be 3"

# What is the independence number of a graph of n vertices every two vertices of which are connected by an edge?
# In other words, the number of all edges in the graph

def IndependenceNumberOfGraph(G):
  n = 0

  for i in range(0, len(G)):
    for j in range(i + 1, len(G[i])):
      if G[i][j] == 1:
        n += 1

  return n

assert IndependenceNumberOfGraph(G1) == 11, "Should be 11"
assert IndependenceNumberOfGraph(G2) == 5, "Should be 5"

# What is the independence number of a graph with at least three vertices and only one edge?

# Given the following graph
#    1
# 0  |
#    2
# One can conclude that the maximum independence number of a graph is 2
# The reason being that 0 is not connected to either 1 or 2
# Therefore our set would look like [0, 1] or [0, 2], since 1 and 2 are adjacent
# We don't add one or the other depending on how we have composed our set.

G3 = [
  [0, 0, 0],
  [0, 0, 1],
  [0, 1, 0]
]

assert IndependenceNumberOfGraphClique(G3) == 2, "Should be 2"
