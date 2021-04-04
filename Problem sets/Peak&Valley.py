MAX_INT = 1 << 32


def getMinIdx(a, n, i, j, k):
  iVal = a[i] if i < n else MAX_INT
  jVal = a[j] if j < n else MAX_INT
  kVal = a[k] if k < n else MAX_INT

  minimum = min(iVal, min(jVal, kVal))
  if iVal == minimum:
    return i
  elif jVal == minimum:
    return j
  else:
    return k


def getPeaksAndValleys(a, n):
  idx = 1
  while idx < n:
    minIdx = getMinIdx(a, n, idx - 1, idx, idx + 1)
    if minIdx != idx:
      a[minIdx], a[idx] = a[idx], a[minIdx]
    idx += 2
  return a


def main():
  arr = [5, 3, 1, 2, 3]
  print(f'Input: {arr}')
  print(getPeaksAndValleys(arr, len(arr)))


if __name__ == '__main__':
  main()