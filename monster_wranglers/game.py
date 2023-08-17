from random import randint
import pygame

from config import WINDOW_HEIGHT, WINDOW_WIDTH


class Game():
    def __init__(self, player, monster_group, display_surface):
        self.score = 0
        self.round_number = 0

        self.round_time = 0

        self.player = player
        self.monster_group = monster_group

        self.next_level_sound = pygame.mixer.Sound(
            "assets/sounds/next_level.wav")

        self.font = pygame.font.Font('assets/fonts/Abrushow.ttf')

        blue_image = pygame.image.load("assets/images/blue_monster.png")
        green_image = pygame.image.load("assets/images/green_monster.png")
        purple_image = pygame.image.load("assets/images/purple_monster.png")
        yellow_image = pygame.image.load("assets/images/yellow_monster.png")

        self.target_monster_images = [blue_image,
                                      green_image, purple_image, yellow_image]

        self.target_monster_type = randint(0, 3)
        self.target_monster_image = self.target_monster_images[self.target_monster_type]

        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.centerx = WINDOW_WIDTH/2
        self.target_monster_rect.top = 30
        self.display_surface = display_surface

    def update(self):
        # TODO
        pass

    def draw(self):
        WHITE = (255, 255, 255)
        BLUE = (20, 176, 235)
        GREEN = (87, 201, 47)
        PURPLE = (226, 76, 243)
        YELLOW = (243, 157, 20)
        colors = [BLUE, GREEN, PURPLE, YELLOW]

        catch_text = self.font.render("Current Catch", True, WHITE)
        catch_rect = catch_text.get_rect()
        catch_rect.centerx = WINDOW_WIDTH/2
        catch_rect.top = 5

        score_text = self.font.render(f"Score:{self.score}", True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 5)

        lives_text = self.font.render(
            f"lives:{self.player.lives}", True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (5, 35)

        round_text = self.font.render(
            f"Current round:{self.round_number}", True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (5, 65)

        time_text = self.font.render(
            f"Round time:{self.round_time}", True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topleft = (WINDOW_WIDTH - 10, 5)

        warp_text = self.font.render(
            f"Warps:{self.player.warps}", True, WHITE)
        warp_rect = warp_text.get_rect()
        warp_rect.topleft = (WINDOW_WIDTH - 10, 35)

        self.display_surface.blit(catch_text, catch_rect)
        self.display_surface.blit(score_text, score_rect)
        self.display_surface.blit(lives_text, lives_rect)
        self.display_surface.blit(round_text, round_rect)
        self.display_surface.blit(time_text, time_rect)
        self.display_surface.blit(warp_text, warp_rect)

        self.display_surface.blit(
            self.target_monster_image, self.target_monster_rect)

        pygame.draw.rect(self.display_surface, colors[self.target_monster_type], (
            0, 100, WINDOW_WIDTH, WINDOW_HEIGHT-200), 4)

        # TODO  def check_collisions
