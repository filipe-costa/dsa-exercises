# Recursion

# Exercise 1

# Write a recursive function that computes the factorial of n, that is
# the number 1  2  : : :  n.

# Without DP / Dictionary
def factorial(n):
  if n < 2:
    return 1
  return n * factorial(n - 1)

assert factorial(5) == 120, "Factorial of 5 does not equal 120"
assert factorial(10) == 3628800, "Factorial of 10 does not equal 3628800"

# with DP / Dictionary
dict = {}
def factorial(n):
  if n in dict:
    return dict[n]

  if n < 2:
    return 1
  
  val = n * factorial(n - 1)

  if val not in dict:
    dict[n] = val

  return val

assert factorial(5) == 120, "Factorial of 5 does not equal 120"
assert factorial(10) == 3628800, "Factorial of 10 does not equal 3628800"

# Exercise 2

# Write a recursive function that computes the sum of even
# elements of the given list.
def isEven(n):
  return n % 2 == 0

def SumEvenRec(A, n):
  total = 0

  if n >= 0:

    if isEven(A[n]):
      total += A[n]

    return total + SumEvenRec(A, n - 1)

  return total

A = [2, 3, 4, 9, 12, 14]

assert SumEvenRec(A, len(A) - 1) == 32, "Total sum is not 32"

# Write a recursive function that computes the amount of even elements in
# the given list.

def TotalEvenRec(A, n):
  total = 0

  if n >= 0:

    if isEven(A[n]):
      total += 1

    return total + TotalEvenRec(A, n - 1)

  return total

A = [2, 3, 4, 9, 12, 14]

assert TotalEvenRec(A, len(A) - 1) == 4, "Total sum is not 4"

# Exercise 3

# Write a recursive function that returns true if the given list A
# contains even numbers and false otherwise.

def ContainsEvenNumbers(A, n):
  if n >= 0:

    if isEven(A[n]):
      return True

    return TotalEvenRec(A, n - 1)

  return False
  
A = [2, 3, 4, 9, 12, 14]
assert ContainsEvenNumbers(A, len(A) - 1), "Does not contain even"

A = [1, 3, 5, 7, 9, 11]
assert not ContainsEvenNumbers(A, len(A) - 1), "Does contain even numbers"

# Exercise 4

# Design a recursive function that computes the index of a
# largest element of the given list A.

def LargestElementIndex(A, n, largest, index):

  if n >= 0:

    if A[n] > largest:
      largest = A[n]
      index = n

    return LargestElementIndex(A, n - 1, largest, index)
  return index

A = [2, 3, 4, 9, 12, 14]
assert LargestElementIndex(A, len(A) - 1, A[0], 0) == 5, "Largest element index is not 5"


# Design a recursive function that computes the largest even element of list
# A. If A does not contain even elements the function should return -1.

def LargestEvenElement(A, n, largest):
  if n >= 0:
    if A[n] > largest and isEven(A[n]):
      largest = A[n]
    return LargestEvenElement(A, n - 1, largest)

  if not isEven(largest):
    return -1
  return largest

A = [2, 3, 4, 9, 12, 14]
assert LargestEvenElement(A, len(A) - 1, A[0]), "Largest even element is not 14"

A = [1, 3, 5, 7, 9, 11]
assert LargestEvenElement(A, len(A) - 1, A[0]) == -1, "Contains even elements"

# Exercise 5

# Write a recursive function that computes the index of the second
# largest element of the given list A.

def SecondLargestRec(A, n, largest, secondLargest):
  if n >= 0:

    if A[n] > largest:
      secondLargest = largest
      largest = A[n]
    elif A[n] > secondLargest:
      secondLargest = A[n]

    return SecondLargestRec(A, n - 1, largest, secondLargest)
  
  return secondLargest

A = [1, 3, 5, 7, 9, 11]
assert SecondLargestRec(A, len(A) - 1, A[0], A[0]) == 9, "Second largest is not 9"

A = [1, 3, 12, 7, 9, 11]
assert SecondLargestRec(A, len(A) - 1, A[0], A[0]) == 11, "Second largest is not 11"

# Write a recursive function that computes the third largest element of the
# given list A.

def ThirdLargestRec(A, n, largest, secondLargest, thirdLargest):
  if n >= 0:

    if A[n] > largest:
      thirdLargest = secondLargest
      secondLargest = largest
      largest = A[n]
    elif A[n] > secondLargest:
      thirdLargest = secondLargest
      secondLargest = A[n]
    elif A[n] > thirdLargest:
      thirdLargest = A[n]

    return ThirdLargestRec(A, n - 1, largest, secondLargest, thirdLargest)
  
  return thirdLargest

A = [1, 3, 5, 7, 9, 11]
assert ThirdLargestRec(A, len(A) - 1, A[0], A[0], A[0]) == 7, "Third largest is not 7"
A = [1, 3, 12, 7, 9, 11]
assert ThirdLargestRec(A, len(A) - 1, A[0], A[0], A[0]) == 9, "Third largest is not 9"

# Exercise 6

# Write a recursive function that splits the SALARIES list into
# female and male salaries according to the gender indicator in the accompanying
# GENDERS list.

# Assume that the length for both lists are equal
def SplitSalariesList(Salaries, Genders, n, M_S = [], F_S = []):

  if n >= 0:
    if Genders[n] == 'F':
      F_S.append(Salaries[n])
    else:
      M_S.append(Salaries[n])

    return SplitSalariesList(Salaries, Genders, n - 1, M_S, F_S)
  
  return [M_S, F_S]

Salaries = [30000, 30000, 15000, 10000]
Genders = ['M', 'F', 'F', 'M']

print(SplitSalariesList(Salaries, Genders, len(Salaries) - 1))