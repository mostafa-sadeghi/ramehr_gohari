import pygame
from alien import Alien

from config import WINDOW_HEIGHT, WINDOW_WIDTH


class Game:
    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        self.round_number = 1
        self.score = 0

        self.player = player
        self.alien_group = alien_group
        self.player_bullet_group = player_bullet_group
        self.alien_bullet_group = alien_bullet_group

        self.new_round_sound = pygame.mixer.Sound("assets/new_round.wav")
        self.breach_sound = pygame.mixer.Sound("assets/breach.wav")
        self.alien_hit_sound = pygame.mixer.Sound("assets/alien_hit.wav")
        self.player_hit_sound = pygame.mixer.Sound("assets/player_hit.wav")

        self.font = pygame.font.Font("assets/Facon.ttf", 32)

    def update(self):
        self.shift_aliens()
        # self.check_collisions()
        # self.check_round_completion()

    def draw(self, display_surface):
        WHITE = (255, 255, 255)

        score_text = self.font.render(f"Score : {self.score}", True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.centerx = WINDOW_WIDTH / 2
        score_rect.top = 10

        round_text = self.font.render(
            f"Round: {self.round_number}", True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (20, 10)

        lives_text = self.font.render(
            f"Lives: {self.player.lives}", True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH - 20, 10)

        display_surface.blit(score_text, score_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(lives_text, lives_rect)

        pygame.draw.line(display_surface, WHITE,
                         (0, 50), (WINDOW_WIDTH, 50), 5)
        pygame.draw.line(display_surface, WHITE, (0, WINDOW_HEIGHT -
                         100), (WINDOW_WIDTH, WINDOW_HEIGHT-100), 5)

    def shift_aliens(self):
        shift = False
        for alien in self.alien_group.sprites():
            if alien.rect.left <= 0 or alien.rect.right >= WINDOW_WIDTH:
                shift = True

        if shift:
            breach = False
            for alien in self.alien_group.sprites():
                alien.rect.y += 10 * self.round_number

                alien.direction *= -1
                alien.rect.x += alien.direction * alien.velocity
                if alien.rect.bottom >= WINDOW_HEIGHT - 100:
                    breach = True

            if breach:
                self.breach_sound.play()
                self.player.lives -= 1
                # self.check_game_status("Aliens breached the line!", 'Press "Enter" to continue')

    def start_new_round(self):
        for i in range(11):
            for j in range(5):
                alien = Alien(64 + i * 64, 64 + j * 64,
                              self.round_number, self.alien_bullet_group)
                self.alien_group.add(alien)

        self.new_round_sound.play()
