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