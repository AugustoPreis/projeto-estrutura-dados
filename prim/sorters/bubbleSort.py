# Percorre a lista diversas vezes, compara elementos adjacentes e os troca
# se estiverem na ordem errada. Esse processo é repetido até que a lista esteja ordenada.
def bubbleSort(arr):
  n = len(arr)

  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

  return arr