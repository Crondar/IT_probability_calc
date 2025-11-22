from config import WeaponStatsConfig
from typing import NamedTuple

class WeaponSetConfig(NamedTuple):
    name: str
    weapons: list[WeaponStatsConfig]

