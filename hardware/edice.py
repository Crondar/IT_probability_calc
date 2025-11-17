import random
from typing import override
from config.edice import EDiceConfig

from hardware.dice import Dice

# config1=EDiceConfig(
#     min_explode=6, dice_config=DiceConfig(sides=6, min_success=5))
# i = config1.min_explode


class Edice(Dice):

    def __init__(self, config = EDiceConfig) -> None:
        self._config = config
        super().__init__(self._config)

    @override
    def get_successes(self) -> int:
        result = self.roll()
        if result >= self._config.min_explode:
            return 1 + self.get_successes()
        elif result >= self._config.min_success:
            return 1
        else:
            return 0
