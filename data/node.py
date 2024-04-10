import typing

class Node:
  def __init__(self, key: typing.Union[int, str], level: int, parent: typing.Optional['Node'] = None, sons: typing.List['Node'] = []):
    self._key = key
    self._level = level
    self._parent = parent
    self._sons = sons


  def get_key(self) -> typing.Union[int, str]:
    return self._key

  def get_parent(self) -> typing.Optional['Node']:
    return self._parent

  def get_sons(self) -> typing.List['Node']:
    return self._sons

  def get_level(self) -> int:
    return self._level

  def set_key(self, key: typing.Union[int, str]) -> None:
    self._key = key

  def set_parent(self, parent: 'Node') -> None:
    self._parent = parent

  def set_sons(self, sons: typing.List['Node']) -> None:
    self._sons = sons

  def add_son(self, son: 'Node') -> None:
    self._sons += [son]  