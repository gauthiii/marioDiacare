import pygame

from classes.Font import Font


class Dashboard(Font):
    def __init__(self, filePath, size, screen,max_points=2000):
        Font.__init__(self, filePath, size)
        self.state = "menu"
        self.screen = screen
        self.levelName = ""
        self.points = 700
        self.points1 = 1200
        self.points2 = 0
        self.coins = 0
        self.ticks = 0
        self.time = 0
        self.max_points = max_points  # Maximum points to fill the progress bar



    def update(self):
        self.glucose_text_rect = self.drawText("GLUCOSE", 50, 20, 15)
        self.drawProgressBar(50, 45, 100, 10,"glucose")  # Drawing the progress bar below the points (chnaged 60 to 45)
        # self.drawText(self.pointString(), 50, 37, 15)
        if self.levelName != "":
            self.drawText(str(int(self.points*100/2000))+" %", 160, 44, 13)

            

        # self.drawText("@x{}".format(self.coinString()), 215, 37, 15)

        self.insulin_text_rect = self.drawText("INSULIN", 480, 20, 15)
        self.drawProgressBar(483, 45, 100, 10,"insulin") 
        # self.drawText(str(self.points), 395, 37, 15)

        if (self.points>1500):
            self.drawText("WARNING!!!", 215, 40, 10)
            self.drawText("GLUCOSE LEVEL IS HIGH", 215, 60, 10)

        # self.glucagon_text_rect = self.drawText("GLUCAGON", 495, 20, 15)
        # self.drawProgressBar(498, 45, 100, 10,"glucagon") 
        # if self.state != "menu":
        #     self.drawText(self.timeString(), 535, 37, 15)

        # update Time
        self.ticks += 1
        if self.ticks == 60:
            self.ticks = 0
            self.time += 1



    # def drawText(self, text, x, y, size):
    #     for char in text:
    #         charSprite = pygame.transform.scale(self.charSprites[char], (size, size))
    #         self.screen.blit(charSprite, (x, y))
    #         if char == " ":
    #             x += size//2
    #         else:
    #             x += size


    def drawText(self, text, x, y, size):
        bounds = pygame.Rect(x, y, 0, size)  # Initialize the bounds of the text
        for char in text:
            charSprite = pygame.transform.scale(self.charSprites[char], (size, size))
            self.screen.blit(charSprite, (x, y))
            if char == " ":
                x += size // 2
            else:
                x += size
            bounds.width += size  # Increase the width of the bounds for each character
        return bounds


    def drawProgressBar(self, x, y, width, height,text):
        # Draw background of the progress bar
        background_color = (50, 50, 50)  # Dark gray
        pygame.draw.rect(self.screen, background_color, [x, y, width, height])

        # Ensure that points do not exceed max_points
        current_points = min(self.points, self.max_points)

        # Calculate width of the filled part
        fill_width = 0
        fill_color=(0,0,0)
        if text=="glucose":
            current_points = min(self.points, self.max_points)
            fill_color = (0, 255, 0)  # Green
            fill_width = int((current_points / self.max_points) * width)
            if current_points >= 1500:
                fill_color = (255, 0, 0)  # Red
            else:
                fill_color = (0, 255, 0)  # Green
        elif text=="insulin":
            current_points = min(self.points1, self.max_points)
            fill_color = (255, 255, 0)  # Red
            fill_width = int((current_points / self.max_points) * width)
            fill_color = (255, 255, 0)  # Yellow
        else:
            current_points = min(self.points, self.max_points)
            fill_color = (255, 255, 0)  # Yellow
            fill_width = int((current_points / self.max_points) * width)*0.4
        pygame.draw.rect(self.screen, fill_color, [x, y, fill_width, height])
        


    def coinString(self):
        return "{:02d}".format(self.coins)

    def pointString(self):
        return "{:06d}".format(self.points)

    def timeString(self):
        return "{:03d}".format(self.time)
