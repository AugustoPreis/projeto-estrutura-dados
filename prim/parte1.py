from utils.generateArray import generateArray
from utils.calculateTime import calculateTime

from sorters.bubbleSort import bubbleSort
from sorters.insertionSort import insertionSort
from sorters.mergeSort import mergeSort
from sorters.quickSort import quickSort

array = generateArray(10000)

bubbleSortResult, bubbleSortTime = calculateTime(bubbleSort, array)
insertionSortResult, insertionSortTime = calculateTime(insertionSort, array)
mergeSortResult, mergeSortTime = calculateTime(mergeSort, array)
quickSortResult, quickSortTime = calculateTime(quickSort, array)

print(f'Bubble Sort: {bubbleSortTime}')
print(f'Insertion Sort: {insertionSortTime}')
print(f'Merge Sort: {mergeSortTime}')
print(f'Quick Sort: {quickSortTime}')