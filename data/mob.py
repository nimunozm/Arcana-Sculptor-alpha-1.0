import typing
import random
from data.biome import Biome

class Mob():
  def __init__(self, name:str, fur: typing.Union[int, None], walk_type: typing.Union[int, None], limbs: typing.Union[int, None], size: typing.Union[int, None], weight: typing.Union[int, None], diet: typing.Union[int, None], biome: Biome):
    self._fur = fur
    self._walk_type = walk_type
    self._limbs = limbs
    self._size = size
    self._weight = weight
    self._diet = diet
    self._biome = biome
    self._name = name

  def get_fur(self) -> int:
    return self._fur

  def get_walk_type(self) -> int:
    return self._walk_type

  def get_limbs(self) -> int:
    return self._limbs

  def get_size(self) -> int:
    return self._size

  def get_weight(self) -> int:
    return self._weight

  def get_diet(self) -> int:
    return self._diet

  def get_biome(self) -> int:
    return self._biome

  def set_fur(self, fur: int):
    self._fur = fur

  def set_walk_type(self, walk_type: int):
    self._walk_type = walk_type

  def set_limbs(self, limbs: int):
    self._limbs = limbs

  def set_size(self, size: int):
    self._size = size

  def set_weight(self, weight: int):
    self._weight = weight

  def set_diet(self, diet: int):
    self._diet =diet

  def assign_fur_str(self) -> str:
    my_str = ''
    if self._fur == 0:
      my_str = 'None'
    elif self._fur == 1:
      my_str = 'Almost_None'
    elif self._fur == 2:
      my_str = 'Thin'
    elif self._fur == 3:
      my_str = 'Moderate'
    elif self._fur == 4:
      my_str = 'Thick'
    elif self._fur == 5:
      my_str = 'Long and Thick :v'
    return my_str

  def assign_walk_type_str(self) -> str:
    my_str = ''
    if self._walk_type == 0:
      my_str = 'Roll'
    elif self._walk_type == 1:
      my_str = 'Rept'
    elif self._walk_type == 2:
      my_str = 'Crawl'
    elif self._walk_type == 3:
      my_str = 'Walk and Run'
    elif self._walk_type == 4:
      my_str = 'Jump'
    return my_str

  def assign_size_str(self) -> str:
    my_str = ''
    if self._size == 0:
      my_str = 'Insect-Size'
    elif self._size == 1:
      my_str = 'Tiny'
    elif self._size == 2:
      my_str = 'Small'
    elif self._size == 3:
      my_str = 'Medium'
    elif self._size == 4:
      my_str = 'Medium-Big'
    elif self._size == 5:
      my_str = 'Big'
    elif self._size == 6:
      my_str = 'Huge'
    elif self._size == 7:
      my_str = 'Monstrous'
    return my_str

  def assign_weight_str(self) -> str:
    my_str = ''
    if self._weight == 0:
      my_str = 'Aerogel-Light'
    elif self._weight == 1:
      my_str = 'Very Light'
    elif self._weight == 2:
      my_str = 'Light'
    elif self._weight == 3:
      my_str = 'Regular'
    elif self._weight == 4:
      my_str = 'Heavy'
    elif self._weight == 5:
      my_str = 'Very Heavy'
    elif self._weight == 6:
      my_str = 'Massive'
    elif self._weight == 7:
      my_str = 'Super Massive'
    return my_str

  def assign_diet_str(self) -> str:
    my_str = ''
    if self._diet == 0:
      my_str = 'Herbivorous'
    elif self._diet == 1:
      my_str = 'Carnivorous'
    elif self._diet == 2:
      my_str = 'Omnivorous'
    return my_str

  def print_mob(self):
    print("Name: ", self._name)
    print("Fur: ", self.assign_fur_str())
    print("Walk Type: ", self.assign_walk_type_str())
    print("Limbs: ", self.get_limbs())
    print("Size: ", self.assign_size_str())
    print("Weight: ", self.assign_weight_str())
    print("Diet: ", self.assign_diet_str())
