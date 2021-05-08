# Exercise 1

# Write a program that computes the smallest element of each column and then
# prints the largest one out of these smallest elements.
# For example, these smallest column elements for the above matrix are 1, 2, 2
# while the largest is 2.

def ExtractColumn(A, i):
  Col = []
  for j in range(0, len(A)):
    Col.append(A[j][i])
  return Col

def LargestElementInColumns(A):
  l = []
  for i in range(0, len(A)):
    col = ExtractColumn(A, i)
    l.append(min(col))
  return max(l)

A = [
  [1, 2, 2],
  [9, 3, 10],
  [7, 5, 4]
]

print(LargestElementInColumns(A))

# Write a program that prints 'YES' if in each column of A all the values are
# distinct and 'NO' otherwise. For example, for the matrix above, the answer
# should be 'YES'. If for instance we change the bottom-right element to 3 then
# the answer becomes 'NO' as the last column has repeated elements.

def AllDistinct(L):
  M = L
  M.sort()

  for i in range(0, len(M) - 1):
    if M[i] == M[i + 1]:
      return False
    return True

def NoRepeatColumns(A):
  for i in range(0, len(A)):
    CurCol = ExtractColumn(A, i)
    if (not AllDistinct(CurCol)):
      print("No")
      return
  
  print("Yes")

A = [ 
  [1,2,3],
  [5,3,4],
  [6,7,2]
]

NoRepeatColumns(A)

# Exercise 2

# Let A be an array sorted in the increasing order. Design an O(n) algorithm that
# prints 'YES' if all the elements of A are distinct and 'NO' otherwise.

def AllDistinct(A):
  for i in range(0, len(A) - 1):
    if A[i] == A[i + 1]:
      return False
  return True

# Merge sort here


# Exercise 4

# Let G be a graph on vertices 0, ... , n - 1. Let A be the adjacency matrix of G. A
# triangle of G is a set of three distinct vertices i, j, k such that i is adjacent to j, i is
# adjacent to k and j is adjacent to k

def isTriangle(G, i, j, k):
  if G[i][j] and G[j][k] and G[i][k]:
    return True
  return False

A = [
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
]

print(isTriangle(A, 0, 1, 2))

# Use the function of the first part to design an algorithm whose input is A
# and that prints the number of triangles of G. Note that you need to take
# necessary precautions to avoid the same triangle being counted more than once.

def CountTriangles(A):
  count = 0
  for i in range(0, len(A)):
    for j in range(i + 1, len(A[i])):
      if A[i][j]:
        for k in range(j + 1, len(A[i])):
          if isTriangle(A, i, j, k):
            count += 1
  return count

A = [
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
]

print(CountTriangles(A))

# Exercise 5

# Write a program whose input is A and S. The program must print 'YES' if G
# has a vertex v, not contained in S such that v is adjacent to all the vertices of
# S. Otherwise the program must print 'NO'.

def isDominated(A, S, v):
  for i in range(0, len(S)):
    vtx = S[i]
    if not A[vtx][v]:
      return False
  return True

def isVertexAdjacentToAllInS(A, S):
  for i in range(0, len(A)):
    if A[i]:
      if isDominated(A, S, i):
        print("YES")
        return

  print("NO")

A = [
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
]

S = [1, 2]

isVertexAdjacentToAllInS(A, S)


# Write a program whose input is A and S. The program must print 'YES' if G
# has two vertices v1, and v2, neither of them contained in S such that each vertex
# of S is adjacent either to v1 or to v2. Otherwise, the program must print 'NO'.

def isDominatedPair(A, S, v1, v2):
  for i in range(0, len(S)):
    vtx = S[i]
    if not A[vtx][v1] and not A[vtx][v2]:
      return False
  return True


def isDominatedVertexPair(A, S):

  for i in range(0, len(A)):
    for j in range(i + 1, len(A)):
      if isDominatedPair(A, S, i, j):
        print("YES")
        return

  print("NO")

A = [
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
]

S = [2]

isVertexAdjacentToAllInS(A, S)