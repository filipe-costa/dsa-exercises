# Exercise 1

# For the purpose of writing this program, you can use functions max(L) and min(L)
# that respectively return the largest and the smallest elements of a list L of integers.
# Let A be an nxn square matrix.
# For example, consider the 3x3 matrix below.
# [ [1,2,3],
# [5,3,4]
# [6,7,2]]

# (a) Write a program that computes the largest element of each row and then prints
# the smallest one of these largest elements.
# For example, these largest row elements of the above matrix are 3, 5, 7 and the
# smallest of them is obviously 3.

def SmallestLargestInRow(A):
  largest = []

  for i in range(0, len(A)):
    l = 0
    for j in range(0, len(A[i])):
      if A[i][j] > l:
        l = A[i][j]
    largest.append(l)

  return min(largest)

A = [
  [1,2,3],
  [5,3,4],
  [6,7,2]
]

print(SmallestLargestInRow(A), 3)

# (b) Write a program that computes the largest element of each column and then
# prints the smallest one out of these largest elements.
# For example, these largest column elements for the above matrix are 6, 7, 4 and
# the smallest is 4.

def SmallestLargestInCol(A):
  largest = []

  for j in range(0, len(A[0])):
    l = 0
    for i in range(0, len(A)):
      if A[i][j] > l:
        l = A[i][j]
  
    largest.append(l)
  return min(largest)

print(SmallestLargestInCol(A), 4)


# Exercise 2

# (a) Let A be a list sorted in the increasing order. Design an O(log n) algorithm that
# returns the following:
# 
#  If there is an element different from both the first and the last element of
#   A, return the index of this element in A. If there are several such elements,
#   any can be returned. For example if A = [1, 1, 2, 4, 5] then 2 and 3 are both
#   legitimate returned values.
# 
#  If A has no elements diferent from both the first and the last one then return -1.
#   Hint: this question is a minor modification of a question given in Coursework
#   2.

def FindMiddle(A):
  size = len(A)

  if A[0] == A[size - 1]:
    return -1

  first = 0
  last = size - 1

  # Avoid overflow if the search space is large
  mid = (first + (last - first)) // 2

  while mid != first and mid != last:
  
    if A[mid] != A[first] and A[mid] != A[last]:
      return mid
    
    if A[mid] == A[first]:
      first = mid + 1
    else:
      last = mid - 1

    mid = (first + (last - first)) // 2

  return -1

A = [1, 1, 2, 4, 5]

print(FindMiddle(A))

# (b) Design an algorithm returning 'YES' if A has 4 diferent elements and 'NO'
# otherwise.
# 
# Hint: It is possible to use the solution of part a) of this question as a function
# and to run this function at most three times.

def FindMiddleFour(A):
  mid = FindMiddle(A)

  if mid == -1:
    return "NO"

  mid1 = FindMiddle(A[:mid + 1])
  mid2 = FindMiddle(A[mid + 1:])

  if mid1 == -1 or mid2 == -1:
    return "NO"

  return "YES"

A = [1, 2, 3, 4, 5, 6]

print(FindMiddleFour(A))

# Exercise 4

# Let G be a graph on vertices 0, ..., n - 1. Let A be the adjacency matrix of G.

# (a) Design an algorithm whose input is A. The algorithm should print the maximum
# degree of a vertex of G.

def MaxGraphDegree(A):
  max = 0

  for i in range(0, len(A)):
    t = 0

    for j in range(0, len(A[i])):
      if A[i][j]:
        t += 1
  
    if t > max:
      max = t

  return max

# (b) A graph is regular if all its vertices have the same degree. Design an algorithm
# whose input is A. The algorithm should print 'YES' if G is regular and 'NO'
# otherwise.

def RegularGraph(A):
  deg = []

  for i in range(0, len(A)):
    t = 0
    for j in range(0, len(A[i])):
      if A[i][j]:
        t += 1

    deg.append(t)

  deg.sort()

  if deg[0] != deg[len(deg) - 1]:
    print("No")
  else:
    print("Yes")


# Exercise 5

# Let G be a graph on vertices 0, ... ,n -1. Let A be the adjacency matrix of G. Let
# S be a subset of vertices of G (treat it like a list all of whose elements are numbers
# between 0 and n - 1 without repetitions).

# (a) Write a program whose input is A and S. The program must print all the edges
# of the subgraph of G induced by S (to print an edge means to print both its
# ends).

def PrintEdges(A,S):

  for i in range(0, len(S) - 1):
    for j in range(i + 1, len(S)):
      end1 = S[i]
      end2 = S[j]
      if A[end1][end2]:
        print(f'{end1}--{end2}')
    

#    -- 1 -- 3 --
#  /              \
# 0                5
#  \              /
#    -- 2 -- 4 --

# Valid set:
# [3, 4, 5]

A = [
  [0, 1, 1, 0, 0, 0],
  [1, 0, 0, 1, 0, 0],
  [1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1],
  [0, 0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1, 0]
]

S = [0]
PrintEdges(A, S)

# (b) Let Connect be a function whose input is the adjacency matrix of a graph. The
# function returns true if the graph is connected and false otherwise. Use the
# function (you do not need to write its code just call it when needed) to design
# an algorithm whose input is A and S. The program should print 'YES' if the
# subgraph of G induced by S is connected and 'NO' otherwise.

def Connect(B): # BFS
  visited = [0] * len(B)
  q = [0]

  while (len(q) > 0):
    v = q.pop()
    visited[v] = 1

    for i in range(0, len(B)):
      print(B[v][i], i)
      if B[v][i] != 0 and not visited[i]:
        q.append(i)

  for i in range(0, len(visited)):
    if visited[i] == 0:
      return False
  
  return True

def ConnectedSubGraph(A, S):
  B = []

  for i in range(0, len(S)):
    end1 = S[i]
    rowB = []

    for j in range(0, len(S)):
      end2 = S[j]
      rowB.append(A[end1][end2])

    B.append(rowB) 


  if Connect(B): 
    print("Connected")
  else:
    print("Not Connected")

#    -- 1 -- 3 --
#  /              \
# 0                5
#  \              /
#    -- 2 -- 4 --

# Valid set:
# [3, 4, 5]
# [2, 4, 5]

# Invalid sets:
# [1, 2, 5]
# [0, 1, 4]

A = [
  [0, 1, 1, 0, 0, 0],
  [1, 0, 0, 1, 0, 0],
  [1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1],
  [0, 0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1, 0]
]

S = [2, 4, 5]

ConnectedSubGraph(A, S)