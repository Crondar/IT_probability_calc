from typing import NamedTuple
from config.dice import DiceConfig


class EDiceConfig(NamedTuple):
    min_explode: int
    dice_config: DiceConfig