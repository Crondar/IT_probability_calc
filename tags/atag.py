from abc import ABC, abstractmethod

class Tag(ABC):

    @abstractmethod
    def get_modifier(self, weapon_range: int, distance: int) -> int:
        pass

    