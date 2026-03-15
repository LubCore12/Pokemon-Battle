from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Monster Battle')
        self.clock = pygame.time.Clock()
        self.running = True
        self.player_active = True

        self.import_assets()

        self.all_sprites = pygame.sprite.Group()

        player_monster_list = ['Cindrill', 'Atrox', 'Cleaf', 'Finsta', 'Larvea', 'Sparchu']
        self.player_monsters = [Monster(name, self.back_surfaces[name]) for name in player_monster_list]
        self.monster = self.player_monsters[0]

        self.all_sprites.add(self.monster)

        opponent_monster = choice(list(MONSTER_DATA.keys()))
        self.opponent = Opponent(opponent_monster, self.front_surfaces[opponent_monster], self.all_sprites)

        self.ui = UI(self.monster, self.player_monsters, self.small_monsters, self.get_input)
        self.opponent_ui = OpponentUI(self.opponent)

        self.timers = {
            'player end': Timer(1000, func=self.opponent_turn),
            'opponent end': Timer(1000, func=self.player_turn)
        }

    def get_input(self, state, data = None):
        if state == 'attack':
            self.apply_attack(self.opponent, data)

        elif state == 'heal':
            pass

        elif state == 'switch':
            pass

        elif state == 'escape':
            self.running = False

        self.player_active = False
        self.timers['player end'].activate()

    def apply_attack(self, target, attack):
        attack_dict = ABILITIES_DATA[attack]
        element = attack_dict['element']
        damage = attack_dict['damage']

        element_multiplier = ELEMENT_DATA[element][target.element]

        target.health -= damage * element_multiplier

        print(f'{target.name}: {target.health}/{target.max_health}')
        print(element, damage, element_multiplier)

    def opponent_turn(self):
        attack = choice(list(self.opponent.abilities))
        self.apply_attack(self.monster, attack)
        self.timers['opponent end'].activate()

    def player_turn(self):
        self.player_active = True

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def import_assets(self):
        self.back_surfaces = folder_importer('images', 'back')
        self.front_surfaces = folder_importer('images', 'front')
        self.small_monsters = folder_importer('images', 'simple')
        self.bg_surfs = folder_importer('images', 'other')

    def draw_monster_floor(self):
        for sprite in self.all_sprites:
            floor_rect = self.bg_surfs['floor'].get_frect(center=sprite.rect.midbottom + pygame.Vector2(0, -10))
            self.display_surface.blit(self.bg_surfs['floor'], floor_rect)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update_timers()
            self.all_sprites.update(dt)
            if self.player_active:
                self.ui.update()

            self.display_surface.blit(self.bg_surfs['bg'], (0, 0))
            self.draw_monster_floor()

            self.all_sprites.draw(self.display_surface)
            self.ui.draw()
            self.opponent_ui.draw()
            pygame.display.update()
        
        pygame.quit()
    
if __name__ == '__main__':
    game = Game()
    game.run()