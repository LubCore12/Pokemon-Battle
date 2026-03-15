from settings import *


class Creature:
    def get_data(self, name):
        self.element = MONSTER_DATA[name]['element']
        self._health = MONSTER_DATA[name]['health']
        self.max_health = MONSTER_DATA[name]['health']
        self.abilities = sample(list(ABILITIES_DATA.keys()), 4)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = min(max(0, value), self.max_health)


class Monster(pygame.sprite.Sprite, Creature):
    def __init__(self, name, surf):
        super().__init__()

        self.image = surf
        self.rect = self.image.get_frect(bottomleft = (100, WINDOW_HEIGHT))
        self.name = name

        self.get_data(name)

    def __repr__(self):
        return f'{self.name}: {self.health}/{self.max_health}'


class Opponent(pygame.sprite.Sprite, Creature):
    def __init__(self, name, surf, groups):
        super().__init__(groups)

        self.image = surf
        self.rect = self.image.get_rect(midtop = (WINDOW_WIDTH - 250, 50))
        self.name = name

        self.get_data(name)

