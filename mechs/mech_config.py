from config import *
from config.limb import LimbConfig
from config.weapon import WeaponConfig
from config.mechstats import MechStatsConfig
from math_help import range


class MechConfig:

    def __init__(self):
        self.dice_config = dice.DiceConfig(sides=6, min_success=5)
        self.edice_config = edice.EDiceConfig(dice_config=self.dice_config, min_explode=6)

        self.mech_stats = MechStatsConfig(charge=10, base_evasion=2, reflex=5, intelligence=1, endurance=2)

        self.emp_hardening = False

        self.hit_location_dice_num = 3
        self.limbs = [
        LimbConfig(name= 'chassis',armor=8, ablative_armor=0, hp=8, hit_location_range=range.Range(9, 12)),
        LimbConfig(name= 'L leg',armor=8, hp=6, hit_location_range=range.Range(4,5)),
        LimbConfig(name= 'R arm',armor=8, hp=6, hit_location_range=range.Range(16,17)),
        LimbConfig(name= 'L arm',armor=8, hp=5, hit_location_range=range.Range(6,8)),
        LimbConfig(name= 'R leg',armor=8, hp=5, hit_location_range=range.Range(13,15)),
        LimbConfig(name= 'R shoulder',armor=0, hp=0, hit_location_range=range.Range(18,18)),
        LimbConfig(name= 'L shoulder',armor=0, hp=0, hit_location_range=range.Range(3, 3)),
        ]

        self.weapon1 = WeaponConfig(a_pen=8, base_dice=4,
                                    stat_mod=self.mech_stats.reflex,
                                    dice_config = self.dice_config, edice_config=self.edice_config)

        self.drone = WeaponConfig(a_pen=0, base_dice=2, auto=3, stat_mod=self.mech_stats.reflex,
                                  dice_config = self.dice_config, edice_config=self.edice_config)

        self.small_drone = WeaponConfig(a_pen=0, base_dice=1, auto=3, stat_mod=self.mech_stats.reflex,
                                        dice_config = self.dice_config, edice_config=self.edice_config)


        self.weapon_set_dict = {
            'plasma lance': [
            self.weapon1,
            self.weapon1,
        ],
            'overdrive': [
                self.weapon1,
                self.weapon1,
                self.weapon1
        ],
            'drones': [
                self.drone,
                self.drone,
                self.drone,
                self.drone,
                self.drone,
                self.small_drone,
                self.small_drone,
                self.small_drone,
                self.small_drone,
                self.small_drone
            ]
        }
