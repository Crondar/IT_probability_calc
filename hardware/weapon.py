from hardware.attack import Attack
from config.weapon import WeaponConfig

class Weapon:

    _additional_mods:int
    _additional_emods:int
    _a_pen: int

    def __init__(self, config: WeaponConfig):
        self._config = config
        self._additional_mods = 0
        self._additional_emods = 0
        self._a_pen = self._config.a_pen
        self._emp = self._config.emp

    def get_damage(self) -> list[int]:

        attack = Attack(num_dice=self._config.base_dice + self._additional_mods + self._config.stat_mod,
                        num_edice=self._config.base_edice + self._additional_emods,
                        dice_config=self._config.dice_config, edice_config=self._config.edice_config)
        success_list = []
        for i in range(self._config.auto):
            success_list.append(attack.get_successes())
        return success_list

    def fire(self) -> list[tuple[int, int, int]]:
        dmg_list: list[tuple[int, int, int]] = []
        for dmg in self.get_damage():
            dmg_list.append((dmg, self._a_pen, self._emp))
        return dmg_list

    @property
    def a_pen(self) -> int:
        return self._a_pen

    @property
    def additional_mods(self) -> int:
        return self._additional_mods

    @additional_mods.setter
    def additional_mods(self, mod: int) -> None:
        self._additional_mods = mod

    @property
    def additional_emods(self) -> int:
        return self._additional_emods

    @additional_emods.setter
    def additional_emods(self, mod: int) -> None:
        self._additional_emods = mod


