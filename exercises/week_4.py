# Runtime constraints

# Exercise 2

# Print all triples of elements of A while still having only a single loop.

def PrintTriplets(A):
  i = 0
  j = 0
  k = 0

  while i < len(A):
    print(A[i], A[j], A[k])

    if j < len(A) - 1:
      j += 1
      k += 1
    else:
      j = 0
      k = 0
      i += 1

A = [1, 2, 3]

PrintTriplets(A)

# Print all triples of elements of A while still having 1 nested loop just like above

def PrintTripletsNestedLoops(A):
  k = 0
  for i in range(len(A)):
    for j in range(0, len(A)):
      print(A[i], A[j], A[k])
      if k < len(A) - 1:
        k += 1
      else:
        k = 0

A = [1, 2, 3]
PrintTripletsNestedLoops(A)

# Exercise 4
# Assume that A is sorted. Design a function that returns an element
# having the largest number of occurrences in A. The runtime of the function
# should be O(n).

def ElementWithLargestNOccurrences(A):
  largest = 0
  occ = 1
  target_index = 0

  for i in range(0, len(A) - 1):
    if A[i] == A[i + 1]:
      occ += 1
    else:
      occ = 1
    if largest < occ:
      largest = occ
      target_index = i

  return A[target_index]

A = [1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 4]
assert ElementWithLargestNOccurrences(A) == 4, "It should be 4"

# Exercise 5

# In this exercise we will get an insight into the methodology
# of amortized analysis briefly mentioned in the previous section. In particular,
# we will see a meaningful reason for an O(n) algorithm to be implemented through
# a nested loop.

# Write a function whose input is a sorted array A. The function should
# return true if A has two elements (not necessarily distinct) whose sum is
# 20 and false otherwise. The runtime of the function should be O(n).

def AmortizedSum(A):
  for i in range(0, len(A)):
    for j in range(0, len(A) - 1):
      if abs(A[i] + A[j]) == 20:
        return True
  return False

A = [10, 10, 5, 15]

print(AmortizedSum(A), True)

# Write a function whose input is a sorted array A. The function should
# return true if A has two elements whose dierence (the absolute value of
# one subtracted from the other) is 20 and false otherwise. The runtime of
# the function should be O(n).

def AmortizedDifference(A):
  for i in range(0, len(A)):
    for j in range(0, len(A) - 1):
      if abs(A[i] - A[j]) == 20:
        return True
  return False

A = [10, 10, 5, 30]

print(AmortizedDifference(A), True)

# Exercise 6

# Let A be a list of integers between 0 and len(A) - 1. Design a linear
# time algorithm that returns true if A has multiple occurrences of the same
# element and false otherwise.

# Assuming that the list is sorted, a possible algorithm would be the following:
def MultipleOccurrencesInSortedList(A):
  for i in range(0, len(A) - 1):
    if A[i] == A[i + 1]:
      return True
  return False

A = [1, 1, 2, 2]
assert MultipleOccurrencesInSortedList(A), "Should be True not False"

A = [1, 2, 3, 4]
assert not MultipleOccurrencesInSortedList(A), "Should be False not True"

# Assume that the list is unsorted, a possible algorithm would be following:
# [0, 1, 2, 3, 4]
def MultipleOccurrencesInUnsortedList(A):
  d = {}

  for i in range(0, len(A)):
    if A[i] not in d:
      d[A[i]] = 1
    elif A[i] in d:
      return True

  return False

A = [1, 1, 2, 2]
assert MultipleOccurrencesInUnsortedList(A), "Should be True not False"

A = [1, 2, 3, 4]
assert not MultipleOccurrencesInUnsortedList(A), "Should be False not True"

# Exercise 7

# Modify the binary search algorithm so that if x is an element of A
# the algorithm returns the smallest index i of A such that A[i] = x. If x is not
# an element of A the algorithm should return -1.

def BinarySearchMinIndex(A, x):
  minInd = 0
  maxInd = len(A) - 1
  smallestInd = -1

  # >= so we don't skip mid value
  while maxInd >= minInd:
    midInd = (minInd + maxInd) // 2

    if A[midInd] == x and smallestInd == -1:
      smallestInd = midInd
    elif A[midInd] == x and midInd < smallestInd:
      smallestInd = midInd

    # We need to find the smallest index of X
    # This allow us to keep iterating in the left side of the list till we do
    # Or return the smallestInd or -1
    if x <= A[midInd]:
      maxInd = midInd - 1
    else:
      minInd = midInd + 1

  return smallestInd


A = [2, 3, 3, 3, 5, 2]
x = 3

assert BinarySearchMinIndex(A, x) == 1, "Should return 1"

A = [2, 3, 3, 5, 5, 2]
x = 5

assert BinarySearchMinIndex(A, x) == 3, "Should return 3"

A = [2, 3, 3, 5, 5, 2]
x = 1

assert BinarySearchMinIndex(A, x) == -1, "Should return -1"

# Exercise 8

# Rewrite the above algorithm under assumption that B is of length
# 1. The algorithm should work in O(1). In particular, the algorithm should not
# contain loops nor recursive calls.

def ContainsX(B, x):
  if B[0] == x:
    return True
  return False

# Exercise 9

# Design an O(log n) algorithm whose input is a sorted list A. The algorithm
# should return true if A contains at least 3 distinct elements. Otherwise,
# the algorithm should return false.

def BinaryDistinct(A):
  size = len(A)

  print(A)
  if A[0] == A[size - 1]:
    return False

  minind = 0
  maxind = size - 1

  mid = (minind + (maxind - minind)) // 2

  while mid != minind and mid != maxind:

    if A[mid] != A[minind] and A[mid] != A[maxind]:
      return True

    if A[mid] == A[minind]:
      minind = mid + 1
    else:
      maxind = mid - 1

    mid = (minind + (maxind - minind)) // 2

  return False


A = [1, 1, 2, 4, 5]

print(BinaryDistinct(A))

# Design an O(log n) algorithm whose input is a sorted list A. The algorithm
# should return true if A contains at least 4 distinct elements. Otherwise,
# the algorithm should return false. Hint: run the function for part 1 at
# most three times.

def Distinct4(A):
  distinct1 = BinaryDistinct(A)

  if not distinct1:
    return False
  
  mid = (len(A) - 1) // 2

  distinct2 = BinaryDistinct(A[:mid + 1])
  distinct3 = BinaryDistinct(A[mid:])

  if not distinct2 or not distinct3:
    return False
  
  return True

A = [1, 1, 2, 4, 5]
print(Distinct4(A))