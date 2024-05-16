import pygame

from classes.Font import Font


class Dashboard(Font):
    def __init__(self, filePath, size, screen,max_points=2000):
        Font.__init__(self, filePath, size)
        self.state = "menu"
        self.screen = screen
        self.levelName = ""
        self.points = 0
        self.coins = 0
        self.ticks = 0
        self.time = 0
        self.max_points = max_points  # Maximum points to fill the progress bar


    def update(self):
        self.drawText("MARIO", 50, 20, 15)
        self.drawProgressBar(50, 60, 100, 10)  # Drawing the progress bar below the points
        self.drawText(self.pointString(), 50, 37, 15)

        self.drawText("@x{}".format(self.coinString()), 225, 37, 15)

        self.drawText("SUGAR LEVEL", 340, 20, 15)
        self.drawText(str(self.levelName), 395, 37, 15)

        self.drawText("TIME", 520, 20, 15)
        if self.state != "menu":
            self.drawText(self.timeString(), 535, 37, 15)

        # update Time
        self.ticks += 1
        if self.ticks == 60:
            self.ticks = 0
            self.time += 1

    def drawText(self, text, x, y, size):
        for char in text:
            charSprite = pygame.transform.scale(self.charSprites[char], (size, size))
            self.screen.blit(charSprite, (x, y))
            if char == " ":
                x += size//2
            else:
                x += size

    def drawProgressBar(self, x, y, width, height):
        # Draw background of the progress bar
        background_color = (50, 50, 50)  # Dark gray
        pygame.draw.rect(self.screen, background_color, [x, y, width, height])

        # Calculate width of the filled part
        fill_width = int((self.points / self.max_points) * width)
        fill_color = (0, 255, 0)  # Green
        pygame.draw.rect(self.screen, fill_color, [x, y, fill_width, height])

    def coinString(self):
        return "{:02d}".format(self.coins)

    def pointString(self):
        return "{:06d}".format(self.points)

    def timeString(self):
        return "{:03d}".format(self.time)
