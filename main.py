from vehicles.mech import Mech as Mech
from mechs.drone_mech import MechConfig as DroneMech
from mechs.laser_mech import MechConfig as LaserMech
from fight import Fights
from hardware import Edice
from config.edice import EDiceConfig

edice = Edice(DroneMech().edice_config)

mech_config1 = DroneMech()
mech1 = Mech(mech_config1)

mech_config2 = LaserMech()
mech2 = Mech(mech_config2)

fight = Fights(mech2, mech1)

# print(fight.get_avg_defender_state('drones', 100))

# edice_sum = 0
#
# for i in range(1000000):
#     edice_sum += edice.get_successes()
# print(edice_sum/1000000)


sumhp = 0
for i in range(10000):
    # mech2.take_damage(mech1.fire_all())
    mech2.display_stats()
    mech2.take_damage(mech1.fire_all_targeted(10, 2))
    sumhp += mech2.get_limb_states()[0].hp
    mech2.reset_full()
print(sumhp/10000)
mech2.display_stats()