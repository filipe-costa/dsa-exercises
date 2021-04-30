import math

# Lists

# Exercise 1

# Suppose that SALARIES is a list of yearly salaries of employees
# working for some organizations. Write a function that computes the average
# salary of those employees that earn more than 30K per year.
def averageOver30K(A):
    total = 0
    numberOfEmployees = 0
    for i in range(0, len(A)):
        if A[i] > 30000: 
            total += A[i]
            numberOfEmployees += 1

    return total / numberOfEmployees

A = [30002, 30001]

assert averageOver30K(A), "Average is not over 30k"

# Exercise 2

# Write a function whose input is a list A and whose output is
# as follows.

  # If A contains an element greater than 20 then the function returns the
  # index of such an element. (In case there are several suitable elements
  # an arbitrary index can be returned).

  # Otherwise, the output is -1.
def findIndex(A):
    for i in range(0, len(A)):
        if A[i] > 20: 
            return i
    return -1

A = [1, 30, 20]
assert findIndex(A) > -1, "No element greater than 20"

A = [1, 10, 20]
assert findIndex(A) == -1, "Element greater than 20"

# Write a function whose input are two lists A and B of the same length.
# The program should return true if these two lists are equal (that A[i] = B[i]
# for each index i) and false otherwise.

# Assume both lists are sorted
def isEqual(A, B):
    for i in range(0, len(A)):
        if A[i] != B[i]:
            return False
    return True

A = [1, 2]
B = [1, 2]
assert isEqual(A, B), "Lists are not equal"

A = [1, 2]
B = [1, 3]
assert not isEqual(A, B), "Lists are equal"

# Exercise 3

# Write a function computing the smallest odd element of A.
def isOdd(n):
  return (n % 2 == 1)

def smallestOddElement(A):
    smallest = A[0]
    for i in range(1, len(A)):
        if A[i] < smallest and A[i] % 2 == 1:
            smallest = A[i]

    if not isOdd(smallest):
      return -1
    return smallest

A = [1, 3, 5, 7, 9, 11]
assert smallestOddElement(A) == 1, "Odd element is not 1"

A = [2, 4, 6, 8, 10, 12]
assert smallestOddElement(A) == -1, "No odd elements"


# Write a function computing the second largest element of A.
def secondLargest(A):
    largest = 0
    secondLargest = 0
    for i in range(0, len(A)):
        if A[i] > largest:
            secondLargest = largest
            largest = A[i]
        elif A[i] > secondLargest:
            secondLargest = A[i]
    return secondLargest

A = [1, 2, 3, 5, 10]
assert secondLargest(A) == 5, "Second Largest is not 5"

# Write a function computing an index of the largest element of A. If the
# largest element has several occurrences return the index of an arbitrary
# occurrence.
def largest(A):
    index = 0
    largest = A[0]
    for i in range(1, len(A)):
        if A[i] > largest:
            largest = A[i]
            index = i
    return index

A = [1, 2, 3, 10]
assert A[largest(A)] == 10, "Largest is not 10"

# Exercise 4
# The input of all the functions considered in this exercise are two
# lists SALARIES and GENDERS. The indices of these lists correspond to
# employees (you can think of the indices as IDs of employees). SALARIES[i] is
# the early salary of employee i. GENDERS[i] is the gender of employee i. In
# particular, GENDER[i] =0 F0 is employee i is female and GENDER[i] =0 M0
# if employee i is male.

# Write a program that returns tuple (FSAL;MSAL) that are respectively
# salaries of female and male employees.
def salaries(Salaries, Genders):
    maleSalaries = []
    femaleSalaries = []

    for i in range(0, len(Salaries)):
        if Genders[i] == 'F':
            femaleSalaries.append(Salaries[i])
        else:
            maleSalaries.append(Salaries[i])
    return [femaleSalaries, maleSalaries]

# Write a program that returns tuple (avf; avm) that are respective average
# salaries of female and male employees.
def averageSalaries(Salaries, Genders):
    maleSalariesTotal = 0
    femaleSalariesTotal = 0
    numberOfMaleEmployees = 0
    numberOfFemaleEmployees = 0

    for i in range(0, len(Salaries)):
        if Genders[i] == 'F':
            femaleSalariesTotal += Salaries[i]
            numberOfFemaleEmployees += 1
        else:
            maleSalariesTotal += Salaries[i]
            numberOfMaleEmployees += 1
    
    return [femaleSalariesTotal / numberOfFemaleEmployees, maleSalariesTotal / numberOfMaleEmployees]

# Write a program that returns tuple (maxf;maxm) that are respectively
# the largest salaries of female and make employees.
def largestSalaries(Salaries, Genders):
    largestMaleSalary = 0
    largestFemaleSalary = 0

    for i in range(0, len(Salaries)):
        if Genders[i] == 'F':
            if Salaries[i] > largestFemaleSalary:
                largestFemaleSalary = Salaries[i]
        else:
            if Salaries[i] > largestMaleSalary:
                largestMaleSalary = Salaries[i]
    
    return [largestFemaleSalary, largestMaleSalary]

print(largestSalaries([30000, 30000, 15000, 10000], ['M', 'F', 'F', 'M']))

# Exercise 5

# Write a function that returns true if there is a female and a male employees
# that receive the same salary and false otherwise.
def isDifferentGenders(gender_1, gender_2):
  return (gender_1 == 'F' and gender_2 == 'M') or (gender_1 == 'M' and gender_2 == 'F')

def isEqualSalary(salary_1, salary_2):
  return salary_1 == salary_2

def hasCommonElement(Salaries, Genders):
    for i in range(0, len(Salaries)):
        for j in range(1, len(Salaries)):
            # Only check for salaries differences if genders are different
            if isDifferentGenders(Genders[i], Genders[j]):
                if isEqualSalary(Salaries[i], Salaries[j]):
                    return True
    return False

assert hasCommonElement([30000, 30000, 15000, 10000], ['M', 'F', 'F', 'M']), "Doesn't have a common element"
assert not hasCommonElement([30000, 31000, 15000, 10000], ['M', 'F', 'F', 'M']), "Has common element"

# Exercise 6

# Write a function whose input are two lists A and B. The function
# returns true if each element of A occurs in B the same number of times as in
# A and false otherwise.
def countOcc(e, A):
  total = 0
  for i in range(0, len(A)):
    if A[i] == e:
      total += 1
  return total

def checkIfElementIsInListTwoxTimes(A, B):
    for i in range(0, len(A)):
      counterElementInA = countOcc(A[i], A)
      counterElementInB = countOcc(A[i], B)
      if counterElementInA != counterElementInB:
        return False
    return True

A = [1, 1, 3, 2, 5, 6]
B = [3, 2, 1, 1, 5, 6]

assert checkIfElementIsInListTwoxTimes(A, B), "Element count diverge"

A = [1, 1, 3, 2, 5, 6]
B = [3, 2, 1, 0, 5, 6]
assert not checkIfElementIsInListTwoxTimes(A, B), "Elements count is the same"
