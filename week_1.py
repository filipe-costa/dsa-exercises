import math

# Lists

# 1. Summing and counting

# Compute the average salary of those employees that earn more than 30K per year
def averageOver30K(A):
    total = 0
    numberOfEmployees = 0
    for i in range(0, len(A)):
        if A[i] > 30000: 
            total += A[i]
            numberOfEmployees += 1

    return total / numberOfEmployees

# Get element index
def findIndex(A):
    for i in range(0, len(A)):
        if A[i] > 20: 
            return i
    return -1

# 2. Existence Checking

# Compare lists for equality, assume both are same len
def isEqual(A, B):
    for i in range(0, len(A)):
        if A[i] != B[i]:
            return False
    return True

# 3. Smallest and largest elements

# Get the smallest odd element of A
def smallestOddElement(A):
    element = math.inf
    for i in range(0, len(A)):
        if A[i] < element and A[i] % 2 == 1:
            element = A[i]
    return smallestOddElement

# Compute the second largest element of A, assume that given {2, 2, 1} second largest is 2
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

# Find the largest element of A
def largest(A):
    largest = 0
    for i in range(0, len(A)):
        if A[i] > 0:
            largest = A[i]
    return largest


# 4. Sublists of the given list

# Create tuple of salaries for male and female employees
def salaries(Salaries, Genders):
    maleSalaries = []
    femaleSalaries = []

    for i in range(0, len(Salaries)):
        if Genders[i] == 'F':
            femaleSalaries.append(Salaries[i])
        else:
            maleSalaries.append(Salaries[i])
    return [femaleSalaries, maleSalaries]

# Create tuple of average salaries for male and female employees
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

# Create tuple of average salaries for male and female employees
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

# 5. Nested loops

# Check if male and female employees have salaries in common
def hasCommonElement(Salaries, Genders):
    for i in range(0, len(Salaries)):
        for j in range(1, len(Salaries)):
            # Only check for salaries differences if genders are different
            if Genders[i] == 'F' and Genders[j] == 'M':
                if Salaries[i] == Salaries[j]:
                    return True
    return False

# 6.

# Check if an element in list 1 occurs in list 2 the same number of times as in A, assume both lists are the same length

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

print(checkIfElementIsInListTwoxTimes(A, B))