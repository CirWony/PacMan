import pygame
import random

BlinkyCount = 0
power_timer = 400

BlinkyLeft = [pygame.image.load('images/BlinkyLeft1.png'), pygame.image.load('images/BlinkyLeft2.png')]
BlinkyRight = [pygame.image.load('images/BlinkyRight1.png'), pygame.image.load('images/BlinkyRight2.png')]
BlinkyUp = [pygame.image.load('images/BlinkyUp1.png'), pygame.image.load('images/BlinkyUp2.png')]
BlinkyDown = [pygame.image.load('images/BlinkyDown1.png'), pygame.image.load('images/BlinkyDown2.png')]

InkeyLeft = [pygame.image.load('images/InkeyLeft1.png'), pygame.image.load('images/InkeyLeft2.png')]
InkeyRight = [pygame.image.load('images/InkeyRight1.png'), pygame.image.load('images/InkeyRight2.png')]
InkeyUp = [pygame.image.load('images/InkeyUp1.png'), pygame.image.load('images/InkeyUp2.png')]
InkeyDown = [pygame.image.load('images/InkeyDown1.png'), pygame.image.load('images/InkeyDown2.png')]

PinkyLeft = [pygame.image.load('images/PinkyLeft1.png'), pygame.image.load('images/PinkyLeft2.png')]
PinkyRight = [pygame.image.load('images/PinkyRight1.png'), pygame.image.load('images/PinkyRight2.png')]
PinkyUp = [pygame.image.load('images/PinkyUp1.png'), pygame.image.load('images/PinkyUp2.png')]
PinkyDown = [pygame.image.load('images/PinkyDown1.png'), pygame.image.load('images/PinkyDown2.png')]

ClydeLeft = [pygame.image.load('images/ClydeLeft1.png'), pygame.image.load('images/ClydeLeft2.png')]
ClydeRight = [pygame.image.load('images/ClydeRight1.png'), pygame.image.load('images/ClydeRight2.png')]
ClydeUp = [pygame.image.load('images/ClydeUp1.png'), pygame.image.load('images/ClydeUp2.png')]
ClydeDown = [pygame.image.load('images/ClydeDown1.png'), pygame.image.load('images/ClydeDown2.png')]

VulnerableGhost = [pygame.image.load('images/Blue1.png'), pygame.image.load('images/Blue2.png')]


class Blinky(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, level):
        super(Blinky, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/BlinkyLeft1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.level = level
        self.speedx = 3
        self.speedy = 3

        self.rand = None
        self.power_timer = 0

        # Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.wall_collide = False
        self.power = False

    def blinky_ai(self):
        current_time = pygame.time.get_ticks()

        if current_time % 300 == 0:
            self.rand = random.choice([1, 2, 3, 4])

        if self.rand == 1:
            self.speedx = 3 + self.level
            self.moving_right = True
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False

        elif self.rand == 2:
            self.speedx = 3 + self.level
            self.moving_right = False
            self.moving_left = True
            self.moving_up = False
            self.moving_down = False

        elif self.rand == 3:
            self.speedy = 3 + self.level
            self.moving_right = False
            self.moving_left = True
            self.moving_up = False
            self.moving_down = False

        elif self.rand == 4:
            self.speedy = 3 + self.level
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = True

        else:
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False

    def update(self):
        global BlinkyCount
        global power_timer

        if self.power:
            self.power_timer += 1
            self.speedx, self.speedy = 2, 2
            if self.power_timer >= power_timer:
                self.power = False
                self.power_timer = 0

        if self.moving_right:
            self.rect.centerx += self.speedx
            BlinkyCount += 1

        elif self.moving_left:
            self.rect.centerx -= self.speedx
            BlinkyCount += 1

        elif self.moving_up:
            self.rect.centery -= self.speedy
            BlinkyCount += 1

        elif self.moving_down:
            self.rect.centery += self.speedy
            BlinkyCount += 1

        else:
            BlinkyCount += 1

    def blitme(self):
        global BlinkyCount

        if BlinkyCount >= 30:
            BlinkyCount = 0

        if self.moving_right and not self.power:
            self.screen.blit(BlinkyRight[BlinkyCount//15], self.rect)
        elif self.moving_left and not self.power:
            self.screen.blit(BlinkyLeft[BlinkyCount//15], self.rect)
        elif self.moving_up and not self.power:
            self.screen.blit(BlinkyUp[BlinkyCount//15], self.rect)
        elif self.moving_down and not self.power:
            self.screen.blit(BlinkyDown[BlinkyCount//15], self.rect)
        else:
            self.screen.blit(BlinkyUp[BlinkyCount//15], self.rect)

        if self.power:
            self.screen.blit(VulnerableGhost[BlinkyCount // 15], self.rect)


class Inkey(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super(Inkey, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/InkeyLeft1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.speedx = 3
        self.speedy = 3

        self.rand = None
        self.power_timer = 0

        # Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.wall_collide = False
        self.power = False

    def blinky_ai(self):
        current_time = pygame.time.get_ticks()

        if current_time % 300 == 0:
            self.rand = random.choice([1, 2, 3, 4])

        if self.rand == 1:
            self.speedx = 3
            self.moving_right = True
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False

        elif self.rand == 2:
            self.speedx = 3
            self.moving_right = False
            self.moving_left = True
            self.moving_up = False
            self.moving_down = False

        elif self.rand == 3:
            self.speedy = 3
            self.moving_right = False
            self.moving_left = True
            self.moving_up = False
            self.moving_down = False

        elif self.rand == 4:
            self.speedy = 3
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = True

        else:
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False

    def update(self):
        global BlinkyCount
        global power_timer

        if self.power:
            self.power_timer += 1
            self.speedx, self.speedy = 2, 2
            if self.power_timer >= power_timer:
                self.power = False
                self.power_timer = 0

        if self.moving_right:
            self.rect.centerx += self.speedx
            BlinkyCount += 1

        elif self.moving_left:
            self.rect.centerx -= self.speedx
            BlinkyCount += 1

        elif self.moving_up:
            self.rect.centery -= self.speedy
            BlinkyCount += 1

        elif self.moving_down:
            self.rect.centery += self.speedy
            BlinkyCount += 1

        else:
            BlinkyCount += 1

    def blitme(self):
        global BlinkyCount

        if BlinkyCount >= 30:
            BlinkyCount = 0

        if self.moving_right and not self.power:
            self.screen.blit(InkeyRight[BlinkyCount//15], self.rect)
        elif self.moving_left and not self.power:
            self.screen.blit(InkeyLeft[BlinkyCount//15], self.rect)
        elif self.moving_up and not self.power:
            self.screen.blit(InkeyUp[BlinkyCount//15], self.rect)
        elif self.moving_down and not self.power:
            self.screen.blit(InkeyDown[BlinkyCount//15], self.rect)
        else:
            self.screen.blit(InkeyDown[BlinkyCount//15], self.rect)

        if self.power:
            self.screen.blit(VulnerableGhost[BlinkyCount // 15], self.rect)


class Pinky(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super(Pinky, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/PinkyLeft1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.speedx = 3
        self.speedy = 3

        self.rand = None
        self.power_timer = 0

        # Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.wall_collide = False
        self.power = False

    def blinky_ai(self):
        current_time = pygame.time.get_ticks()

        if current_time % 300 == 0:
            self.rand = random.choice([1, 2, 3, 4])

        if self.rand == 1:
            self.speedx = 3
            self.moving_right = True
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False

        elif self.rand == 2:
            self.speedx = 3
            self.moving_right = False
            self.moving_left = True
            self.moving_up = False
            self.moving_down = False

        elif self.rand == 3:
            self.speedy = 3
            self.moving_right = False
            self.moving_left = True
            self.moving_up = False
            self.moving_down = False

        elif self.rand == 4:
            self.speedy = 3
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = True

        else:
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False

    def update(self):
        global BlinkyCount
        global power_timer

        if self.power:
            self.power_timer += 1
            self.speedx, self.speedy = 2, 2
            if self.power_timer >= power_timer:
                self.power = False
                self.power_timer = 0

        if self.moving_right:
            self.rect.centerx += self.speedx
            BlinkyCount += 1

        elif self.moving_left:
            self.rect.centerx -= self.speedx
            BlinkyCount += 1

        elif self.moving_up:
            self.rect.centery -= self.speedy
            BlinkyCount += 1

        elif self.moving_down:
            self.rect.centery += self.speedy
            BlinkyCount += 1

        else:
            BlinkyCount += 1

    def blitme(self):
        global BlinkyCount

        if BlinkyCount >= 30:
            BlinkyCount = 0

        if self.moving_right and not self.power:
            self.screen.blit(PinkyRight[BlinkyCount // 15], self.rect)
        elif self.moving_left and not self.power:
            self.screen.blit(PinkyLeft[BlinkyCount // 15], self.rect)
        elif self.moving_up and not self.power:
            self.screen.blit(PinkyUp[BlinkyCount // 15], self.rect)
        elif self.moving_down and not self.power:
            self.screen.blit(PinkyDown[BlinkyCount // 15], self.rect)
        else:
            self.screen.blit(PinkyLeft[BlinkyCount // 15], self.rect)

        if self.power:
            self.screen.blit(VulnerableGhost[BlinkyCount // 15], self.rect)


class Clyde(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super(Clyde, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ClydeLeft1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.speedx = 3
        self.speedy = 3

        self.rand = None
        self.power_timer = 0

        # Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.wall_collide = False
        self.power = False

    def blinky_ai(self):
        current_time = pygame.time.get_ticks()

        if current_time % 300 == 0:
            self.rand = random.choice([1, 2, 3, 4])
            if self.rand == 1 or 2:
                self.speedx = 3
            elif self.rand == 3 or 4:
                self.speedy = 3

        if self.rand == 1:
            self.moving_right = True
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False

        elif self.rand == 2:
            self.moving_right = False
            self.moving_left = True
            self.moving_up = False
            self.moving_down = False

        elif self.rand == 3:
            self.moving_right = False
            self.moving_left = True
            self.moving_up = False
            self.moving_down = False

        elif self.rand == 4:
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = True

        else:
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False

    def update(self):
        global BlinkyCount
        global power_timer

        if self.power:
            self.power_timer += 1
            self.speedx, self.speedy = 2, 2
            if self.power_timer >= power_timer:
                self.power = False
                self.power_timer = 0

        if self.moving_right:
            self.rect.centerx += self.speedx
            BlinkyCount += 1

        elif self.moving_left:
            self.rect.centerx -= self.speedx
            BlinkyCount += 1

        elif self.moving_up:
            self.rect.centery -= self.speedy
            BlinkyCount += 1

        elif self.moving_down:
            self.rect.centery += self.speedy
            BlinkyCount += 1

        else:
            BlinkyCount += 1

    def blitme(self):
        global BlinkyCount

        if BlinkyCount >= 30:
            BlinkyCount = 0

        if self.moving_right and not self.power:
            self.screen.blit(ClydeRight[BlinkyCount//15], self.rect)
        elif self.moving_left and not self.power:
            self.screen.blit(ClydeLeft[BlinkyCount//15], self.rect)
        elif self.moving_up and not self.power:
            self.screen.blit(ClydeUp[BlinkyCount//15], self.rect)
        elif self.moving_down and not self.power:
            self.screen.blit(ClydeDown[BlinkyCount//15], self.rect)
        else:
            self.screen.blit(ClydeRight[BlinkyCount//15], self.rect)

        if self.power:
            self.screen.blit(VulnerableGhost[BlinkyCount//15], self.rect)
