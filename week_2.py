
# Exercise 1

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

def isInRow(v, A, j):
  # Checks if the next item in the row is the same
  for k in range(j + 1, len(A)):
    if v == A[k]:
      return True
    
  return False

def isInColumn(v, A, j, i):
  # Checks the next row in the list, so we don't compare the same values
  for k in range(i + 1, len(A)):
    # Checks if value corresponds to the value at column j in row k
    if v == A[k][j]:
      return True

  return False

def isRepeated(A):
  for i in range(0, len(A)):
    for j in range(0, len(A[i])):
      if isInRow(A[i][j], A[i], j) and isInColumn(A[i][j], A, j, i):
        return False
  return True

print(isRepeated(A))
print(isRepeated(B))

# Exercise 2

marks = [
  [40, 40, 40, 40, 20],
  [50, 60, 20, 10, 20],
  [20, 40, 20, 30, 30],
  [20, 20, 30, 20, 20]
]

# 1

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

# 2

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

# Exercise 4

# Exercise 5

# Exercise 6
