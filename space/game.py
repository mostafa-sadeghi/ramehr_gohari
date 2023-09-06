import pygame

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
        self.alien_hit_sound = pygame.mixer.Sound("alien_hit.wav")
        self.player_hit_sound = pygame.mixer.Sound("player_hit.wav")

        self.font = pygame.font.Font("Facon.ttf", 32)

    def update(self):
        # TODO
        pass

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
