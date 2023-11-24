import random

# Gera um array de números inteiros
# Utiliza o parametro "length" para definir o tamanho do array
def generateArray(length):
  return [random.randint(1, 1000) for _ in range(length)]