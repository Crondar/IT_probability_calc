from hardware import *
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

    def roll_weapon_set(self, set_name: str, additional_mods: int = 0, additional_emods: int = 0) -> list[Damage]:
        dmg_list: list[Damage] = []
        for weapon in self._weapons[set_name]:
            dmg_list += weapon.fire(additional_mods=additional_mods, additional_emods=additional_emods)
        return dmg_list

    def roll_hit_location(self) -> int:
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

    def strip_evasion(self, damage_list: list[Damage]) -> list[Damage]:
        new_damage: list[Damage] = []
        for dmg in range(len(damage_list)):
            if damage_list[dmg].damage > self._evasion:
                new_damage.append(damage_list[dmg])
        return new_damage

    def take_damage(self, damage_list: list[Damage]) -> None:
        adjusted_dmg = self.strip_evasion(damage_list)
        for dmg in adjusted_dmg:
            if dmg.location == 0:
                hit_loc = self.get_adjusted_hit_location(self.roll_hit_location())
            for limb in self._limbs:
                if limb.hit_range.contains(dmg.location):
                    print(f"{limb.name}, dmg: {dmg.damage}, AP: {dmg.a_pen}, EMP: {dmg.emp}")
                    init_hp = limb.hp
                    limb.damage(dmg.damage, dmg.a_pen)
                    if init_hp > limb.hp:
                        self._charge -= max(dmg.emp - self._emp_hardening, 0)
                    else:
                        self._charge -= max(dmg.emp / 2, 0 - self._emp_hardening, 0)

    def reset_round(self) -> None:
        for limb in self._limbs:
            limb.reset_armor()
        self._evasion = self._config.mech_stats.base_evasion

    def reset_full(self) -> None:
        for limb in self._limbs:
            limb.reset_armor()
            limb.reset_health()
            limb.reset_ablative()
        self._evasion = self._config.mech_stats.base_evasion

    def get_limb_states(self) -> list[Limb]:
        limb_list: list[Limb] = []
        for limb in self._limbs:
            limb_list.append(limb)
        return limb_list

    def display_stats(self) -> None:
        for limb in self._limbs:
            print(f"{limb.name}: hp: {limb.hp}, armor: {limb.armor} + {limb.ablative}a")
        print(f"charge: {self._charge}")

    @property
    def charge(self) -> int:
        return self._charge




