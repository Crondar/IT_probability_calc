from hardware import *
from hardware import Limb
from mechs.drone_mech import MechConfig


class Mech:

    def __init__(self, config: MechConfig):
        self._config = config
        self._limbs = []
        for limb in self._config.limbs:
            self._limbs.append(Limb(limb))

        self._weapons = {}
        for k in self._config.weapon_set_dict.keys():
            w_set = []
            for weapon in self._config.weapon_set_dict[k]:
                w_set.append(Weapon(weapon))
            self._weapons[k] = w_set

        self._evasion = self._config.mech_stats.base_evasion
        self._charge = self._config.mech_stats.charge
        self._emp_hardening = self._config.emp_hardening

    def roll_weapon_set(self, set_name: str, additional_mods: int = 0, additional_emods: int = 0) -> list[tuple[int, int, int]]:
        dmg_list: list[tuple[int, int, int]] = []
        for weapon in self._weapons[set_name]:
            weapon.additional_mods = additional_mods
            weapon.additional_emods = additional_emods
            dmg_list += weapon.fire()
        return dmg_list

    def roll_hit_location(self):
        total: int = 0
        loc_dice = Dice(self._config.dice_config)
        for dice in range(self._config.hit_location_dice_num):
            total += loc_dice.roll()
        return total

    def get_adjusted_hit_location(self, hit_loc: int) -> int:
        for limb in self._limbs:
            if limb.hit_range.contains(hit_loc) and limb.hp <= 0:
                new_loc = hit_loc
                if hit_loc < 9:
                    new_loc = hit_loc + limb.hit_range.max_val - limb.hit_range.min_val + 1
                elif hit_loc > 12:
                    new_loc = hit_loc - (limb.hit_range.max_val - limb.hit_range.min_val + 1)
                else:
                    return hit_loc
                return self.get_adjusted_hit_location(new_loc)
        return hit_loc

    def strip_evasion(self, damage: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
        new_damage: list[tuple[int, int, int]] = []
        for dmg in range(len(damage)):
            if damage[dmg][0] >= self._evasion:
                new_damage.append(damage[dmg])
        return new_damage

    def take_damage(self, damage: list[tuple[int, int, int]]) -> None:
        adjusted_dmg = self.strip_evasion(damage)
        for dmg in adjusted_dmg:
            hit_loc = self.get_adjusted_hit_location(self.roll_hit_location())
            for limb in self._limbs:
                if limb.hit_range.contains(hit_loc):
                    print(f"{limb.name}, dmg: {dmg[0]},")
                    init_hp = limb.hp
                    limb.damage(dmg[0], dmg[1])
                    if init_hp > limb.hp:
                        self._charge -= max(dmg[2] - self._emp_hardening, 0)
                    else:
                        self._charge -= max(dmg[2] / 2, 0)

    def reset_round(self):
        for limb in self._limbs:
            limb.reset_armor()
        self._evasion = self._config.mech_stats.base_evasion

    def reset_full(self):
        for limb in self._limbs:
            limb.reset_armor()
            limb.reset_health()
            limb.reset_ablative()
        self._evasion = self._config.mech_stats.base_evasion

    def display_stats(self):
        for limb in self._limbs:
            print(f"{limb.name}: hp: {limb.hp}, armor: {limb.armor} + {limb.ablative}a")
        print(f"charge: {self._charge}")






