from config import *
from config.limb import LimbConfig
from config.weapon import WeaponStatsConfig
from config.mechstats import MechStatsConfig
from math_help import range
import weapons


class MechConfig:

    def __init__(self):
        self.dice_config = dice.DiceConfig(sides=6, min_success=5)
        self.edice_config = edice.EDiceConfig(dice_config=self.dice_config, min_explode=6)

        self.mech_stats = MechStatsConfig(charge=10, base_evasion=1, reflex=4, intellect=1, endurance=3)
        self.rsc = 320
        self.emp_hardening = 2

        self.hit_location_dice_num = 3
        self.limbs = [
        LimbConfig(name='chassis', armor=8, ablative_armor=0, hp=7, hit_location_range=range.Range(9, 12)),
        LimbConfig(name='L leg', armor=6, hp=3, hit_location_range=range.Range(4, 5)),
        LimbConfig(name='R arm', armor=6, hp=4, hit_location_range=range.Range(16, 17)),
        LimbConfig(name='L arm', armor=6, hp=6, hit_location_range=range.Range(6, 8)),
        LimbConfig(name='R leg', armor=6, hp=3, hit_location_range=range.Range(13, 15)),
        LimbConfig(name='R shoulder', armor=0, hp=0, hit_location_range=range.Range(18, 18)),
        LimbConfig(name='L shoulder', armor=0, hp=0, hit_location_range=range.Range(3, 3)),
        ]



        self.weapons = [
            weapons.magnetic_sniper_rifle,
            weapons.magnetic_sniper_rifle,
            weapons.magnetic_sniper_rifle,
            weapons.magnetic_sniper_rifle,
            weapons.magnetic_sniper_rifle,
            weapons.magnetic_sniper_rifle,
            weapons.magnetic_auto_rifle,
            weapons.magnetic_auto_rifle,
            weapons.magnetic_anti_material_rifle,
            weapons.magnetic_anti_material_rifle,
            weapons.magnetic_anti_material_rifle,
            weapons.magnetic_anti_material_rifle,
        ]

        # self.weapon1 = WeaponStatsConfig(a_pen=8, base_dice=4,
        #                                  stat_mod=self.mech_stats.reflex,
        #                                  dice_config = self.dice_config, edice_config=self.edice_config)
        #
        # self.drone = WeaponStatsConfig(a_pen=0, base_dice=0, auto=4, stat_mod=self.mech_stats.reflex,
        #                                dice_config = self.dice_config, edice_config=self.edice_config)
        #
        # self.small_drone = WeaponStatsConfig(a_pen=1, base_dice=0, auto=3, stat_mod=self.mech_stats.reflex,
        #                                      dice_config = self.dice_config, edice_config=self.edice_config)
        #
        # self.infantry = WeaponStatsConfig(a_pen=0, base_dice=1, auto=216, stat_mod=self.mech_stats.reflex,
        #                                   dice_config = self.dice_config, edice_config=self.edice_config)
        # self.gyro = WeaponStatsConfig(a_pen=0, base_dice=8, auto=5, stat_mod=self.mech_stats.reflex,
        #                               dice_config = self.dice_config, edice_config=self.edice_config)
        # self.gyro_drone = WeaponStatsConfig(a_pen=0, base_dice=8, auto=3, stat_mod=self.mech_stats.endurance,
        #                                     dice_config = self.dice_config, edice_config=self.edice_config)
        # self.amatter = WeaponStatsConfig(a_pen=5, base_dice=8, auto=4, stat_mod=self.mech_stats.reflex,
        #                                  dice_config = self.dice_config, edice_config=self.edice_config)
        # self.rf = WeaponStatsConfig(a_pen=0, base_dice=0, auto=24, stat_mod=self.mech_stats.reflex,
        #                             dice_config = self.dice_config, edice_config=self.edice_config)


        # self.weapon_set_dict = { #will take {'name': WeaponSet}

        #     'plasma lance': [
        #     self.weapon1,
        #     self.weapon1,
        # ],
        #     'overdrive': [
        #         self.weapon1,
        #         self.weapon1,
        #         self.weapon1
        # ],
        # 'drones': [
        #         self.drone,
        #         self.drone,
        #         self.drone,
        #         self.drone,
        #         self.drone,
        #         self.drone,
        #         self.drone,
        #         self.drone,
        #         self.drone,
        #         self.drone,
        #         self.drone,
        #         self.drone,
        #         self.small_drone,
        #         self.small_drone,
        #         self.small_drone,
        #         self.small_drone,
        #         self.small_drone,
        #         self.small_drone,
        #         self.amatter
        # ],
        # 'emp': [
        #         self.drone,
        #         self.drone,
        #         self.drone,
        #         self.drone,
        #         self.drone
        # ],
        # 'infantry': [
        #     self.infantry,
        # ],
        # 'gyro': [
        #     self.gyro,
        #     self.gyro_drone
        # ],
        # 'amatter': [
        #     self.amatter,
        # ],
        # 'rf': [
        #     self.rf,
        # ]
        # }


