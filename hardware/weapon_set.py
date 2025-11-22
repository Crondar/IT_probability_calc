from hardware import Weapon
from config import WeaponStatsConfig, MechStatsConfig


class WeaponSet:
    
    def __init__(self, weapon_list: list[WeaponStatsConfig], mech_stats: MechStatsConfig):
        self._weapons = []
        for weapon in weapon_list:
            self._weapons.append(Weapon(weapon, mech_stats))


