import random
from typing import List
from data.mdl import MultidimensionalList
from data.biome import Biome
from data.mob import Mob
from data.node import Node
from data.store import Store
from data.tree import Tree  

# Disposable alpha-version constants
MOB_LIMBS: int = 4
MOB_WEIGHT: int = 3
MOB_SIZE: int = 3
MOB_DIET: int = 1

class Mob_Controller:
  def __init__(self, mob_name: str, biome: Biome):
    #Arguments
    self._biome = biome
    self._store = Store('data/_settings.txt')
    self._mob_name = mob_name
    self._mob = Mob(self._mob_name, None, None, MOB_LIMBS, MOB_SIZE, MOB_WEIGHT, MOB_DIET, self._biome)
    #Limits
    self._fur_limit = self.init_fur_limit()  #*****
    self._weight_limit = None
    self._walk_type_limit = self.init_walk_type_limit() #***
    self._size_limit = None
    self._diet_limit = None
    #Mob related
    self._mob_fur = self.init_mob_fur()
    self._mob_walk_type = self.init_mob_walk_type()

  def get_mob(self) -> Mob:
    return self._mob
    
  #Limits depending on outer attributes
  def init_fur_limit(self) -> List[int]:
    fur_limit = []
    if self._biome.get_avr_temp() < 0:
      fur_limit = [3, 4]
    elif self._biome.get_avr_temp() >= 0 and self._biome.get_avr_temp() < 10:
      fur_limit = [2, 3, 4]
    elif self._biome.get_avr_temp() >= 10 and self._biome.get_avr_temp() < 20:
      fur_limit = [1, 2, 3]
    elif self._biome.get_avr_temp() >= 20 and self._biome.get_avr_temp() < 50:
      fur_limit = [0, 1]
    elif self._biome.get_avr_temp() >= 50:
      fur_limit = [0]
    return fur_limit

  #Mob parts depending on outer attributes
  def init_mob_fur(self) -> int:
    store: Tree = self._store.get_tree()
    fur_category: Node = store.find('Fur')
    fur_types = []
    pos_fur_types = []
    for son in fur_category.get_sons():
      fur_types = fur_types + [son.get_key()]
    for fur_type in fur_types:
      if fur_type in self._fur_limit:
        pos_fur_types = pos_fur_types + [fur_type]
    mob_fur = random.choice(pos_fur_types)
    return mob_fur

  #Builds a pre-inner-limits mob
  def build_pre_mob(self):
    self._mob = Mob(self._mob_name, self._mob_fur, None, MOB_LIMBS, MOB_SIZE, MOB_WEIGHT, MOB_DIET, self._biome)
    return self._mob

  #Limits depending on inner attributes
  def init_walk_type_limit(self) -> List[int]:
    walk_type_limit = []
    mob_limbs = self._mob.get_limbs()
    if mob_limbs == 0:
      walk_type_limit = [0, 1]
    if mob_limbs == 1:
      walk_type_limit = [2, 4]
    if mob_limbs >= 2 and mob_limbs <= 4:
      walk_type_limit = [2, 3, 4] 
    return walk_type_limit

  #Mob parts depending on outer attribute
  def init_mob_walk_type(self) -> int:
    store: Tree = self._store.get_tree()
    walk_category: Node = store.find('Walk_type')
    walk_types = []
    pos_walk_types = []
    for son in walk_category.get_sons():
      walk_types = walk_types + [son.get_key()]
    for walk_type in walk_types:
      if walk_type in self._walk_type_limit:
        pos_walk_types = pos_walk_types + [walk_type]
    mob_walk_type = random.choice(pos_walk_types)
    return mob_walk_type

  #Builds the final Mob
  def build_mob(self):
    self._mob = Mob(self._mob_name, self._mob_fur, self._mob_walk_type, MOB_LIMBS, MOB_SIZE, MOB_WEIGHT, MOB_DIET, self._biome)
    self._mob.print_mob()


