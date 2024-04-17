"""
4/17

DONE : 
1. click the start button to start the game
2. the player moves with the mouse
3. the stones fly from all sides
4. the speed of the stones can be changed
5. if a stone hits the player, the player's health decreases by 10%
6. if the player's health is 0%, the game will end
7. there is a timer : 30 seconds
8. if the timer stops and the player's health is more than 0% -> print("You WIN") & display text on the screen
9. the healthbar and timer is displayed on the screen
10. changed the font (google font)

TO DO:
1. make the player stay in the middle of the screen
2. make the game full screen
3. make the shield to protect the player
4. make a function to shoot stones 
"""

import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
STONE_SIZE = 30
STONE_SPEED = 5
PLAYER_HEALTH = 100
COUNTDOWN_SECONDS = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT = (241, 250, 238)
DARK_GRAY = (40, 40, 40)
GRAY = (100, 100, 100)

# Fonts
BUTTON_FONT = pygame.font.Font("PixelifySans-VariableFont_wght.ttf", 30)
TITLE_FONT = pygame.font.Font("PixelifySans-VariableFont_wght.ttf", 60)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stone Defense Game")

background_img = pygame.image.load("background.jpg")  # Load your background image here
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (PLAYER_SIZE, PLAYER_SIZE))

stone_img = pygame.image.load("stone.png")
stone_img = pygame.transform.scale(stone_img, (STONE_SIZE, STONE_SIZE))
icon_img = pygame.image.load("icon.png")
pygame.display.set_icon(icon_img)

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Stone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = stone_img
        self.rect = self.image.get_rect()
        self.direction = random.choice(["right", "left", "up", "down"])
        if self.direction == "right":
            self.rect.x = 0 - STONE_SIZE
            self.rect.y = random.randint(0, SCREEN_HEIGHT - STONE_SIZE)
            self.speed_x = STONE_SPEED
            self.speed_y = 0
        elif self.direction == "left":
            self.rect.x = SCREEN_WIDTH
            self.rect.y = random.randint(0, SCREEN_HEIGHT - STONE_SIZE)
            self.speed_x = -STONE_SPEED
            self.speed_y = 0
        elif self.direction == "up":
            self.rect.x = random.randint(0, SCREEN_WIDTH - STONE_SIZE)
            self.rect.y = SCREEN_HEIGHT
            self.speed_x = 0
            self.speed_y = -STONE_SPEED
        elif self.direction == "down":
            self.rect.x = random.randint(0, SCREEN_WIDTH - STONE_SIZE)
            self.rect.y = 0 - STONE_SIZE
            self.speed_x = 0
            self.speed_y = STONE_SPEED

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()

def draw_health_bar(surface, x, y, health):
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (health / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surface, RED, fill_rect)
    pygame.draw.rect(surface, WHITE, outline_rect, 2)

# Create the start button
def create_button(surface, text, x, y, width, height, inactive_color, active_color, action):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
        pygame.draw.rect(surface, active_color, (x, y, width, height))
        if click[0] == 1:
            action()
    else:
        pygame.draw.rect(surface, inactive_color, (x, y, width, height))

    button_text = BUTTON_FONT.render(text, True, BLACK)
    text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    surface.blit(button_text, text_rect)

def start_game():
    global countdown_timer, PLAYER_HEALTH
    countdown_timer = COUNTDOWN_SECONDS * 60  # Reset countdown timer
    PLAYER_HEALTH = 100  # Reset player health

    # Create sprites group
    # https://gamedevacademy.org/pygame-sprite-group-tutorial-complete-guide/
    all_sprites = pygame.sprite.Group()
    stones = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update countdown timer
        win_font = pygame.font.Font("PixelifySans-VariableFont_wght.ttf", 50)
        countdown_timer -= 1
        if countdown_timer <= 0:
            if PLAYER_HEALTH > 0:
                win_text = win_font.render("You WIN!", True, WHITE)
                win_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(win_text, win_rect)
                pygame.display.flip()
                pygame.time.wait(5000)
                print("You WIN!")
                
            pygame.quit()
            sys.exit()

        if len(stones) < 5:
            stone = Stone()
            all_sprites.add(stone)
            stones.add(stone)

        all_sprites.update()

        # Collisions with stones
        hits = pygame.sprite.spritecollide(player, stones, True)
        for hit in hits:
            PLAYER_HEALTH -= 10

        screen.blit(background_img, (0, 0))  # Blit background image
        all_sprites.draw(screen)
        draw_health_bar(screen, 10, 10, PLAYER_HEALTH)

        # Draw countdown timer
        countdown_seconds = countdown_timer // 60  # Convert frames back to seconds
        timer_text = BUTTON_FONT.render("Time left: {}s".format(countdown_seconds), True, WHITE)
        screen.blit(timer_text, (SCREEN_WIDTH - 250, 10))

        if PLAYER_HEALTH <= 0:
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(60)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        screen.blit(background_img, (0, 0))

        title_text = TITLE_FONT.render("Stone Defense Game", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        screen.blit(title_text, title_rect)

        # Start button
        create_button(screen, "Start", 300, 350, 200, 80, GRAY, LIGHT, start_game)

        pygame.display.flip()
        clock.tick(60)

main()
