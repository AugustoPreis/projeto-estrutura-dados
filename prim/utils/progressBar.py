from tqdm import tqdm

class ProgressBar:

  # Cria uma barra de progresso atualizavel
  def __init__(self, total = 100, initial = 0, desc = ''):
    self.bar = tqdm(
      total=total,
      initial=initial,
      desc=desc,
      colour='green',
      bar_format='{desc}{percentage:3.0f}% |{bar:30}|',
    )

  def reset(self):
    self.bar.reset()

  def update(self, value, desc = ''):
    self.bar.update(value)

    if (desc != ''):
      self.bar.set_description(desc)

  def end(self):
    self.bar.close()