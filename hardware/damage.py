# add damage type/tag
class Damage:

    _damage: int
    _a_pen: int
    _location: int
    _emp: int
    _tags: str

    def __init__(self, damage: int, a_pen: int = 0, location: int = 0, emp: int = 0, tags:str = '',) -> None:
        self._damage = damage
        self._a_pen = a_pen
        self._location = location
        self._emp = emp
        self._tags = tags


    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage: int):
        self._damage = damage

    @property
    def a_pen(self):
        return self._a_pen

    @a_pen.setter
    def a_pen(self, a_pen: int):
        self._a_pen = a_pen

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location: int):
        self._location = location

    @property
    def emp(self):
        return self._emp

    @emp.setter
    def emp(self, emp: int):
        self._emp = emp

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags: str):
        self._tags = tags

