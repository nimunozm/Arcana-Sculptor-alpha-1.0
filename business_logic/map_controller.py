import random
from data.mdl import MultidimensionalList

class MapController:
  def __init__(self, rows:int, columns:int) -> None:
    self._rows = rows
    self._columns = columns
    self._grid = self._generate_random_values()

  def get_grid(self) -> MultidimensionalList:
    return self._grid
    
  def generate_full_random_values(self):
    #Este método hizo parte del proceso de creación y diseño, sin embargo, no se utiliza
    grid = MultidimensionalList(self._rows, self._columns)

    for i in range(self._rows):
      for j in range(self._columns):
        value = random.randint(0, 1)
        grid.add(value, i, j)

    return grid

  def _generate_random_values(self):
    grid = MultidimensionalList(self._rows, self._columns)

    for i in range(self._rows):
      for j in range(self._columns):
        score = self.calculate_score(grid, i, j)
        # Generar un valor aleatorio basado en la puntuación
        value = random.choices([0, 1], weights=[score['0'], score['1']])[0]
        grid.add(value, i, j)

    return grid

  def calculate_score(self, grid, row, column):
    score = {'0': 1, '1': 1}  # Puntuaciones iniciales iguales

    # Calcular la cantidad de vecinos que tienen el mismo valor
    for i in range(row - 1, row + 2):
      for j in range(column - 1, column + 2):
        if 0 <= i < grid._rows and 0 <= j < grid._columns and (i != row or j != column):
          neighbor_value = str(grid._data[i][j])  # Convertir a cadena para usar como clave en el diccionario
          # Incrementar la puntuación si el vecino es 1
          if neighbor_value == '1':
            score['1'] += 4
          else:
            score['0'] += 1

    return score

  def count_adjacent_ones(self, row, column):
    count = 0
    for i in range(row - 1, row + 2):  
      for j in range(column - 1, column + 2):
        if 0 <= i < self._grid._rows and 0 <= j < self._grid._columns and (i != row or j != column):
          if self._grid._data[row][column] == 1 and self._grid._data[i][j] == 1:
            count += 1
          elif self._grid._data[row][column] == 0 and self._grid._data[i][j] == 0:
            count += 1
    return count

  def replace_less_than_4_black(self):
    for i in range(self._grid._rows):
      for j in range(self._grid._columns):
        if self._grid._data[i][j] == 1:
          count = self.count_adjacent_ones(i, j)
          if count < 4:
            self._grid._data[i][j] = 0

  def replace_less_than_4_white(self):
    for i in range(self._grid._rows):
      for j in range(self._grid._columns):
        if self._grid._data[i][j] == 0:
          count = self.count_adjacent_ones(i, j)
          if count < 4:
            self._grid._data[i][j] = 1

