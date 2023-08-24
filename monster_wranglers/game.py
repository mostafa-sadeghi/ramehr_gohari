from random import choice, randint
import pygame

from config import WINDOW_HEIGHT, WINDOW_WIDTH
from monster import Monster


class Game():
    def __init__(self, player, monster_group, display_surface):
        self.score = 0
        self.round_number = 0

        self.round_time = 0
        self.frame_counter = 0

        self.player = player
        self.monster_group = monster_group

        self.next_level_sound = pygame.mixer.Sound(
            "assets/sounds/next_level.wav")

        self.font = pygame.font.Font('assets/fonts/Abrushow.ttf', 24)

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
        self.frame_counter += 1
        if self.frame_counter == 60:
            self.round_time += 1
            self.frame_counter = 0
        self.check_collisions()

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
        time_rect.topright = (WINDOW_WIDTH - 10, 5)

        warp_text = self.font.render(
            f"Warps:{self.player.warps}", True, WHITE)
        warp_rect = warp_text.get_rect()
        warp_rect.topright = (WINDOW_WIDTH - 10, 35)

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

        pygame.draw.rect(
            self.display_surface, colors[self.target_monster_type], (WINDOW_WIDTH/2-32, 30, 64, 64), 2)

    def check_collisions(self):
        collided_monster = pygame.sprite.spritecollideany(
            self.player, self.monster_group)
        if collided_monster:
            if collided_monster.type == self.target_monster_type:
                self.score += 100 * self.round_number
                collided_monster.remove(self.monster_group)
                if self.monster_group:
                    self.player.catch_sound.play()
                    self.choose_new_target()
                else:
                    self.player.reset()
                    self.start_new_round()

            else:
                self.player.die_sound.play()
                self.player.lives -= 1
                if self.player.lives <= 0:
                    self.pause_game(
                        f"Final Score:{self.score}", "Press 'Enter to play again...")
                    self.reset_game()
                self.player.reset()

    def start_new_round(self):
        self.score += int(10000 * self.round_number/(1 + self.round_number))
        self.round_time = 0
        self.round_number += 1
        self.player.warps += 1

        for monster in self.monster_group:
            self.monster_group.remove(monster)

        for i in range(self.round_number):
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT-164), self.target_monster_images[0], 0))
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT-164), self.target_monster_images[1], 1))
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT-164), self.target_monster_images[2], 2))
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT-164), self.target_monster_images[3], 3))
        self.choose_new_target()
        self.next_level_sound.play()

    def choose_new_target(self):
        target_monster = choice(self.monster_group.sprites())
        self.target_monster_image = target_monster.image
        self.target_monster_type = target_monster.type

    def pause_game(self, main_text, sub_text, running):

        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        main_text = self.font.render(main_text, True, WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

        sub_text = self.font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 64)

        self.display_surface.fill(BLACK)
        self.display_surface.blit(main_text, main_rect)
        self.display_surface.blit(sub_text, sub_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False

        return running

    def reset_game(self):
        self.score = 0
        self.round_number = 0
        self.player.lives = 5
        self.player.warps = 2
        self.start_new_round()
