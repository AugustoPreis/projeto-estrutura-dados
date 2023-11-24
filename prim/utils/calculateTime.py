from time import time

def calculateTime(callback, array):
  start = time()
  result = callback(array.copy())
  end = time()

  return result, end - start