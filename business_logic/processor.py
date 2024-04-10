from data.biome import Biome
from business_logic.mob_controller import Mob_Controller

# Disposable alpha-version constants
MOB_NAME: str = "Nof"
BIOME: Biome = Biome('Forest',(2000, 3500), 0.8)

class Processor:
  def __init__(self):
    controller = Mob_Controller(MOB_NAME, BIOME)
    controller.build_pre_mob()
    controller.build_mob()