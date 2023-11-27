import utils.console as console

from utils.generateArray import generateArray
from utils.calculateTime import calculateTime
from utils.progressBar import ProgressBar
from utils.table import table

from sorters.bubbleSort import bubbleSort
from sorters.insertionSort import insertionSort
from sorters.mergeSort import mergeSort
from sorters.quickSort import quickSort

array = generateArray(10000)
progressBar = ProgressBar()

progressBar.update(0, 'Executando bubble sort')
bubbleSortResult, bubbleSortTime = calculateTime(bubbleSort, array)

progressBar.update(25, 'Executando insertion sort')
insertionSortResult, insertionSortTime = calculateTime(insertionSort, array)

progressBar.update(50, 'Executando merge Sort')
mergeSortResult, mergeSortTime = calculateTime(mergeSort, array)

progressBar.update(75, 'Executando quick Sort')
quickSortResult, quickSortTime = calculateTime(quickSort, array)

progressBar.end()
console.clear()

table(
  ['Algoritmo', 'Tempo de execução'],
  [
    ['Bubble Sort', bubbleSortTime],
    ['Insertion Sort', insertionSortTime],
    ['Merge Sort', mergeSortTime],
    ['Quick Sort', quickSortTime],
  ],
)