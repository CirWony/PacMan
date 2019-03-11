import pygame

goRight = [pygame.transform.scale(pygame.image.load('images/PacManR1.png'), (25, 25)),
           pygame.transform.scale(pygame.image.load('images/PacManR2.png'), (25, 25)),
           pygame.transform.scale(pygame.image.load('images/PacManR3.png'), (25, 25)),
           pygame.transform.scale(pygame.image.load('images/PacMan.png'), (25, 25))]

goLeft = [pygame.transform.scale(pygame.image.load('images/PacManL1.png'), (25, 25)),
          pygame.transform.scale(pygame.image.load('images/PacManL2.png'), (25, 25)),
          pygame.transform.scale(pygame.image.load('images/PacManL3.png'), (25, 25)),
          pygame.transform.scale(pygame.image.load('images/PacMan.png'), (25, 25))]

goUp = [pygame.transform.scale(pygame.image.load('images/PacManU1.png'), (25, 25)),
        pygame.transform.scale(pygame.image.load('images/PacManU2.png'), (25, 25)),
        pygame.transform.scale(pygame.image.load('images/PacManU3.png'), (25, 25)),
        pygame.transform.scale(pygame.image.load('images/PacMan.png'), (25, 25))]

goDown = [pygame.transform.scale(pygame.image.load('images/PacManD1.png'), (25, 25)),
          pygame.transform.scale(pygame.image.load('images/PacManD2.png'), (25, 25)),
          pygame.transform.scale(pygame.image.load('images/PacManD3.png'), (25, 25)),
          pygame.transform.scale(pygame.image.load('images/PacMan.png'), (25, 25))]

char = [pygame.image.load('images/PacMan.png')]
walkCount = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super(Player, self).__init__()
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('images/PacMan.png'), (25, 25))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y

        self.speedx = 3
        self.speedy = 3

        # Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.wall_collide = False

    def update(self):
        global walkCount

        if self.moving_right:
            self.rect.centerx += self.speedx
            walkCount += 1

        if self.moving_left:
            self.rect.centerx -= self.speedx
            walkCount += 1

        if self.moving_up:
            self.rect.centery -= self.speedy
            walkCount += 1

        if self.moving_down:
            self.rect.centery += self.speedy
            walkCount += 1

    def blitme(self):
        global walkCount

        if walkCount + 1 >= 24:
            walkCount = 0

        if self.moving_right:
            self.screen.blit(goRight[walkCount//6], self.rect)
        elif self.moving_left:
            self.screen.blit(goLeft[walkCount//6], self.rect)
        elif self.moving_up:
            self.screen.blit(goUp[walkCount//6], self.rect)
        elif self.moving_down:
            self.screen.blit(goDown[walkCount//6], self.rect)
        else:
            self.screen.blit(goLeft[3], self.rect)
