import math
import os
NT_MAX = 15
PATH=".data.csv"

def evaluateTables(np, save=False):
  NT = None
  NT_BUSY, NT_FREE = loadDataTables()
  if np <= 6:
    NT = math.ceil(np/3)
  else:
    if np % 2 != 0:
      NT = math.floor(np/2)
    else: 
      NT = (np/2) -1
  NT_BUSY = NT_BUSY + NT
  NT_FREE = NT_MAX - NT_BUSY
  if save:
    saveDataTables(NT_BUSY, NT_FREE)
  return (NT_BUSY, NT_FREE)

def fileExist():
  if not os.path.exists(PATH):
    saveDataTables(0, 15)


def loadDataTables():
  fileExist()
  NT_BUSY = None
  NT_FREE = None
  with open(PATH) as f:
    values = f.readlines()[0].split(",")
    NT_BUSY = int(values[0])
    NT_FREE = int(values[1])
  return (NT_BUSY, NT_FREE)

def saveDataTables(NT_BUSY, NT_FREE):
  with open(PATH, 'w') as f:
      f.write("{},{}".format(NT_BUSY, NT_FREE))

# np = int(input())
# result = evaluateTables(np)
# print(result)