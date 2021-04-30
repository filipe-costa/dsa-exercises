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

# Let A and B be list of integers such that the elements of A are in the
# range 0, ..., len(A) - 1 while the elements of B are just arbitrary integers.
# design a linear time algorithm checking whether

# Exercise 7

# Modify the binary search algorithm so that if x is an element of A
# the algorithm returns the smallest index i of A such that A[i] = x. If x is not
# an element of A the algorithm should return -1.

# Exercise 8

# Rewrite the above algorithm under assumption that B is of length
# 1. The algorithm should work in O(1). In particular, the algorithm should not
# contain loops nor recursive calls.

# Exercise 9

# Design an O(log n) algorithm whose input is a sorted list A. The algorithm
# should return true if A contains at least 3 distinct elements. Otherwise,
# the algorithm should return false.

# Design an O(log n) algorithm whose input is a sorted list A. The algorithm
# should return true if A contains at least 4 distinct elements. Otherwise,
# the algorithm should return false. Hint: run the function for part 1 at
# most three times.