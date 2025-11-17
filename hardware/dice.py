import random
from config.dice import *


class Dice:

    def __init__(self, config: DiceConfig) -> None:
        self._config = config

    def get_successes(self) -> int:
        if self.roll() >= self._config.min_success:
            return 1
        else:
            return 0

    def roll(self) -> int:
        return random.randint(1,self._config.sides)