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