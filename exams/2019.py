# Exercise 1

# Let A be an nxn square matrix. The main diagonal of A are elements of the form
# A[i][i] (the row index equals the column index). The elements A[i][j] such that i < j
# are above the main diagonal and the elements A[i][j] such that i > j are below the
# main diagonal. For example, considered the following 3x3 matrix.

# [[1,2,3],
# [5,1,4]
# [6,7,1]]

# Here the numbers 1 all lie on the main diagonal, numbers 2, 3, 4 lie above the main
# diagonal and numbers 5, 6, 7 lie below the main diagonal.

# (a) Write an O(n) algorithm computing the sum of elements of the main diagonal
# of a matrix A.

def DiagonalSum(A):
  total = 0

  for i in range(0, len(A)):
    total += A[i][i]

  return total

A = [
  [1,2,3],
  [5,1,4],
  [6,7,1]
]

assert DiagonalSum(A) == 3, "Diagonal should be equal to 3"

# (b) A matrix is called triangular if all the elements below the main diagonal equal
# zero. Write an O(n2) algorithm that prints 'YES' if the given matrix A is
# triangular and 'NO' otherwise.

# Lower Triangular
def IsTriangularMatrix(A):

  for i in range(0, len(A)):
    for j in range(i + 1, len(A)):
      if A[j][i] > 0:
        print("No")
        return False
  print("Yes")
  return True

A = [
  [1,2,3],
  [5,1,4],
  [6,7,1]
]

assert not IsTriangularMatrix(A), "Shouldn't be a lower triangular matrix"

A = [
  [1,2,3],
  [0,1,4],
  [0,7,1]
]

assert not IsTriangularMatrix(A), "Shouldn't be a lower triangular matrix"

A = [
  [1,2,3],
  [0,1,4],
  [0,0,1]
]

assert IsTriangularMatrix(A), "Should be a lower triangular matrix"

# Upper Triangular
def IsReverseTriangular(A):

  for i in range(0, len(A)):
    for j in range(i + 1, len(A)):
      if A[i][j] > 0:
        print("No")
        return False
  print("Yes")
  return True

A = [
  [1,2,3],
  [5,1,4],
  [6,7,1]
]

assert not IsReverseTriangular(A), "Shouldn't be a upper triangular matrix"

A = [
  [1,2,3],
  [0,1,4],
  [0,7,1]
]

assert not IsReverseTriangular(A), "Shouldn't be a upper triangular matrix"

A = [
  [1,0,0],
  [2,1,0],
  [3,5,1]
]

assert IsReverseTriangular(A), "Should be a uppers triangular matrix"

# Exercise 4

# (a) Write an algorithm whose input is an array and the output is obtained by sorting
# the even elements of A in the increasing order while leaving the odd elements
# at their initial place. For example, if A = [5, 4, 3, 2, 1] then the resulting array
# must me [5, 2, 3, 4, 1].

# Can use selection sort for this
def swap(ls, i, j):
  tmp = ls[i]
  ls[i] = ls[j]
  ls[j] = tmp

def isEven(n):
  return n % 2 == 0

def isEvenAhead(a, b):
  return isEven(a) and isEven(b) and a < b

def EvenSelectionSort(A):
  for i in range(0, len(A)):
    jMin = i

    for j in range(i + 1, len(A)):
      if isEvenAhead(A[j], A[jMin]):
        jMin = j

    if jMin != i:
      swap(A, i, jMin)

  return A

A = [5, 4, 3, 2, 1]

print(EvenSelectionSort(A), [5, 2, 3, 4, 1])

# (b) Solve the same problem but with an O(n log n) algorithm. Note that if you solve
# this question correctly, it will also be a solution for question 4 a).
# Hint: Copy even elements in a separate array and apply Merge Sort. Then copy
# the element back to the initial array. In order to do the last step, you need to
# maintain an array of indices of the even elements in the initial array.

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

# O(4n log n) -> O(n log n)
def EvenMergeSort(A):
  evenIdxs = []
  evenEls = []

  # O(n)
  for i in range(0, len(A)):
    if isEven(A[i]):
      evenIdxs.append(i)
      evenEls.append(A[i])

  # O(n log n)
  evenEls = MergeSort(evenEls, 0, len(evenEls) - 1)

  # O(n)
  for i in range(len(evenIdxs)):
    A[evenIdxs[i]] = evenEls[i]  
  
  return A

A = [5, 4, 3, 2, 1]
print(EvenMergeSort(A), [5, 2, 3, 4, 1])

A = [5, 8, 4, 2, 1, 2, 3, 4]
print(EvenMergeSort(A), [5, 2, 2, 4, 1, 4, 3, 8])


# Exercise 5

#   (a) A graph G on vertices 0,... n-1. Let A be represented by the adjacency matrix.
#   (b) Two disjoint subsets A (should be either B or C, since A is a matrix, lecturer mistake) and B of vertices of G (disjoint means that they do not
# have an element in common).
# 
# The program must print all the edges of G having one end in A, the other end in B.
# The program must work in O(n^2).

def PrintEdges(A, B, C):
  for i in range(0, len(B)):
    for j in range(0, len(C)):
      if A[B[i]][C[j]]:
        print(f'Edge: {B[i]}--{C[j]}')

#    -- 1 -- 3 --
#  /              \
# 0                5
#  \              /
#    -- 2 -- 4 --

# Disjoint sets
# [0, 1, 2]
# [3, 4, 5]

# Valid edges with one end in B and other C:
# 1 - 3
# 2 - 4

A = [
  [0, 1, 1, 0, 0, 0],
  [1, 0, 0, 1, 0, 0],
  [1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1],
  [0, 0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1, 0]
]

B = [0, 1, 2]
C = [3, 4, 5]

PrintEdges(A, B, C)

