import typing

class Biome:
  def __init__(self, name:str, altitude: typing.Sequence[float], resources_accessibility: float):
    self._name = name
    self._alt = altitude
    self._resources = resources_accessibility
    self._temp = self.init_temp()
    self._avr_temp = self.init_avr_temp()
    self._VD = self.init_VD()
    self._hum = self.init_hum()
    self._rel_hum = None

  def init_temp(self) -> typing.Sequence[float]:
    min_temp = 25 - (self._alt[1]/180)
    max_temp = 25 - (self._alt[0]/180)
    return (min_temp, max_temp)

  def init_avr_temp(self) -> float:
    min_temp = self._temp[0]
    max_temp = self._temp[1]
    avr_temp = (min_temp + max_temp) / 2
    return avr_temp

  def init_VD(self) -> typing.Sequence[float]:
    min_T = self._temp[0]
    max_T = self._temp[1]
    #min_VD
    VD1 = 5.018 + (0.32321*min_T) + ((8.1847*(10**-3))*(min_T**2)) + ((3.1243*(10**-4))*(min_T**3))
    VD2 = 6.335 + (0.6718*min_T) - ((2.0887*(10**-2))*(min_T**2)) + ((7.3095*(10**-4))*(min_T**3))
    min_VD = (VD1 + VD2) / 2
    #max_VD
    VD3 = 5.018 + (0.32321*max_T) + ((8.1847*(10**-3))*(max_T**2)) + ((3.1243*(10**-4))*(max_T**3))
    VD4 = 6.335 + (0.6718*max_T) - ((2.0887*(10**-2))*(max_T**2)) + ((7.3095*(10**-4))*(max_T**3))
    max_VD = (VD3 + VD4) / 2

    return (min_VD, max_VD)

  def init_hum(self) -> typing.Sequence[float]:
    max_hum = self._VD[1]
    return (0, max_hum)

  def init_rel_hum(self) -> typing.Sequence[float]:
    pass

  def get_temp(self) -> typing.Sequence[float]:
    return self._temp

  def get_avr_temp(self) -> float:
    return self._avr_temp

  def get_alt(self) -> typing.Sequence[float]:
    return self._alt

  def get_hum(self) -> typing.Sequence[int]:
    return self._hum

  def get_resources(self) -> float:
    return self._resources

  def set_temp(self, temperature) -> None:
    self._temp = temperature

  def set_alt(self, altitude) -> None:  
    self._alt = altitude

  def set_hum(self, humidity) -> None:
    self._hum = humidity

  def set_resources(self, resources_accessibility) -> None:
    self._resources = resources_accessibility

  def print_biome(self):
    print("Name: ", self._name)
    print("Altitude: ", self._alt)
    print("Temperature: ", self._temp)
    print("Average Temperature: ", self._avr_temp)
    print("Humidity: ", self._hum)
    print("Resources Accesibility: ", self._resources*100,"%")
    print("VD: ", self._VD)
    print("Rel_hum: ", self._rel_hum)

