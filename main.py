import pygame
from classes.Dashboard import Dashboard
from classes.Level import Level
from classes.Menu import Menu
from classes.Sound import Sound
from entities.Mario import Mario
from config import SCALED_WIDTH, SCALED_HEIGHT
import sys


def show_loading_screen(screen, scaled_width, scaled_height, level, sound):
    font = pygame.font.Font('SuperMario256.ttf', 24)  # Create a font object with a specified font and size
    full_text = "An Adaptation of Super Mario"
    displayed_text = ""  # Start with an empty string and build it up character by character

    text_surface = font.render("", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(scaled_width // 2, scaled_height // 2))
    
    clock = pygame.time.Clock()
    char_interval = 200  # Time in milliseconds to wait before showing the next character

    for i in range(len(full_text) + 1):
        while pygame.time.get_ticks() % char_interval > 100:  # Minor loop to delay until the next interval
            clock.tick(60)  # Control the loop speed to be responsive
            for event in pygame.event.get():  # Event processing
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.time.delay(25)
        displayed_text = full_text[:i]  # Get substring of the text up to the i-th character
        sound.play_sfx(sound.kick)
        text_surface = font.render(displayed_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(scaled_width // 2, scaled_height // 2))

        # Drawing the background similar to the drawMenuBackground method
        for y in range(0, 13):
            for x in range(0, 20):
                screen.blit(level.sprites.spriteCollection.get("sky").image, (x * 32, y * 32))
        for y in range(13, 15):
            for x in range(0, 20):
                screen.blit(level.sprites.spriteCollection.get("ground").image, (x * 32, y * 32))

        screen.blit(text_surface, text_rect)  # Blit the current portion of the text
        pygame.display.update()  # Update the entire screen to reflect changes

        for event in pygame.event.get():  # Additional event processing within the main loop
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.time.delay(800) 

    full_text = "Developed by Ashika Ramesh"
    displayed_text = ""  # Start with an empty string and build it up character by character

    text_surface = font.render("", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(scaled_width // 2, scaled_height // 2))
    
    clock = pygame.time.Clock()
    char_interval = 200  # Time in milliseconds to wait before showing the next character

    for i in range(len(full_text) + 1):
        while pygame.time.get_ticks() % char_interval > 100:  # Minor loop to delay until the next interval
            clock.tick(60)  # Control the loop speed to be responsive
            for event in pygame.event.get():  # Event processing
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.time.delay(25)
        displayed_text = full_text[:i]  # Get substring of the text up to the i-th character
        sound.play_sfx(sound.kick)
        text_surface = font.render(displayed_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(scaled_width // 2, scaled_height // 2))

        # Drawing the background similar to the drawMenuBackground method
        for y in range(0, 13):
            for x in range(0, 20):
                screen.blit(level.sprites.spriteCollection.get("sky").image, (x * 32, y * 32))
        for y in range(13, 15):
            for x in range(0, 20):
                screen.blit(level.sprites.spriteCollection.get("ground").image, (x * 32, y * 32))

        screen.blit(text_surface, text_rect)  # Blit the current portion of the text
        pygame.display.update()  # Update the entire screen to reflect changes

        for event in pygame.event.get():  # Additional event processing within the main loop
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.time.delay(800)  # Hold the completed text on screen for 2 seconds after typing completes
    # Fade-out effect
    fade_surface = pygame.Surface((scaled_width, scaled_height))
    fade_surface.fill((0, 0, 0))
    for alpha in range(0, 255, 5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)  # Delay to control the speed of the fade effect



def main():
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode((SCALED_WIDTH, SCALED_HEIGHT))
    sound = Sound()
    dashboard = Dashboard("./img/font.png:./img/font-red.png", 8, screen)
    
    level = Level(screen, sound, dashboard)
    show_loading_screen(screen,SCALED_WIDTH, SCALED_HEIGHT,level,sound)  # Call the loading screen function
    max_frame_rate = 60
    
    menu = Menu(screen, dashboard, level, sound)

    while not menu.start:
        menu.update()

    mario = Mario(0, 0, level, screen, dashboard, sound)
    clock = pygame.time.Clock()

    while not mario.restart:
        pygame.display.set_caption(f"Super Mario running with {int(clock.get_fps()):d} FPS")
        if mario.pause:
            mario.pauseObj.update()
        else:
            level.drawLevel(mario.camera)
            dashboard.update()
            mario.update()
        pygame.display.update()
        clock.tick(max_frame_rate)
    return 'restart'

if __name__ == "__main__":
    exitmessage = 'restart'
    while exitmessage == 'restart':
        exitmessage = main()
