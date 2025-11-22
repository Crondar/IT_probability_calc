import numpy

from hardware import Limb
from vehicles.mech import Mech
import numpy as np

class Fights:

    def __init__(self, defender: Mech, attacker: Mech):
        self._defender = defender
        self._attacker = attacker

    def get_avg_defender_state(self, weapon_set: str, sample: int = 100) -> tuple[list[tuple[str, float, float, float]], float]:
        """
        returns ([(limb_name, limb_hp, limb_armor, limb_ablative),], charge)
        """
        limb_states: list[list[Limb]] = []
        charge_list: list[int] = []
        for i in range(sample):
            self._defender.take_damage(self._attacker.roll_weapon_set(weapon_set))
            limb_states.append(self._defender.get_limb_states())
            charge_list.append(self._defender.charge)
            self._defender.reset_full()
        avg_charge = sum(charge_list) / len(charge_list)
        avg_limb_states: list[tuple[str, float, float, float]] = []
        for i in range(len(limb_states[0])):
            limb_name = limb_states[0][i].name
            limb_avg_hp = 0
            limb_avg_armor = 0
            limb_avg_ablative = 0
            for j in limb_states:
                limb_avg_hp += j[i].hp / len(limb_states)
                limb_avg_armor += j[i].armor / len(limb_states)
                limb_avg_ablative += j[i].ablative / len(limb_states)
            avg_limb_states.append((limb_name, limb_avg_hp, limb_avg_armor, limb_avg_ablative))
        return avg_limb_states, avg_charge



