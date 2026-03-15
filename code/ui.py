import pygame

from settings import *

class UI:
    def __init__(self, monster, player_monsters, small_monsters):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.SysFont(None, 30)
        self.left = WINDOW_WIDTH / 2 - 100
        self.top = WINDOW_HEIGHT / 2 + 50
        self.monster = monster

        self.general_options = [
            'attack',
            'heal',
            'switch',
            'escape'
        ]

        self.general_index = {
            'col': 0,
            'row': 0
        }

        self.attack_options = self.monster.abilities

        self.attack_index = {
            'col': 0,
            'row': 0
        }

        self.switch_index = 0

        self.state = 'general'
        self.cols, self.rows = 2, 2
        self.visible_monsters = 4
        self.player_monsters = list(filter(lambda monster: self.monster != monster and monster.health > 0, player_monsters))
        self.small_monsters = small_monsters

    def input(self):
        keys = pygame.key.get_just_pressed()
        if self.state == 'general':
            self.general_index['col'] = (self.general_index['col'] + int(keys[pygame.K_DOWN] - keys[pygame.K_UP])) % self.cols
            self.general_index['row'] = (self.general_index['row'] +  int(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])) % self.rows

            if keys[pygame.K_SPACE]:
                self.state = self.general_options[self.general_index['row'] + int(self.general_index['col'] * 2)]

        elif self.state == 'attack':
            self.attack_index['col'] = (self.attack_index['col'] + int(keys[pygame.K_DOWN] - keys[pygame.K_UP])) % self.cols
            self.attack_index['row'] = (self.attack_index['row'] +  int(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])) % self.rows

            if keys[pygame.K_SPACE]:
                print(self.attack_options[self.attack_index['row'] + int(self.attack_index['col'] * 2)])

        elif self.state == 'switch':
            self.switch_index = (self.switch_index + int(keys[pygame.K_DOWN] - keys[pygame.K_UP])) % len(self.player_monsters)

            if keys[pygame.K_SPACE]:
                print(self.player_monsters[self.switch_index])

        if keys[pygame.K_ESCAPE]:
            self.state = 'general'

    def basic_select(self, index, options):
        rect = pygame.FRect(self.left + 40, self.top + 60, 400, 200)
        pygame.draw.rect(self.display_surface, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['gray'], rect, 4, 4)

        for col in range(self.cols):
            for row in range(self.rows):
                x = rect.left + rect.width / (self.rows * 2) + (rect.width / self.rows) * row
                y = rect.top + rect.height / (self.cols * 2) + (rect.height / self.cols) * col
                i = row + 2 * col
                color = COLORS['gray'] if col == index['col'] and row == index['row'] else COLORS['black']

                text_surf = self.font.render(options[i], True, color)
                text_rect = text_surf.get_frect(center=(x, y))

                self.display_surface.blit(text_surf, text_rect)

    def switch(self):
        rect = pygame.FRect(self.left + 40, self.top - 100, 400, 400)
        pygame.draw.rect(self.display_surface, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['gray'], rect, 4, 4)

        v_offset = 0 if self.switch_index < self.visible_monsters else -(self.switch_index // 4) * rect.height

        for i in range(len(self.player_monsters)):
            x = rect.centerx
            y = rect.top + rect.height / (self.visible_monsters * 2) + rect.height / self.visible_monsters * i + v_offset
            color = COLORS['gray'] if i == self.switch_index else COLORS['black']

            name = self.player_monsters[i].name

            text_surface = self.font.render(name, True, color)
            text_rect = text_surface.get_frect(midleft=(x, y))
            monster_surf = self.small_monsters[name]
            monster_rect = monster_surf.get_frect(center=(x - 100, y))

            if rect.contains(text_rect):
                self.display_surface.blit(text_surface, text_rect)
                self.display_surface.blit(monster_surf, monster_rect)

    def update(self):
        self.input()

    def draw(self):
        match self.state:
            case 'general':
                self.basic_select(self.general_index, self.general_options)
            case 'attack':
                self.basic_select(self.attack_index, self.attack_options)
            case 'switch':
                self.switch()