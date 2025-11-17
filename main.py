from mechs.mech1.mech import Mech as Mech1
from mechs.mech1.mech_config import MechConfig as MechConfig1

mech_config1 = MechConfig1()
mech1 = Mech1(mech_config1)

mech_config2 = MechConfig1()
mech2 = Mech1(mech_config2)

mech2.take_damage(mech2.roll_weapon_set('overdrive'))
mech2.display_stats()