from vehicles.mech import Mech as Mech
from mechs.drone_mech import MechConfig as MechConfig1
from mechs.laser_mech import MechConfig as LaserMech

mech_config1 = MechConfig1()
mech1 = Mech(mech_config1)

mech_config2 = LaserMech()
mech2 = Mech(mech_config2)

mech2.take_damage(mech1.roll_weapon_set('emp'))
mech2.display_stats()