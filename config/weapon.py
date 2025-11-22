from typing import NamedTuple
from config import EDiceConfig, DiceConfig

class WeaponStatsConfig(NamedTuple):
    name: str
    base_dice: int
    stat_mod: str
    weapon_range: int
    dice_config: DiceConfig = DiceConfig(sides=6, min_success=5)
    edice_config: EDiceConfig = EDiceConfig(dice_config=DiceConfig(sides=6, min_success=5), min_explode=6)
    auto: int = 1
    a_pen: int = 0
    base_edice: int = 0
    emp: int = 0
    svg: int = 0
    rsc: int = 0




