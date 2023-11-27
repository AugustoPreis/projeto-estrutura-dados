from tabulate import tabulate

# Cria uma tabela com os dados informados
def table(headers, data):
  content = tabulate(data, headers=headers)

  print(content)