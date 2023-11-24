# O Insertion Sort cria uma sequência ordenada de elementos um de cada vez,
# pegando um elemento da lista e colocando na posição correta.
def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = key

  return arr