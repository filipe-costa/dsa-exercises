# Week 10 / 11 -> Graphs

def BFS(L, x):
  labelled = [0] * len(L)
  labelled[x] = 1
  Component = [x]
  curindex = 0

  while(curindex < len(Component)):
    y = Component[curindex]
    z = L[y]

    for i in range(len(z)):
      if labelled[z[i]] == 0:
        labelled[z[i]] = 1
        Component.append(z[i])
        curindex = curindex + 1

    return Component

L = {
  0: [1, 2],
  1: [2, 3],
  2: [0, 1],
  3: [1, 0],
  4: [1, 3]
}

x = 2
print(BFS(L, x))
x = 4
print(BFS(L, x))