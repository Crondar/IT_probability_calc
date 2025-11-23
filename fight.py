import numpy

from config import WeaponStatsConfig
from hardware import Limb
from vehicles.mech import Mech
import numpy as np


def display_weapon_list(weapon_list: list[WeaponStatsConfig]):
    for w in range(len(weapon_list)):
        print(f"[{w}]: {weapon_list[w].name}")


class Fights:

    def __init__(self, defender: Mech, attacker: Mech):
        self._defender = defender
        self._attacker = attacker

    def _get_user_int(self, prompt: str) -> int:
        target = input(prompt)
        if target.isdigit():
            return int(target)
        else:
            print("invalid input")
            return self._get_user_int(prompt)

    def display_game_state(self):
        print("defender health:")
        self._defender.display_stats()
        print(f"attacker rsc: {self._attacker.rsc}")
        print(f"attacker charge: {self._attacker.charge}")

    def choose_weapons(self):
        new_weapons = []
        current_weapons = self._attacker.weapons.copy()
        for w in range(len(current_weapons)):
            print("weapon options:")
            display_weapon_list(current_weapons)
            input_index = self._get_user_int("enter the index of the weapons you are going to fire: ")
            if  input_index < len(current_weapons):
                new_weapons.append(current_weapons.pop(input_index))
            print("current selection")
            display_weapon_list(new_weapons)
        self._attacker.weapons = new_weapons


    def initiative(self):
        self.choose_weapons()
        additional_mods = self._get_user_int("Additional dice Mods: ")
        target = self._get_user_int("enter the weapon target (0 for none): ")
        if target > 0:
            target_mod = abs(self._get_user_int("enter target modifier: "))
            self._defender.take_damage(self._attacker.fire_all_targeted(target, target_mod, additional_mods=additional_mods))
        else:
            self._defender.take_damage(self._attacker.fire_all(additional_mods=additional_mods))
        self.display_game_state()

    def run(self):
        while self._defender.get_limb_states()[0].hp > 0:
            self.initiative()


    # def get_avg_defender_state(self, weapon_set: str, sample: int = 100) -> tuple[list[tuple[str, float, float, float]], float]:
    #     """
    #     returns ([(limb_name, limb_hp, limb_armor, limb_ablative),], charge)
    #     """
    #     limb_states: list[list[Limb]] = []
    #     charge_list: list[int] = []
    #     for i in range(sample):
    #         self._defender.take_damage(self._attacker.roll_weapon_set(weapon_set))
    #         limb_states.append(self._defender.get_limb_states())
    #         charge_list.append(self._defender.charge)
    #         self._defender.reset_full()
    #     avg_charge = sum(charge_list) / len(charge_list)
    #     avg_limb_states: list[tuple[str, float, float, float]] = []
    #     for i in range(len(limb_states[0])):
    #         limb_name = limb_states[0][i].name
    #         limb_avg_hp = 0
    #         limb_avg_armor = 0
    #         limb_avg_ablative = 0
    #         for j in limb_states:
    #             limb_avg_hp += j[i].hp / len(limb_states)
    #             limb_avg_armor += j[i].armor / len(limb_states)
    #             limb_avg_ablative += j[i].ablative / len(limb_states)
    #         avg_limb_states.append((limb_name, limb_avg_hp, limb_avg_armor, limb_avg_ablative))
    #     return avg_limb_states, avg_charge



