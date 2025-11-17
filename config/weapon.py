from typing import NamedTuple
from config import EDiceConfig, DiceConfig

class WeaponConfig(NamedTuple):
    base_dice: int
    stat_mod: int
    dice_config: DiceConfig
    edice_config: EDiceConfig
    auto: int = 1
    a_pen: int = 0
    base_edice: int = 0



