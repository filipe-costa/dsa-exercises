# Sorting -> This is actually lecture/week 8

# swap to be used later
from week_3 import isEven

def swap(ls, i, j):
  tmp = ls[i]
  ls[i] = ls[j]
  ls[j] = tmp

# Exercise 1
# https://en.wikipedia.org/wiki/Selection_sort
# Let NAMES and AVERAGES be lists of the same length containing student names and their respective averages. Write a function that gets
# these two lists as input and print the student names and respective averages in
# the decreasing order of the averages.
def SortAndPrintStudentsByDecreaseAverageOrder(names, averages):
  size = len(averages)
  for i in range(0, size - 1):
    jMax = i

    for j in range(i + 1, size):
      avg = averages[j]
      # If current jth average is greater than the previous ith average, we found a new max
      if avg > averages[jMax]:
        jMax = j
    if jMax != i:
      swap(averages, i, jMax)
      swap(names, i, jMax)
  
  for i in range(size):
    print(f'{names[i]}: {averages[i]}')
  
  return (names, averages)

names = ["Ban", "Meliodas", "Escanor"]
averages = [99.91, 99.95, 100]
print("Before SortAndPrintStudentsByDecreaseAverageOrder: ", names, averages)
print("After SortAndPrintStudentsByDecreaseAverageOrder: ", SortAndPrintStudentsByDecreaseAverageOrder(names, averages))

# Exercise 2
# https://en.wikipedia.org/wiki/Selection_sort
# Write a function whose input is a matrix A. The function should
# output the indices of the rows of A ordered by the increasing order of sums of
# the respective rows.

# O(n^2)
def SortBySumOrder(A):
  # O(n)
  idxs = [i for i in range(len(A))]
  size = len(A)

  # Modified Selection Sort
  for i in range(0, size - 1):
    curr_sum = sum(A[i])
    min_sum = curr_sum
    jMin = i

    for j in range(i + 1, size):
      tmp_sum = sum(A[j])
      if tmp_sum < min_sum:
        min_sum = tmp_sum
        jMin = j

    if min_sum != curr_sum:
      swap(idxs, i, jMin)

  return idxs

A = [
  [1, 2, 3],
  [4, 5, 6],
  [1, 2, 4]
]
# output: [0, 2, 1]
print("Before SortBySumOrder", A)
print("After SortBySumOrder", SortBySumOrder(A), [0, 2, 1])


# Exercise 3
# Write an algorithm that returns a list B such that each number occurring in A occurs in B exactly once. The numbers can appear in B
# in an arbitrary order. For the example above,the output can be [7, 2, 1, 9, 5].
def CreateSet(A):
  dict = {}
  B = []
  size = len(A)

  for i in range(size):
    if A[i] not in dict:
      dict[A[i]] = 1
      B.append(A[i])
  return B

A = [7, 7, 2, 2, 2, 1, 1, 9, 9, 5, 5, 5, 5]
print("Before CreateSet", A)
print("After CreateSet", CreateSet(A))

# Write an algorithm that returns a list C that is a permutation of the
# elements of B so that they are sorted according to the following criterion.
# B[i] occurs C before B[j] if
# 
#  The number of rows in A containing an occurrence of B[i] is greater
#   than the number of rows in A containing an occurrence of B[j] or
# 
#  The number of rows in A containing an occurrence of B[i] is the same
#   as that of B[j] but B[i] < B[j].
# 
# For A and B as in the examples in the previous two parts, C = [2, 5, 7, 1, 9].
def CreateSetFromMatrix(A):
  dict = {}
  B = []

  for i in range(0, len(A)):
    for j in range(0, len(A[i])):
      if A[i][j] not in dict:
        dict[A[i][j]] = 1
        B.append(A[i][j])

  return B

def CountDict(A):
  d = {}

  for i in range(0, len(A)):
    for j in range(0, len(A[i])):
      if A[i][j] not in d:
        d[A[i][j]] = 1
      else:
        d[A[i][j]] = d[A[i][j]] + 1

  return d

def ShouldPermute(el1, el2, counter_dict):
  if counter_dict[el1]>counter_dict[el2]:
    return True
  if counter_dict[el1]==counter_dict[el2] and el1<el2:
    return True
  return False


def Permutation(A, B):
  size = len(B)
  counter_dict = CountDict(A)

  for i in range(0, size - 1):
    minIdx = i

    for j in range(i + 1, size):

      if not ShouldPermute(B[minIdx], B[j], counter_dict):
        minIdx = j

    if minIdx != i:
      swap(B, i, minIdx)

  return B

A = [
  [7, 2, 1],
  [9, 2, 5],
  [7, 5, 2]
]

print("Before Permutation: ", CreateSetFromMatrix(A))
print("After Permutation: ", Permutation(A, CreateSetFromMatrix(A)))

# Exercise 4

# Write a function that reorders the elements of the input list A
# (we assume that A has not multiple occurrences) according to the following
# principle.
#  All the even numbers occur before all the odd numbers.
#  The even numbers are ordered in the increasing order.
#  The odd numbers are ordered in exactly the same order as in A.
# For example, if A = [2, 1, 5, 3, 8, 4] then after the 'sorting' A must be
# [2, 4, 8, 1, 5, 3].

# O(n)
def EvenOddList(A):
  even = []
  odd = []

  for i in range(len(A)):
    if isEven(A[i]):
      even.append(A[i])
    else: 
      odd.append(A[i])

  even.sort() # sort in place

  return [*even, *odd]

A = [2, 1, 5, 3, 8, 4]
print("Before EvenOddList: ", A)
print("After EvenOddList: ", EvenOddList(A))


# Write a function with the same input A as in the previous part. The
# function should permute elements of A according to the following principle.
#  All the even numbers are ordered by the increasing order.
#  All the odd numbers are ordered by the increasing order.
#  After the permutation, each element A[i] retains its parity. That is
# if A[i] is even in the beginning it remains even after the permutation
# and an odd element remains odd.

# O(n)
def EvenOddListParity(A):
  size = len(A)
  l = [0] * size
  evenIdxs = []
  oddIdxs = []

  for i in range(size):
    if isEven(A[i]):
      evenIdxs.append(i)
    else:
      oddIdxs.append(i)

  
  A.sort()  # sort all of them O(n)
  
  # keep track of index for each array of idxs
  j = 0
  # append 
  for i in range(size):
    if isEven(A[i]):
      l[evenIdxs[j]] = A[i]
      j += 1

  # Reset J
  j = 0
  for i in range(size):
    if not isEven(A[i]):
      l[oddIdxs[j]] = A[i]
      j += 1

  return l

A = [2, 1, 5, 3, 8, 4]
print("Before EvenOddListParity: ", A)
print("After EvenOddListParity: ", EvenOddListParity(A))

def EvenAhead(a, b):
  return (isEven(a) and isEven(b) and a<b)

def OddAhead(a, b):
  return (not isEven(a) and not isEven(b) and a<b)

def SelSortEvenOddListParity(A):
  size = len(A)
  for i in range(0, size - 1):
    jMin = i

    for j in range(i + 1, size):
      n = A[j]
  
      if EvenAhead(n, A[jMin]) or OddAhead(n, A[jMin]):
        jMin = j
    
    if jMin != i:
      swap(A, i, jMin)

  return A

A = [2, 1, 5, 3, 8, 4]
print("Before SelSortEvenOddListParity: ", A)
print("After SelSortEvenOddListParity: ", SelSortEvenOddListParity(A))

# Solve the problem as in the second part of this exercise by substituting
# a suitable sorting criterion to SelSortGen function.

def SortCrit(a, b):
  return EvenAhead(a, b) or OddAhead(a, b)

def SelSortGen(A, cb):
  size = len(A)
  for i in range(0, size - 1):
    jMin = i

    for j in range(i + 1, size):
      n = A[j]
  
      if cb(n, A[jMin]):
        jMin = j
    
    if jMin != i:
      swap(A, i, jMin)

  return A

A = [2, 1, 5, 3, 8, 4]
print("Before SelSortGen Sort Parity: ", A)
print("After SelSortGen Sort Parity: ", SelSortGen(A, SortCrit))

# Exercise 5 -> Theoretical tracing by hand of Insertion and Selection Sort algorithms -> skip;


# Exercise 6
# https://en.wikipedia.org/wiki/Insertion_sort
# Write a function InsertSortGen(A; sortcrit) that applies insertion Sort on A according to the sorting criterion as specified by function sortcrit.
def EvenAhead(a, b):
  return a%2 < b%2 or (isEven(a) and isEven(b) and a<b)

def OddAhead(a, b):
  return a%2 < b%2 or (not isEven(a) and not isEven(b) and a<b)

def InsertSortGen(A, cb):
  i = 1
  while i < len(A):
    x = A[i]
    j = i - 1

    while j >= 0 and cb(x, A[j]):
      A[j + 1] = A[j]
      j -= 1
    
    A[j+1] = x
    i += 1
  
  return A

A = [2, 1, 5, 3, 8, 4]
print("Before InsertSortGen: ", A)
print("After InsertSortGen using Even function cb: ", InsertSortGen(A, EvenAhead))

A = [2, 1, 5, 3, 8, 4]
print("Before InsertSortGen: ", A)
print("After InsertSortGen using Odd function cb: ", InsertSortGen(A, OddAhead))