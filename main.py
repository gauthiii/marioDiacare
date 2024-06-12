import pygame
from classes.Dashboard import Dashboard
from classes.Level import Level
from classes.Menu import Menu
from classes.Sound import Sound
from entities.Mario import Mario
from config import SCALED_WIDTH, SCALED_HEIGHT
import sys
#Hi Auntyy

# Global flag to determine if the loading screen should be shown
first_run = True

def drawBG(screen,level):
        
    mariox=2*32
    marioy=12*32

    koopax=17.5*32
    koopay=11*32
    # Drawing the background similar to the drawMenuBackground method
    for y in range(0, 13):
        for x in range(0, 20):
            screen.blit(level.sprites.spriteCollection.get("sky").image, (x * 32, y * 32))
    for y in range(13, 15):
        for x in range(0, 20):
            if x==5 or x==6 or x==9 or x==10:
                screen.blit(level.sprites.spriteCollection.get("sky").image, (x * 32, y * 32))
            else:
                screen.blit(level.sprites.spriteCollection.get("ground").image, (x * 32, y * 32))

    
    screen.blit(level.sprites.spriteCollection.get("mario_idle").image, (mariox, marioy))

    screen.blit(
        level.sprites.spriteCollection.get("cloud1_1").image, (4 * 32, 3 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("cloud1_2").image, (5 * 32, 3 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("cloud1_3").image, (6 * 32, 3 * 32)
    )

    screen.blit(
        level.sprites.spriteCollection.get("cloud2_1").image, (4 * 32, 4 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("cloud2_2").image, (5 * 32, 4 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("cloud2_3").image, (6 * 32, 4 * 32)
    )

    screen.blit(
        level.sprites.spriteCollection.get("cloud1_1").image, (13 * 32, 2 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("cloud1_2").image, (14 * 32, 2 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("cloud1_3").image, (15 * 32, 2 * 32)
    )

    screen.blit(
        level.sprites.spriteCollection.get("cloud2_1").image, (13 * 32, 3 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("cloud2_2").image, (14 * 32, 3 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("cloud2_3").image, (15 * 32, 3 * 32)
    )


    screen.blit(
        level.sprites.spriteCollection.get("pipeL").image, (5 * 32, 10 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("pipeR").image, (6 * 32, 10 * 32)
    )
    for i in range(11,15):
        screen.blit(
            level.sprites.spriteCollection.get("pipe2L").image, (5 * 32, i * 32)
        )
        screen.blit(
            level.sprites.spriteCollection.get("pipe2R").image, (6 * 32, i * 32)
        )


    screen.blit(
        level.sprites.spriteCollection.get("pipeL").image, (9 * 32, 12 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("pipeR").image, (10 * 32, 12 * 32)
    )
    for i in range(13,15):
        screen.blit(
            level.sprites.spriteCollection.get("pipe2L").image, (9 * 32, i * 32)
        )
        screen.blit(
            level.sprites.spriteCollection.get("pipe2R").image, (10 * 32, i * 32)
        )


    screen.blit(
            level.sprites.spriteCollection.get("bush_1").image, (13 * 32, 12 * 32)
        )
    screen.blit(
        level.sprites.spriteCollection.get("bush_2").image, (14 * 32, 12 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("bush_2").image, (15 * 32, 12 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("bush_2").image, (16 * 32, 12 * 32)
    )
    screen.blit(
        level.sprites.spriteCollection.get("bush_3").image, (17 * 32, 12 * 32)
    )

    screen.blit(pygame.transform.scale(pygame.image.load('./img/icons/Apple.png').convert_alpha(), (32, 32)), (7.5*32, 12*32))

    screen.blit(pygame.transform.scale(pygame.image.load('./img/icons/Coke.png').convert_alpha(), (32*2, 32*2)), (koopax, koopay))

def show_loading_screen(screen, scaled_width, scaled_height, level, sound):
    font = pygame.font.Font('SuperMario256.ttf', 24)
    full_text = "An Adaptation of Super Mario "
    displayed_text = ""

    # Define the main text color and the stroke color
    text_color = (255, 255, 255)  # White
    stroke_color = (0, 0, 0)  # Black
    stroke_width = 2  # Width of the stroke

    text_surface = font.render("", True, text_color)
    text_rect = text_surface.get_rect(center=(scaled_width // 2, scaled_height // 2))

    clock = pygame.time.Clock()
    char_interval = 200

    for i in range(len(full_text) + 1):
        while pygame.time.get_ticks() % char_interval > 100:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.time.delay(25)
        displayed_text = full_text[:i]
        sound.play_sfx(sound.kick)
        # Create the text surfaces
        text_surface = font.render(displayed_text, True, text_color)
        stroke_surface = font.render(displayed_text, True, stroke_color)

        # Create surfaces with strokes by blitting the stroke text offset around the main text
        final_surface = pygame.Surface(text_surface.get_size(), pygame.SRCALPHA)
        for dx in range(-stroke_width, stroke_width + 1):
            for dy in range(-stroke_width, stroke_width + 1):
                if dx * dx + dy * dy <= stroke_width * stroke_width:
                    final_surface.blit(stroke_surface, (dx + stroke_width, dy + stroke_width))

        final_surface.blit(text_surface, (stroke_width, stroke_width))
        text_rect = final_surface.get_rect(center=(scaled_width // 2, scaled_height // 2))

        drawBG(screen, level)

        screen.blit(final_surface, text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.time.delay(800)

    full_text = "Designed by Ashika Ramesh "
    displayed_text = ""

    for i in range(len(full_text) + 1):
        while pygame.time.get_ticks() % char_interval > 100:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.time.delay(25)
        displayed_text = full_text[:i]
        sound.play_sfx(sound.kick)
        text_surface = font.render(displayed_text, True, text_color)
        stroke_surface = font.render(displayed_text, True, stroke_color)

        final_surface = pygame.Surface(text_surface.get_size(), pygame.SRCALPHA)
        for dx in range(-stroke_width, stroke_width + 1):
            for dy in range(-stroke_width, stroke_width + 1):
                if dx * dx + dy * dy <= stroke_width * stroke_width:
                    final_surface.blit(stroke_surface, (dx + stroke_width, dy + stroke_width))

        final_surface.blit(text_surface, (stroke_width, stroke_width))
        text_rect = final_surface.get_rect(center=(scaled_width // 2, scaled_height // 2))

        drawBG(screen, level)

        screen.blit(final_surface, text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.time.delay(800)
    fade_surface = pygame.Surface((scaled_width, scaled_height))
    fade_surface.fill((0, 0, 0))
    for alpha in range(0, 255, 5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)




def main():
    global first_run
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode((SCALED_WIDTH, SCALED_HEIGHT))
    sound = Sound()
    dashboard = Dashboard("./img/font.png:./img/font-red.png", 8, screen)
    
    level = Level(screen, sound, dashboard)

    if first_run:
        show_loading_screen(screen, SCALED_WIDTH, SCALED_HEIGHT, level, sound)
        first_run = False  # Set the flag to False after the first run
        
    max_frame_rate = 60
    
    menu = Menu(screen, dashboard, level, sound)

    while not menu.start:
        menu.update()

    mario = Mario(0, 0, level, screen, dashboard, sound)
    clock = pygame.time.Clock()

    while not mario.restart:
        pygame.display.set_caption(f"Super Mario running with {int(clock.get_fps()):d} FPS")
        # if mario.speed:
        #     print("SSSLLOOOOOOOWWWWWWW")
        #     max_frame_rate = 30
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
