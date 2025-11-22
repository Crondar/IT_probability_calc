from config import WeaponStatsConfig
from config import DiceConfig, EDiceConfig

_dice_config = DiceConfig(sides=6, min_success=5)
_edice_config = EDiceConfig(dice_config=_dice_config, min_explode=6)


autocannon = WeaponStatsConfig(base_dice=3, base_edice=0, a_pen=0, auto=2, stat_mod='reflex',
                               dice_config=_dice_config, edice_config= _edice_config)
ciws_advanced = WeaponStatsConfig(base_dice=2, base_edice=0, a_pen=0, auto=0, stat_mod='reflex',
                                  dice_config=_dice_config, edice_config= _edice_config)
ciws = WeaponStatsConfig(base_dice=0, base_edice=0, a_pen=0, auto=0, stat_mod='reflex',
                         dice_config=_dice_config, edice_config= _edice_config)
autocannon_anti_infantry = WeaponStatsConfig(base_dice=-1, base_edice=0, a_pen=0, auto=2, stat_mod='reflex',
                                             dice_config=_dice_config, edice_config= _edice_config)
battle_cannon = WeaponStatsConfig(base_dice=3, base_edice=2, a_pen=0, auto=0, stat_mod='reflex',
                                  dice_config=_dice_config, edice_config= _edice_config)
autocannon_heavy = WeaponStatsConfig(base_dice=2, base_edice=2, a_pen=0, auto=0, stat_mod='reflex',
                                     dice_config=_dice_config, edice_config= _edice_config)
artillery_rifle_heavy = WeaponStatsConfig(base_dice=9, base_edice=0, a_pen=0, auto=0, stat_mod='reflex',
                                          dice_config=_dice_config, edice_config= _edice_config)
battle_cannon_heavy = WeaponStatsConfig(base_dice=4, base_edice=3, a_pen=0, auto=0, stat_mod='reflex',
                                        dice_config=_dice_config, edice_config= _edice_config)
machine_gun_heavy = WeaponStatsConfig(base_dice=-1, base_edice=0, a_pen=0, auto=4, stat_mod='reflex',
                                      dice_config=_dice_config, edice_config= _edice_config)
autocannon_light = WeaponStatsConfig(base_dice=2, base_edice=0, a_pen=0, auto=2, stat_mod='reflex',
                                     dice_config=_dice_config, edice_config= _edice_config)
artillery_rifle_light = WeaponStatsConfig(base_dice=6, base_edice=0, a_pen=0, auto=0, stat_mod='reflex',
                                          dice_config=_dice_config, edice_config= _edice_config)
machine_gun_light = WeaponStatsConfig(base_dice=1, base_edice=0, a_pen=0, auto=3, stat_mod='none',
                                      dice_config=_dice_config, edice_config= _edice_config)
rotary_autocannon_light = WeaponStatsConfig(base_dice=0, base_edice=0, a_pen=0, auto=3, stat_mod='reflex',
                                            dice_config=_dice_config, edice_config= _edice_config)
magnetic_anti_material_rifle = WeaponStatsConfig(base_dice=6, base_edice=0, a_pen=5, auto=0, stat_mod='reflex',
                                                 dice_config=_dice_config, edice_config= _edice_config)
magnetic_auto_rifle = WeaponStatsConfig(base_dice=1, base_edice=0, a_pen=1, auto=3, stat_mod='reflex',
                                        dice_config=_dice_config, edice_config= _edice_config)
magnetic_sniper_rifle = WeaponStatsConfig(base_dice=3, base_edice=0, a_pen=3, auto=2, stat_mod='reflex',
                                          dice_config=_dice_config, edice_config= _edice_config)
rotary_autocannon = WeaponStatsConfig(base_dice=1, base_edice=0, a_pen=0, auto=3, stat_mod='reflex',
                                      dice_config=_dice_config, edice_config= _edice_config)
recoilless_rifle = WeaponStatsConfig(base_dice=0, base_edice=2, a_pen=0, auto=0, stat_mod='none',
                                     dice_config=_dice_config, edice_config= _edice_config)
high_energy_laser_focused = WeaponStatsConfig(base_dice=6, base_edice=0, a_pen=0, auto=0, stat_mod='reflex',
                                              dice_config=_dice_config, edice_config= _edice_config)
high_energy_laser = WeaponStatsConfig(base_dice=5, base_edice=0, a_pen=0, auto=0, stat_mod='reflex',
                                      dice_config=_dice_config, edice_config= _edice_config)
low_power_laser = WeaponStatsConfig(base_dice=2, base_edice=0, a_pen=0, auto=0, stat_mod='reflex',
                                    dice_config=_dice_config, edice_config= _edice_config)
plasma_blaster = WeaponStatsConfig(base_dice=0, base_edice=3, a_pen=0, auto=0, stat_mod='reflex',
                                   dice_config=_dice_config, edice_config= _edice_config)
plasma_lance = WeaponStatsConfig(base_dice=2, base_edice=0, a_pen=8, auto=0, stat_mod='reflex',
                                 dice_config=_dice_config, edice_config= _edice_config)
rapid_fire_laser = WeaponStatsConfig(base_dice=0, base_edice=0, a_pen=0, auto=4, stat_mod='reflex',
                                     dice_config=_dice_config, edice_config= _edice_config)
twin_laser = WeaponStatsConfig(base_dice=2, base_edice=0, a_pen=0, auto=2, stat_mod='reflex',
                               dice_config=_dice_config, edice_config= _edice_config)
arc_mace = WeaponStatsConfig(base_dice=2, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                             dice_config=_dice_config, edice_config= _edice_config)
dagger = WeaponStatsConfig(base_dice=2, base_edice=0, a_pen=0, auto=0, stat_mod='reflex',
                           dice_config=_dice_config, edice_config= _edice_config)
hammer = WeaponStatsConfig(base_dice=7, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                           dice_config=_dice_config, edice_config= _edice_config)
rocket_hammer = WeaponStatsConfig(base_dice=12, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                                  dice_config=_dice_config, edice_config= _edice_config)
sword = WeaponStatsConfig(base_dice=5, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                          dice_config=_dice_config, edice_config= _edice_config)
axe = WeaponStatsConfig(base_dice=5, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                        dice_config=_dice_config, edice_config= _edice_config)
heavy_missiles_emp = WeaponStatsConfig(base_dice=0, base_edice=4, a_pen=0, auto=0, stat_mod='intellect',
                                       dice_config=_dice_config, edice_config= _edice_config)
heavy_missiles_kinetic = WeaponStatsConfig(base_dice=8, base_edice=0, a_pen=0, auto=0, stat_mod='intellect',
                                           dice_config=_dice_config, edice_config= _edice_config)
heavy_missiles = WeaponStatsConfig(base_dice=0, base_edice=6, a_pen=0, auto=0, stat_mod='intellect',
                                   dice_config=_dice_config, edice_config= _edice_config)
heavy_missiles_plasma = WeaponStatsConfig(base_dice=0, base_edice=10, a_pen=3, auto=0, stat_mod='intellect',
                                          dice_config=_dice_config, edice_config= _edice_config)
heavy_missiles_swarm = WeaponStatsConfig(base_dice=0, base_edice=3, a_pen=0, auto=3, stat_mod='intellect',
                                         dice_config=_dice_config, edice_config= _edice_config)
rocket_pod_light = WeaponStatsConfig(base_dice=0, base_edice=1, a_pen=0, auto=0, stat_mod='intellect',
                                     dice_config=_dice_config, edice_config= _edice_config)
rocket_pod_ripple = WeaponStatsConfig(base_dice=0, base_edice=1, a_pen=0, auto=3, stat_mod='intellect',
                                      dice_config=_dice_config, edice_config= _edice_config)
rocket_pod = WeaponStatsConfig(base_dice=0, base_edice=3, a_pen=0, auto=0, stat_mod='intellect',
                               dice_config=_dice_config, edice_config= _edice_config)
standard_missiles_emp = WeaponStatsConfig(base_dice=0, base_edice=3, a_pen=0, auto=0, stat_mod='intellect',
                                          dice_config=_dice_config, edice_config= _edice_config)
standard_missiles_kinetic = WeaponStatsConfig(base_dice=5, base_edice=0, a_pen=0, auto=0, stat_mod='intellect',
                                              dice_config=_dice_config, edice_config= _edice_config)
standard_missiles = WeaponStatsConfig(base_dice=0, base_edice=4, a_pen=0, auto=0, stat_mod='intellect',
                                      dice_config=_dice_config, edice_config= _edice_config)
standard_missiles_plasma = WeaponStatsConfig(base_dice=0, base_edice=6, a_pen=3, auto=0, stat_mod='intellect',
                                             dice_config=_dice_config, edice_config= _edice_config)
standard_missiles_swarm = WeaponStatsConfig(base_dice=0, base_edice=2, a_pen=0, auto=3, stat_mod='intellect',
                                            dice_config=_dice_config, edice_config= _edice_config)
claws_large = WeaponStatsConfig(base_dice=3, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                                dice_config=_dice_config, edice_config= _edice_config)
claws_small = WeaponStatsConfig(base_dice=1, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                                dice_config=_dice_config, edice_config= _edice_config)
claws_standard = WeaponStatsConfig(base_dice=2, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                                   dice_config=_dice_config, edice_config= _edice_config)
hand_large = WeaponStatsConfig(base_dice=2, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                               dice_config=_dice_config, edice_config= _edice_config)
hand_small = WeaponStatsConfig(base_dice=0, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                               dice_config=_dice_config, edice_config= _edice_config)
hand_standard = WeaponStatsConfig(base_dice=1, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                                  dice_config=_dice_config, edice_config= _edice_config)
scissors_large = WeaponStatsConfig(base_dice=4, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                                   dice_config=_dice_config, edice_config= _edice_config)
scissors_small = WeaponStatsConfig(base_dice=2, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                                   dice_config=_dice_config, edice_config= _edice_config)
scissors_standard = WeaponStatsConfig(base_dice=3, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                                      dice_config=_dice_config, edice_config= _edice_config)
shield_basic = WeaponStatsConfig(base_dice=2, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                                 dice_config=_dice_config, edice_config= _edice_config)
shield_buckler = WeaponStatsConfig(base_dice=-1, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                                   dice_config=_dice_config, edice_config= _edice_config)
shield_heavy = WeaponStatsConfig(base_dice=3, base_edice=0, a_pen=0, auto=0, stat_mod='endurance',
                                 dice_config=_dice_config, edice_config= _edice_config)
