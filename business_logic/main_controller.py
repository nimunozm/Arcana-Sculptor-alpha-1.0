from business_logic.map_controller import MapController
from business_logic.mob_controller import Mob_Controller
from data.biome import Biome
from data.store import Store
from userInterface.user_interface import UserInterface as u_i


class MainController:
  def __init__(self, ui):
    self._ui : u_i = ui
    
  def run_programm(self):
    running = True
    store = Store('data/_settings.txt')
    store.get_tree()
    self._ui.greeting()
    biomes:list = []
    mobs:list = []
    while running:
      option:int = self._ui.menu()
      
      if option == 1:
        rows, columns = self._ui.get_map_size()
        grid = MapController(rows, columns)
        grid.replace_less_than_4_black()
        grid.replace_less_than_4_white()
        print('-----------------------------------------')
        print('Estamos trabajando...')
        grid.get_grid().visualize_grid()
        print('Hemos termiando')
        op_map:int = self._ui.map_menu()
        if op_map == 1:
          running = False
          
      elif option == 2:
        charac_bio:tuple = self._ui.get_biome_characteristics()
        biome = Biome(*charac_bio)
        print('-----------------------------------------')
        print('Nuevo bioma generado')
        biome.print_biome()
        op_bio_keep:int = self._ui.keep_or_not()
        
        if op_bio_keep == 1:
          biomes += [biome]
          print("Bioma agregado")
          
        op_bio_menu:int = self._ui.biome_menu()
        if op_bio_menu == 1:
          for i in biomes:
            print('\n')
            i.print_biome()
            
        if op_bio_menu == 2:
          running = False

      elif option == 3:
        charac_mob = self._ui.get_mod_info(biomes)
        mob_controller = Mob_Controller(*charac_mob)        
        mob_controller.build_pre_mob()
        print('-----------------------------------------')
        print('Nuevo bioma generado')
        mob_controller.build_mob()
        op_mob_keep:int = self._ui.keep_or_not()
        if op_mob_keep == 1:
          mobs += [mob_controller.get_mob()]
          print("Mob agregado")

        op_mob_menu:int = self._ui.mod_menu()
        if op_mob_menu == 1:
          for i in mobs:
            print('\n')
            i.print_mob()

        if op_mob_menu == 2:
          running = False

      elif option == 4:
        print("\nBiomas:")
        for i in biomes:
          i.print_biome()
          
        print("\nMobs:")
        for j in mobs:
          j.print_mob()

        op_look = self._ui.look_menu()
        if op_look == 1:
          running = False
          

      elif option == 5:
        running = False
          
    self._ui.bye_bye()
      