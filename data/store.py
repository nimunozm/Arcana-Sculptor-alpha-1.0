from typing import List
from data.tree import Tree
from data.mdl import MultidimensionalList as MDL

MAX_CAT_PRODS = 8

class Store():
  def __init__(self, settings: str):
    self._settings = settings
    self._name = self.init_name()
    self._categories = self.init_categories()
    self._products = self.init_products()
    self._tree = self.build_Tree()

  def init_name(self) -> str:
    with open(self._settings, 'r') as file:
      name = file.readline().strip()
      return name

  def init_categories(self) -> List[str]:
    with open(self._settings, 'r') as file:
      # Leer la segunda línea
      next(file)
      second_line = file.readline().strip()
      # Dividir la línea en categorías usando ';' como separador
      categories = second_line.split(';')
      return categories

  def init_products(self) -> MDL:
    products = MDL(len(self._categories), MAX_CAT_PRODS)
    products1 = []
    with open(self._settings, 'r') as file:
      # Salta la primera línea (que contiene las categorías)
      next(file)
      next(file)

      row = 0
      for line in file:
        line = line.strip()
        if line:
          products_py_list = []
          products_py_list = [int(val) for val in line.split(';')]
          column = 0            
          for product in products_py_list:
            products.add(product, row, column)
            column += 1
          row += 1
    return products

  def build_Tree(self) -> Tree:
    tree = Tree(self._name)
    rows = self._products.get_rows()
    columns = self._products.get_columns()
    #Añado categorias
    for category in self._categories:
      tree.add_category(category)
    #Añado productos
    row = 0
    column = 0
    #Me vuelvo loco, no se ni como funciono esta madre, tuve que programar la subscriptibilidad de una clase!!! SABEN LO QUE ESO SIGNIFICA???? PORQUE YO TAMPOCO !!!!!!!!!!
    while row<rows:      
      if self._products[row, column] is not None:
        tree.add_product(self._products[row, column], tree.find(self._categories[row]))
      column += 1
      if column == columns:
        column = 0
        row += 1
    return tree

  def get_tree(self) -> Tree:
    return self._tree
