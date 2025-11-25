from config import *
from config.limb import LimbConfig
from config.weapon import WeaponStatsConfig
from config.mechstats import MechStatsConfig
from math_help import range
import weapons as wep


class MechConfig:

    def __init__(self):
        self.dice_config = dice.DiceConfig(sides=6, min_success=5)
        self.edice_config = edice.EDiceConfig(dice_config=self.dice_config, min_explode=6)

        self.mech_stats = MechStatsConfig(charge=10, base_evasion=4, reflex=9, intellect=1, endurance=3)
        self.rsc = 320
        self.emp_hardening = 2

        self.hit_location_dice_num = 3
        self.limbs = [
        LimbConfig(name= 'chassis',armor=4, ablative_armor=0, hp=5, hit_location_range=range.Range(9, 12)),
        LimbConfig(name= 'L leg',armor=2, hp=6, hit_location_range=range.Range(4,5)),
        LimbConfig(name= 'R arm',armor=4, hp=6, hit_location_range=range.Range(16,17)),
        LimbConfig(name= 'L arm',armor=4, hp=5, hit_location_range=range.Range(6,8)),
        LimbConfig(name= 'R leg',armor=2, hp=5, hit_location_range=range.Range(13,15)),
        LimbConfig(name= 'R shoulder',armor=0, hp=0, hit_location_range=range.Range(18,18)),
        LimbConfig(name= 'L shoulder',armor=0, hp=0, hit_location_range=range.Range(3, 3)),
        ]


        self.weapons = [wep.magnetic_anti_material_rifle] * 4 +[wep.rapid_fire_laser] * 12 + [wep.magnetic_auto_rifle] * 7
