from typing import List
from data.biome import Biome

class UserInterface:
  def greeting(self):
    print("Bienvenido a Arcana Sculptor")
    print("-----------------------------------------")
  
  def menu(self) -> int:
    print("\n1. Generar un nuevo map de alturas")
    print("2. Crear plantilla de Bioma")
    print("3. Crear mob primitivo")
    print("4. Mirar biomas y mobs")
    print("5. Terminar Programa")
    while True:
      try:
          option:int = int(input("Ingrese el número de la opción: "))
          return option
      except ValueError:
          print("Error: Por favor, ingrese un número entero válido.")

  def get_map_size(self) -> tuple[int, int]:
    rows = int(input("\nIngrese el número de filas del mapa: "))
    columns = int(input("Ingrese el número de columnas del mapa: "))
    return rows, columns
  
  def map_menu(self) -> int:
    print('\n-----------------------------------------')
    print('Nuevo mapa generado')
    print('Da click en la pestaña \'Output\' para ver el mapa')
    print('>> Opciones')
    print("0. Volver al menú principal")
    print("1. Terminar Programa")
    while True:
      try:
          option = int(input("Ingrese el número de la opción: "))
          return option
      except ValueError:
          print("Error: Por favor, ingrese un número entero válido.")

  def get_biome_characteristics(self) -> tuple[str, tuple[float, float], float]:
    print("\nIngrese las características del bioma:")
    name:str = str(input("Nombre: "))
    min_alt:float = float(input("Altitud minima: "))
    max_alt:float = float(input("Altitud máxima: "))
    resources:float = float(input("Porcentaje de recursos accesibles: "))/100
    
    return name, (min_alt, max_alt), resources

  def keep_or_not(self) -> int:
    print('\n>> ¿Guardar?')
    print("1. Si")
    print("2. No")
    while True:
      try:
          option = int(input("Ingrese el número de la opción: "))
          return option
      except ValueError:
          print("Error: Por favor, ingrese un número entero válido.")
    
  def biome_menu(self) -> int:
    print('\n>> Opciones')
    print("0. Volver al menú principal")
    print("1. Ver todos los biomas")
    print("2. Terminar Programa")
    while True:
      try:
          option = int(input("Ingrese el número de la opción: "))
          return option
      except ValueError:
          print("Error: Por favor, ingrese un número entero válido.")

  def get_mod_info(self, biomes:List[Biome]) -> tuple[str, Biome]:
    name:str = str(input("\nIngrese el nombre quiere quiere poner: "))
    print("Biomas disponibles")
    i = 1
    for biome in biomes:
      print("\nBioma número " + str(i))
      biome.print_biome()
      i += 1
    while True:
      try:
        biome_num:int = int(input("Ingrese el número del bioma: "))
        op_biome = biomes[biome_num-1]
        return name, op_biome
      except ValueError:
          print("Error: Por favor, ingrese un número entero válido.")

  def mod_menu(self) -> int:
    print('\n>> Opciones')
    print("0. Volver al menú principal")
    print("1. Ver todos los mobs")
    print("2. Terminar Programa")
    while True:
      try:
          option = int(input("Ingrese el número de la opción: "))
          return option
      except ValueError:
          print("Error: Por favor, ingrese un número entero válido.")

  def look_menu(self) -> int:
    print('\n>> Opciones')
    print("0. Volver al menú principal")
    print("1. Terminar Programa")
    while True:
      try:
          option = int(input("Ingrese el número de la opción: "))
          return option
      except ValueError:
          print("Error: Por favor, ingrese un número entero válido.")

  def bye_bye(self) -> None:
    print('Gracias por usar Arcana Sculptor')