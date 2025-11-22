import random
from typing import override
from config.edice import EDiceConfig

from hardware.dice import Dice

class Edice(Dice):

    def __init__(self, config: EDiceConfig) -> None:
        self._config = config
        self._min_explode = self._config.min_explode
        super().__init__(self._config.dice_config)


    @override
    def get_successes(self) -> int:
        result = self.roll()
        if result >= self._min_explode:
            return 1 + self.get_successes()
        elif result >= self._config.min_success:
            return 1
        else:
            return 0
