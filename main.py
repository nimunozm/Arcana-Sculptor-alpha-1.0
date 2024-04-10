from business_logic.main_controller import MainController
from userInterface.user_interface import UserInterface

controller = MainController(UserInterface())
controller.run_programm()