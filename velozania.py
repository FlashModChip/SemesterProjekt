# import and Initialization
import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

# Display
SIZE = (800, 600)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(SIZE)
screen.fill(WHITE)

pygame.display.set_caption('VeloZania')


# Entities

# der Radler
class Cycler(pygame.sprite.Sprite):
    # Startkoordinaten
    x_cord = 40
    y_cord = 350

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/Cycler.png')
        self.image = pygame.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()

        self.rect.left = self.x_cord
        self.rect.top = self.y_cord

    def update(self):
        self.rect = (self.x_cord, self.y_cord)


class Auto(pygame.sprite.Sprite):
    # Startkoordinaten
    x_cord = 900
    y_cord = randint(250, 400) # Zufallposi für Position auf der rechten Spur

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/redcar.png')
        self.image = pygame.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()

        self.rect.left = self.x_cord
        self.rect.top = self.y_cord

    def bewegung(self):
        if self.x_cord > -110:
            self.x_cord -= 5 # geschwindigkeit des Autos / für Test eignet sich 30

    def update(self):
        self.rect = (self.x_cord, self.y_cord)


# Hintergrund
class Background(pygame.sprite.Sprite):
    def __init__(self):
        BLACK = (250, 250, 250)
        GREEN = (0, 255, 0)
        STREET = (150, 150, 150)
        # i = 0

        self.bg_gruen = pygame.draw.rect(screen, GREEN, (0, 100, 800, 400))
        self.bg_grau = pygame.draw.rect(screen, STREET, (0, 150, 800, 300))

        # hier würde ich gerne die Striche automatisch nach links bewegen lassen,
        # um somit die Bewegung zu des Radlers zu simmulieren (???)
        ## hab das Gefühl, dass die Schleife lags verursacht
        # while i <= 900:
        # self.bg_striche = pygame.draw.rect(screen, BLACK, (i, 300, 25, 5))
        #   i = i + 30
        self.bg_striche = pygame.draw.rect(screen, BLACK, (0, 300, 800, 5))


# Init des Radlers und Autos
car = Auto()
cycler = Cycler()
sprite_group = pygame.sprite.Group()
sprite_group.add(car)
sprite_group.add(cycler)


# Action --> Alter

# Assign Variables

# noch ungenutzt
pygame.time.set_timer(USEREVENT, 200)

# Loop
while True:

    # Timer
    FPS = 30
    fpsClock = pygame.time.Clock()
    fpsClock.tick(FPS)

    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #für die neue Positionierung des Autos vorn
        if car.x_cord <= -100:
            car.x_cord = randint(800, 2000)
            car.y_cord = randint(250, 400)


    # elif event.type == USEREVENT:

    car.bewegung()
    # refresh des Hintergrunds
    bg = Background()

    # Bewegen des Radlers
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if Cycler.y_cord >= 100:
            Cycler.y_cord -= 3
    elif keys[pygame.K_DOWN]:
        if Cycler.y_cord <= 380:
            Cycler.y_cord += 3

    sprite_group.update()
    sprite_group.draw(screen)

    # Redisplay
    pygame.display.update()
