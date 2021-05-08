# Find if a list A contains repeated elements between 0 and len(A) - 1 or false otherwise in O(n) runtime.
def FindRepeatedElements(A):
  B = [0] * len(A)
  for i in range(0, len(A)):
    # If we found the repeated occurrence
    if B[A[i]] == 1:
      return True
    B[A[i]] += 1

  return False

A = [0, 1, 1, 3]
assert FindRepeatedElements(A), "Should be True"

# Find three consecutive numbers x, x + 1, x + 2 (i.e. 7, 8, 9) in list A
# The function must return true if the list contains 3 consecutive numbers or false otherwise.
def FindConsecutiveNumbers(A):
  B = [0] * len(A)

  for i in range(0, len(A)):
    B[A[i]] = 1

  for i in range(0, len(B) - 2):
    if B[i] > 0 and B[i + 1] > 0 and B[i + 2] > 0:
      return True

    return False


A = [0, 1, 1, 1, 0]
assert not FindConsecutiveNumbers(A), "Should be False"

A = [0, 3, 1, 1, 1, 2]
assert FindConsecutiveNumbers(A), "Should be True"


# Find middle vertex in a graph
# This is a vertex U that has distinct neighbours V and W such that there is no edge between V and W
# The function must return the list of all middle vertices

#     1 -- 3
#   / |    |
# 0   |    |
#   \ |    |
#     2 -- 4

def isMiddle(G, u):
  for v in range(0, len(G[u])):
    for w in range(v + 1, len(G[u])):
      if G[u][v] and G[u][w] and G[v][w] == 0:
        return True
  return False

def FindMiddleVertices(G):
  middle = []

  for u in range(0, len(G)):
    if (isMiddle(G, u)):
      middle.append(u)

  return middle

A = [
  [0, 1, 1, 0, 0],
  [1, 0, 1, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 0]
]

assert len(FindMiddleVertices(A)) == 4, "Length should be 4"

# Find the number of edges between middle vertices
def FindMiddleEdges(G):
  v = FindMiddleVertices(G)

  count = 0

  for i in range(0, len(v) - 1):
    for j in range(i + 1, len(v)):
      if G[v[i]][v[j]]:
        count += 1

  return count

A = [
  [0, 1, 1, 0, 0],
  [1, 0, 1, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 0]
]

assert FindMiddleEdges(A) == 4, "Should be 4"