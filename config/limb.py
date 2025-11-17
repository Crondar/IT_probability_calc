from typing import NamedTuple
from math_help import range

class LimbConfig(NamedTuple):
    armor: int
    hp: int
    hit_location_range: range.Range
    name: str
    ablative_armor: int = 0

