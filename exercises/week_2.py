# Exercise 1
# Write a function whose input is a matrix A. This function returns
# true if each row and each column have no repeated occurrences and false
# otherwise.
A = [
  [1,2,3],
  [3,1,2],
  [2,3,1]
]

B = [
  [2,2,3],
  [3,1,2],
  [2,3,1]
]

C = [
  [3,2,1],
  [2,1,1],
  [1,3,2]
]

D = [
  [1,3,2],
  [2,1,1],
  [1,3,1]
]

def isInRow(v, A, j):
  # Checks if the next item in the row is the same
  for k in range(0, len(A)):
    # We skip the element that matches the current one at A[k]
    # We just check the previous and next values in this row
    # This avoids false positives
    if k == j:
      continue
    if v == A[k]:
      return True
    
  return False

def isInColumn(v, A, j, i):
  for k in range(0, len(A)):
    # We skip the row that matches the current one
    # We just check the previous and next values in this column
    # This avoids false positives
    if k == i:
      continue
    if v == A[k][j]:
      return True

  return False

def isNotRepeated(A):
  for i in range(0, len(A)):
    curRow = A[i]
    for j in range(0, len(curRow)):
      curVal = curRow[j]
      if isInRow(curVal, curRow, j) and isInColumn(curVal, A, j, i):
        return False
  return True

assert isNotRepeated(A), "Has repeated elements"
assert not isNotRepeated(B), "Doesn't have repeated elements"
assert not isNotRepeated(C), "Doesn't have repeated elements"
assert not isNotRepeated(D), "Doesn't have repeated elements"

# Exercise 2
# The input of the tasks of this exercise is a matrix MARKS whose
# rows correspond to students and columns correspond to modules. The entries of
# the matrix are marks of the corresponding student for the corresponding module.
marks = [
  [40, 40, 40, 40, 20],
  [50, 60, 20, 10, 20],
  [20, 40, 20, 30, 30],
  [20, 20, 30, 20, 20]
]

# Write a function returning the list of average marks of all students.
# Assume that all modules are taken and have marks
def avgRowMarks(A): 
  avg = 0
  count = 0

  for i in range(0, len(A)):
    avg += A[i]
    count += 1

  return round(avg / count, 2)

def STAverages(marks):
  averages = []

  for i in range(0, len(marks)):
    curAvg = avgRowMarks(marks[i])
    averages.append(curAvg)

  return averages

# Write a function returning the list of average marks of all modules.
# Assume that all modules are taken and have marks
def getColumn(A, j):
  Column = []

  for i in range(0, len(A)):
    Column.append(A[i][j])

  return Column

def avgMarks(A):
  avg = 0
  count = 0

  for i in range(0, len(A)):
    avg += A[i]
    count += 1

  return round(avg / count, 2)

def MODAverages(marks):
  averages = []

  for i in range (0, len(marks[0])):
    curCol = getColumn(marks, i)
    curAvg = avgMarks(curCol)
    averages.append(curAvg)

  return averages

print(STAverages(marks))
print(MODAverages(marks))

# Exercise 3
# A graph is regular if the degrees of all the vertices are the same. Write a function
# whose input is an adjacency matrix A of a graph G. The function returns true
# if G is a regular graph and false otherwise.

# 0-regular graph
A = [
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0]
]

# 1-regular graph
B = [
  [0,1,0,0,0,0],
  [1,0,0,0,0,0],
  [0,0,0,1,0,0],
  [0,0,1,0,0,0],
  [0,0,0,0,0,1],
  [0,0,0,0,1,0]
]

# 2-regular graph
C = [
  [0,1,1,0,0,0],
  [1,0,1,0,0,0],
  [1,1,0,0,0,0],
  [0,0,0,0,1,1],
  [0,0,0,1,0,1],
  [0,0,0,1,1,0]
]

# 3-regular graph
D = [
  [0,1,0,1,0,1],
  [1,0,1,0,0,1],
  [0,1,0,1,1,0],
  [1,0,1,0,1,0],
  [0,0,1,1,0,1],
  [1,1,0,0,1,0]
]

# Not regular graph
E = [
  [0,1,0,1,0,1],
  [1,0,1,0,0,1],
  [1,1,0,1,1,0],
  [1,0,1,0,1,0],
  [0,0,1,1,0,1],
  [1,1,0,0,1,0]
]

# Lecture matrix
I = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,0,1],
  [0,0,1,0,1],
  [0,0,1,1,0]
]

# bipartite graph
BG = [
  [0,0,0,1,1,1],
  [0,0,0,1,1,1],
  [0,0,0,1,1,1],
  [1,1,1,0,0,0],
  [1,1,1,0,0,0],
  [1,1,1,0,0,0]
]

# Regular graph vertices need to have the same number of degrees
def isRegularGraph(A):

  # Get list of degrees
  d0 = sum(A[0])

  if d0 == 0:
    return False
  
  # Do comparisons from i to i - 1
  for i in range(1, len(A)):
    d = sum(A[i])
    if d0 != d:
      return False

  return True

assert not isRegularGraph(A), "It is a regular graph"
assert not isRegularGraph(E), "It is a regular graph"
assert not isRegularGraph(I), "It is a regular graph"

assert isRegularGraph(B), "It is not a regular graph"
assert isRegularGraph(C), "It is not a regular graph"
assert isRegularGraph(D), "It is not a regular graph"
assert isRegularGraph(BG), "It is not a regular graph"

# Exercise 4
# Three different vertices i; j; k are called a triangle if i is adjacent
# to j, j is adjacent to k, and i is adjacent to k. In other words, a triangle is
# just a clique of size 3. Write a function TrianglesCount. The input of this
# function is the adjacency matrix A of a graph G and the output is the number
# of triangles of G.

def TrianglesCount(A):
  total = 0

  for i in range(len(A)):
    for j in range(len(A[i])):
      if (A[i][j]):
        for k in range(len(A[i])):
          if (A[i][j] and A[j][k] and A[i][k]):
            total += 1

  return (total // 6)

A = [
  [0,1,1],
  [1,0,1],
  [1,1,0]
]
assert TrianglesCount(A) == 1, "More than 1 triangle"

B = [
  [0,1,1,0,0,0],
  [1,0,1,0,0,0],
  [1,1,0,0,0,0],
  [0,0,0,0,1,1],
  [0,0,0,1,0,1],
  [0,0,0,1,1,0]
]
assert TrianglesCount(B) == 2, "More than 2 triangles"

# Exercise 5
# Let S be a subset of vertices of G. We say that S is a dominating
# set of G if each vertex of G is either contained in S or dominated by S.
# Write a function IsDominatingSet whose input is the adjacency matrix A of a graph
# G and a list S containing a subset of vertices of G. The function must return
# true if S is a dominating set of G and false otherwise.
# Note: wikipedia description is slightly different

def isDominated(A,S,v):
  for i in range(0, len(S)):
    vert=S[i]
    if(A[vert][v] == 1):
      return True
  return False

def isDominatingSet(A, S):
  count = 0
  for i in range(0, len(A)):
    if(isDominated(A, S, i)):
      count += 1

  return (count == len(A) - len(S))

#    -- 1 -> 3
#  /   |   / |
# 0    |  /  |
#  \   | v   |
#    -- 2 -- 4

# Valid sets
# [1, 4]
# [1, 3]
# [0, 3]
# [0, 4]

# Invalid sets
# [2, 3]
# [0, 1]
# [1, 2]

matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,0,1],
  [0,0,1,0,1],
  [0,0,1,1,0]
]

subSet0 = [1, 4]
assert isDominatingSet(matrix, subSet0), "It is not a dominating set"

matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,0,1],
  [0,0,1,0,1],
  [0,0,1,1,0]
]

subSet1 = [0, 3]
assert isDominatingSet(matrix, subSet1), "It is not a dominating set"

matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,0,1],
  [0,0,1,0,1],
  [0,0,1,1,0]
]
subSet2 = [0, 3]
assert isDominatingSet(matrix, subSet2), "It is not a dominating set"

matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,0,1],
  [0,0,1,0,1],
  [0,0,1,1,0]
]
invalidSubSet0 = [2, 3]
assert not isDominatingSet(matrix, invalidSubSet0), "It is a dominating set"

matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,0,1],
  [0,0,1,0,1],
  [0,0,1,1,0]
]
invalidSubSet1 = [0, 1]
assert not isDominatingSet(matrix, invalidSubSet1), "It is a dominating set"

# Exercise 6
# A subset S of vertices of a graph G is called a vertex cover of G
# if each edge of G has at least one end in S.
# Write a function IsV ertexCover whose
# input is the adjacency matrix A of a graph G and a subset of vertices of G (in
# the form of a list). The function returns true if S is a vertex cover of G and
# false otherwise.

def isCovered(edge, vx):
  i, j = edge
  if vx == i or vx == j:
    return True
  return False

# Delete covered edges
def deleteEdges(A, S,):
  for i in range(len(A)):
    for j in range(len(A[i])):
      edge = [i, j]
      for k in range(len(S)):
        vx = S[k]
        # if each edge of G has at least one end in S.
        # Delete the edge
        if isCovered(edge, vx):
          A[i][j] = 0
          A[j][i] = 0

def isVertexCover(A, S):
  deleteEdges(A, S)
  # If an edge still exists
  # It means that our subset of vertices doesn't cover the whole graph
  for i in range(len(A)):
    for j in range(len(A[i])):
      if A[i][j]:
        return False
  return True

#    -- 1 -- 3
#  /   |   / |
# 0    |  /  |
#  \   | /   |
#    -- 2 -- 4

# Valid subsets:

# [0, 1, 2, 4]
# [1, 2, 3]
# [1, 2, 4]

# Invalid subsets

# [0, 1]
# [0, 1, 3]
# [1, 2]

# Undirected graph
matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,1,1],
  [0,1,1,0,1],
  [0,0,1,1,0]
]
subSet0 = [0, 1, 2, 4]
assert isVertexCover(matrix, subSet0), "It is not a Vertex Cover"

# Undirected graph
matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,1,1],
  [0,1,1,0,1],
  [0,0,1,1,0]
]
subSet1 = [1, 2, 4]
assert isVertexCover(matrix, subSet1), "It is not a Vertex Cover"

# Undirected graph
matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,1,1],
  [0,1,1,0,1],
  [0,0,1,1,0]
]
subSet2 =  [1, 2, 3]
assert isVertexCover(matrix, subSet2), "It is not a Vertex Cover"

# Undirected graph
matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,1,1],
  [0,1,1,0,1],
  [0,0,1,1,0]
]
invalidSubSet0 = [0, 1]
assert not isVertexCover(matrix, invalidSubSet0), "It is a Vertex Cover"

# Undirected graph
matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,1,1],
  [0,1,1,0,1],
  [0,0,1,1,0]
]
invalidSubSet1 = [0, 1, 3]
assert not isVertexCover(matrix, invalidSubSet1), "It is a Vertex Cover"

# Undirected graph
matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,1,1],
  [0,1,1,0,1],
  [0,0,1,1,0]
]
invalidSubSet2 = [1, 2]
assert not isVertexCover(matrix, invalidSubSet2), "It is a Vertex Cover"

#     1
#     | \
#     |  \
# 0 --|-- 3
#     |  /
#     | /
#     2

# Valid subsets

# [0, 1, 3]
# [1, 3]

# Invalid subsets
# [0, 1]
# [1, 2]

matrix = [
  [0, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 1, 0, 1],
  [1, 1, 1, 0],
]

subSet0 = [0, 1, 3]
assert isVertexCover(matrix, subSet0), "It is not a Vertex Cover"

matrix = [
  [0, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 1, 0, 1],
  [1, 1, 1, 0],
]

subSet1 = [1, 3]
assert isVertexCover(matrix, subSet1), "It is not a Vertex Cover"

matrix = [
  [0, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 1, 0, 1],
  [1, 1, 1, 0],
]

invalidsubSet0 = [0, 1]
assert isVertexCover(matrix, subSet0), "It is a Vertex Cover"

matrix = [
  [0, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 1, 0, 1],
  [1, 1, 1, 0],
]

invalidsubSet1 = [1, 2]
assert isVertexCover(matrix, subSet1), "It is a Vertex Cover"