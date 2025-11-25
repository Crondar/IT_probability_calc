from vehicles.mech import Mech
from matplotlib import pyplot as plt


class Probability:

    def __init__(self, defender: Mech, attacker: Mech):
        self._defender = defender
        self._attacker = attacker

    def plot_chassis(self):
