from config import MechStatsConfig
from hardware import Attack
from config.weapon import WeaponStatsConfig
from hardware import Damage

class Weapon:

    _a_pen: int
    _stat_mod: int

    def __init__(self, config: WeaponStatsConfig, mech_stats: MechStatsConfig) -> None:
        self._config = config
        self._a_pen = self._config.a_pen
        self._emp = self._config.emp
        self._mech_stats = mech_stats
        self._stat_mod = 0
        for stat in self._mech_stats._fields:
            if self._config.stat_mod == stat and self._mech_stats.__annotations__[stat] is int:
                self._stat_mod = mech_stats._asdict()[stat]

    def get_damage(self, additional_mods: int, additional_emods: int) -> list[int]:

        attack = Attack(num_dice=self._config.base_dice + additional_mods + self._stat_mod,
                        num_edice=self._config.base_edice + additional_emods,
                        dice_config=self._config.dice_config, edice_config=self._config.edice_config)
        success_list = []
        for i in range(self._config.auto):
            success_list.append(attack.get_successes())
        return success_list

    def fire(self, additional_mods: int = 0, additional_emods: int = 0) -> list[Damage]:
        dmg_list: list[Damage] = []
        for dmg in self.get_damage(additional_mods, additional_emods):
            dmg_list.append(Damage(dmg, a_pen=self._a_pen, emp=self._emp))
        return dmg_list

    @property
    def a_pen(self) -> int:
        return self._a_pen

    # @property
    # def additional_mods(self) -> int:
    #     return self._additional_mods
    #
    # @additional_mods.setter
    # def additional_mods(self, mod: int) -> None:
    #     self._additional_mods = mod
    #
    # @property
    # def additional_emods(self) -> int:
    #     return self._additional_emods
    #
    # @additional_emods.setter
    # def additional_emods(self, mod: int) -> None:
    #     self._additional_emods = mod


