import typing
import numpy as np
import matplotlib.pyplot as plt


class MultidimensionalList:
  def __init__(self, rows:int, columns:int) -> None:
    self._rows = rows
    self._columns = columns
    self._data = [[0] * columns for _ in range(rows)]

  def add(self, value:int, row:int, column:int) -> None:
    if row < 0 or row >= self._rows or column < 0 or column >= self._columns:
        raise IndexError("Índices fuera de rango")
    self._data[row][column] = value

  def remove(self, row:int, column:int) -> None:
    if row < 0 or row >= self._rows or column < 0 or column >= self._columns:
        raise IndexError("Índices fuera de rango")
    self._data[row][column] = 0

  def to_numpy(self) -> np.ndarray:
    return np.array(self._data)

  def visualize_grid(self) -> None:
    grid_np = self.to_numpy()
    plt.imshow(grid_np, cmap='binary', interpolation='nearest')
    plt.show(block=False)

  def get_rows(self):
    return self._rows

  def get_columns(self):
    return self._columns

  def __iter__(self):
    for row in self._data:
      yield from row

  def __getitem__(self, key: typing.Tuple[int,int]):
    if isinstance(key, tuple):
      row, column = key
      if row < 0 or row >= self._rows or column < 0 or column >= self._columns:
        raise IndexError("Índice fuera de rango")
      return self._data[row][column]
    else:
      raise TypeError("Key must be a tuple (row, column)")

  def __str__(self) -> str:
      return '\n'.join([' '.join([str(item) for item in row]) for row in self._data])