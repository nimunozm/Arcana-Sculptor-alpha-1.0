from typing import Union
from data.node import Node


class Tree:

  def __init__(self, root: str) -> None:
    self._root = Node(root, 0, None, [])

  def get_root(self) -> Node:
    return self._root

  def add_category(self, category: str) -> None:
    new_node = Node(category, 1, self._root, [])
    self._root.set_sons(self._root.get_sons() + [new_node])

  def add_product(self, product: int, category: Node) -> None:
    new_node = Node(product, 2, category, [])
    category.add_son(new_node)

  def find(self, key: Union[str, int]) -> Union[Node, None]:
    return self._find_recursive(key, self._root)

  def _find_recursive(self, key: Union[str, int],
                      current_node: Node) -> Union[Node, None]:
    if current_node.get_key() == key:
      return current_node

    for child in current_node.get_sons():
      found_node = self._find_recursive(key, child)
      if found_node:
        return found_node

    return None

  def print_tree(self) -> None:
    self._print_recursive(self._root, 0)

  def _print_recursive(self, node: Node, level: int) -> None:
    if node is None:
      return

    print("  " * level + str(node.get_key()))
    for child in node.get_sons():
      self._print_recursive(child, level + 1)
