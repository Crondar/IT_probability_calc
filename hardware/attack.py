from hardware.dice import Dice
from hardware.edice import Edice

class Attack:

    def __init__(self, num_dice: int, num_edice: int, dice_config, edice_config) -> None:
        self._dice_pool = []
        if num_edice < 0:
            num_dice += num_edice
        if num_dice < 0:
            num_dice = 0
        for i in range(num_dice):
            self._dice_pool.append(Dice(dice_config))
        for i in range(num_edice):
            self._dice_pool.append(Edice(edice_config))

    def get_successes(self) -> int:
        successes = 0
        for dice in self._dice_pool:
            successes += dice.get_successes()
        return successes

    def get_targeted_successes(self, target_mod: int) -> int:
        successes = 0
        pool = self._dice_pool
        pool.sort(key=lambda dice: dice == Edice, reverse=True)
        for dice in pool[0:max(-target_mod, len(pool))]:
            successes += dice.get_successes()
        return successes

