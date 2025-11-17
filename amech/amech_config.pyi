from hardware import edice
from config import *
from abc import ABC

class AMechConfig(ABC):

    def __init__(self):
        self.dice_config: dice.DiceConfig
        self.edice_config: edice.EDiceConfig