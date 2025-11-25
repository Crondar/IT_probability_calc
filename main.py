from vehicles.mech import Mech as Mech
from mechs.drone_mech import MechConfig as DroneMech
from mechs.lilun import MechConfig as LaserMech
from fight import Fights
from hardware import Edice
from config.edice import EDiceConfig

edice = Edice(DroneMech().edice_config)

mech_config1 = DroneMech()
mech1 = Mech(mech_config1)

mech_config2 = LaserMech()
mech2 = Mech(mech_config2)

fight = Fights(mech2, mech1)

fight.run()

# sumhp = 0
# sumfails = 0
# reps = 10000
# for i in range(reps):
#     mech2.take_damage(mech1.fire_all())
#     # mech2.display_stats()
#     # mech2.take_damage(mech1.fire_all_targeted(10, 2))
#     if mech2.get_limb_states()[0].hp > 0:
#         sumfails += 1
#     sumhp += mech2.get_limb_states()[0].hp
#     mech2.reset_full()
# print(sumhp/reps)
# print(f"{(1 - sumfails/reps) * 100}% chance of one-shotting")
# mech2.display_stats()
