# Escolhe um elemento como pivô e particiona a lista ao redor do pivô,
# colocando os elementos menores à esquerda e os elementos maiores à direita.
# Esse processo é então aplicado recursivamente às sublistas.
def quickSort(arr):
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr[0]
    lesser = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quickSort(lesser) + [pivot] + quickSort(greater)