from config.limb import LimbConfig
from math_help.range import Range

class Limb:

    def __init__(self, config: LimbConfig):
        self._config = config
        self._armor_range = Range(0, config.armor)
        self._armor = config.armor
        self._ablative = config.ablative_armor
        self._hp = config.hp
        self._hit_range = config.hit_location_range
        self._name = self._config.name



    def reset_armor(self):
        self._armor = self._config.armor

    def damage(self, dmg: int, a_pen: int) -> None:
        if self._ablative > 0:
            self._ablative -= a_pen
            if self._ablative < 0:
                pen = -self._ablative
                self._armor = max(self._armor-pen, 0)
                self._hp -= max([dmg - self._armor, 0])
                self._armor += pen
            else:
                self._ablative -= dmg
                self._armor -= max(-self._ablative, 0)
                self._hp -= max(-self._armor, 0)
            self._ablative += a_pen
        else:
            pen = max(self._armor-a_pen, 0)
            self._armor -= pen
            self._armor -= dmg
            self._hp -= max(-self._armor, 0)
            self._armor += a_pen

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def hit_range(self) -> Range:
        return self._hit_range

    @property
    def name(self) -> str:
        return self._name

    @property
    def armor(self) -> int:
        return self._armor

    @property
    def ablative(self) -> int:
        return self._ablative