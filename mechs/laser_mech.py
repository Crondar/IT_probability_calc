from config import *
from config.limb import LimbConfig
from config.weapon import WeaponStatsConfig
from config.mechstats import MechStatsConfig
from math_help import range


class MechConfig:

    def __init__(self):
        self.dice_config = dice.DiceConfig(sides=6, min_success=5)
        self.edice_config = edice.EDiceConfig(dice_config=self.dice_config, min_explode=6)

        self.mech_stats = MechStatsConfig(charge=16, base_evasion=2, reflex=4, intelligence=2, endurance=2)

        self.emp_hardening = 2

        self.hit_location_dice_num = 3
        self.limbs = [
        LimbConfig(name= 'chassis',armor=12, ablative_armor=0, hp=8, hit_location_range=range.Range(9, 12)),
        LimbConfig(name= 'L leg',armor=8, hp=6, hit_location_range=range.Range(4,5)),
        LimbConfig(name= 'R arm',armor=8, hp=6, hit_location_range=range.Range(16,17)),
        LimbConfig(name= 'L arm',armor=8, hp=5, hit_location_range=range.Range(6,8)),
        LimbConfig(name= 'R leg',armor=8, hp=5, hit_location_range=range.Range(13,15)),
        LimbConfig(name= 'R shoulder',armor=0, hp=3, hit_location_range=range.Range(18,18)),
        LimbConfig(name= 'L shoulder',armor=0, hp=0, hit_location_range=range.Range(3, 3)),
        ]

        self.rf_laser = WeaponStatsConfig(a_pen=0, base_dice=2, auto=4,
                                          stat_mod=self.mech_stats.reflex,
                                          dice_config = self.dice_config, edice_config=self.edice_config)


        self.weapon_set_dict = {
            'laser': [
            self.rf_laser,
            self.rf_laser,
            self.rf_laser,
        ],
        'overdrive': [
            self.rf_laser,
            self.rf_laser,
            self.rf_laser,
            self.rf_laser,
        ]
        }
