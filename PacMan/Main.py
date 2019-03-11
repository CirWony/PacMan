import pygame
import random
from pygame import *
from operator import itemgetter
from pygame.sprite import Group

# Local Python Files
from Text import Text
from Map import result
from Player import Player
from Wall import Wall, Pellet, Shield, Power, PortalB, PortalO, Fruits
from Ghosts import Blinky, Inkey, Pinky, Clyde
from Constants import *
from Nodes import NodeGroup

SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()

titleFONT = 'fonts/PAC-FONT.TTF'
FONT = 'fonts/FLORIAN.otf'

animation_count = 0


class MainLoop(object):

    def __init__(self):
        pygame.init()

        self.clock = time.Clock()
        self.screen = SCREEN
        pygame.display.set_caption('PacMan')

        # Images
        self.background = pygame.transform.scale(pygame.image.load('images/wallpaper.jpg'), (SCREEN_W, SCREEN_H + 20))
        self.shield = pygame.transform.scale(image.load('images/shield.png'), (15, 25))

        # Texts
        self.titleText = Text(titleFONT, 70, 'PacMan', YELLOW, 255, 125)
        self.titleText1 = Text(FONT, 25, 'Press "P" to play', YELLOW, 320, 215)
        self.titleText2 = Text(FONT, 25, 'Press "H" to see high scores', YELLOW, 240, 615)

        self.titleBlinky = Text(FONT, 50, 'Blinky', RED, 350, 475)
        self.titleInkey = Text(FONT, 50, 'Inkey', CYAN, 370, 475)
        self.titlePinky = Text(FONT, 50, 'Pinky', PINK, 370, 475)
        self.titleClyde = Text(FONT, 50, 'Clyde', ORANGE, 370, 475)

        self.hsText = Text(FONT, 60, 'High Scores', YELLOW, 200, 125)
        self.hsText1 = Text(FONT, 25, 'Press "ESC" to go back', YELLOW, 230, 615)
        self.hsInGame = Text(FONT, 20, 'Score: ', YELLOW, 695, 65)
        self.levelText = Text(FONT, 20, 'Level: ', YELLOW, 90, 65)
        self.loseText = Text(FONT, 70, 'GAME OVER', YELLOW, 255, 125)

        # Menus
        self.mainScreen = True
        self.highScore = False
        self.startGame = False
        self.gameOver = False

        # Groups
        self.vertical_wall = Group()
        self.horizontal_wall = Group()
        self.corner_wall = Group()
        self.shield = Group()
        self.pellet_group = Group()
        self.pellet_group_initial = Group()
        self.player_group = Group()
        self.fruit_group = Group()

        self.Blinky_g = Group()
        self.Inkey_g = Group()
        self.Pinky_g = Group()
        self.Clyde_g = Group()
        self.ghost_group = Group(self.Blinky_g, self.Inkey_g, self.Pinky_g, self.Clyde_g)

        self.power_group = Group()
        self.node_group = Group()
        self.portal_groupO = Group()
        self.portal_groupB = Group()

        # Make python happy
        self.score = 0
        self.level = 1
        self.lives = 3
        self.sounds = None
        self.noteIndex = None
        self.player = None
        self.Blinky = None
        self.Inkey = None
        self.Pinky = None
        self.Clyde = None
        self.wall = None
        self.pellet = None

        # Testing
        self.nodes = NodeGroup(0, 0)
        self.position = None

    def reset(self):
        self.score = 0
        self.level = 1
        self.lives = 3
        self.player = None
        self.Blinky = None
        self.Inkey = None
        self.Pinky = None
        self.Clyde = None
        self.pellet_group.empty()
        self.player_group.empty()
        self.ghost_group.empty()
        self.fruit_group.empty()
        self.pellet = None

    def set_position(self):
        self.position = self.nodes.nodeList[0]

    def create_audio(self):
        self.sounds = {}

        for sound_name in ['pacman_chomp', 'pacman_beginning', 'pacman_death']:
            self.sounds[sound_name] = mixer.Sound('sounds/' + '{}.wav'.format(sound_name))
            self.sounds[sound_name].set_volume(0.1)

        self.noteIndex = 0

    def draw_pellets(self, level):
        for x in range(len(level)):
            for y in range(len(level[x])):
                for z in range(len(level[x][y])):
                    character = level[x][y][z]
                    x_pos = 810 - (z * 15)
                    y_pos = 90 + (x * 15)

                    if character == "-":
                        self.pellet_group.add(Pellet(self.screen, x_pos, y_pos))
                        self.pellet_group_initial.add(Pellet(self.screen, x_pos, y_pos))
                    if character == "|":
                        self.pellet_group.add(Pellet(self.screen, x_pos, y_pos))
                        self.pellet_group_initial.add(Pellet(self.screen, x_pos, y_pos))
                    if character == "N":
                        self.pellet_group.add(Pellet(self.screen, x_pos, y_pos))
                        self.pellet_group_initial.add(Pellet(self.screen, x_pos, y_pos))
                    if character == "F":
                        select = random.randint(1, 3)
                        self.fruit_group.add(Fruits(self.screen, x_pos, y_pos, select))

    def draw_chars(self, level):
        for x in range(len(level)):
            for y in range(len(level[x])):
                for z in range(len(level[x][y])):
                    character = level[x][y][z]
                    x_pos = 810 - (z * 15)
                    y_pos = 90 + (x * 15)

                    if character == "M":
                        self.player = Player(self.screen, x_pos, y_pos - 3)
                        self.player_group.add(self.player)
                    if character == "B":
                        self.Blinky = Blinky(self.screen, x_pos, y_pos, self.level)
                        self.Blinky_g.add(self.Blinky)
                    if character == "I":
                        self.Inkey = Inkey(self.screen, x_pos, y_pos)
                        self.Inkey_g.add(self.Inkey)
                    if character == "P":
                        self.Pinky = Pinky(self.screen, x_pos, y_pos)
                        self.Pinky_g.add(self.Pinky)
                    if character == "C":
                        self.Clyde = Clyde(self.screen, x_pos, y_pos)
                        self.Clyde_g.add(self.Clyde)
        self.ghost_group.add(self.Blinky_g, self.Clyde_g, self.Pinky_g, self.Inkey_g)

    def draw_map(self, level):
        for row in range(len(level)):
            for y in range(len(level[row])):
                for col in range(len(level[row][y])):
                    character = level[row][y][col]
                    x_pos = 810 - (col * 15)
                    y_pos = 90 + (row * 15)

                    if character == "0":
                        self.vertical_wall.add(Wall(self.screen, x_pos, y_pos))
                    if character == "H":
                        self.horizontal_wall.add(Wall(self.screen, x_pos, y_pos))
                    if character == "S":
                        self.shield.add(Shield(self.screen, x_pos, y_pos))
                    if character == "+":
                        self.power_group.add(Power(self.screen, x_pos - 12, y_pos - 12))
                    if character == "N":
                        self.node_group.add(NodeGroup(x_pos + 15, y_pos + 15))
                    if character == "@":
                        self.portal_groupO.add(PortalO(self.screen, x_pos, y_pos))
                    if character == "$":
                        self.portal_groupB.add(PortalB(self.screen, x_pos, y_pos))

    def get_pathing(self):
        if pygame.sprite.groupcollide(self.player_group, self.node_group, False, False):
            # print(self.player.rect.centerx)
            pass

    def key_presses(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit()
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.player.speedx = 3
                self.player.moving_right = True
                self.player.moving_left = False
                self.player.moving_up = False
                self.player.moving_down = False
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.player.speedx = 3
                self.player.moving_right = False
                self.player.moving_left = True
                self.player.moving_up = False
                self.player.moving_down = False
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.player.speedy = 3
                self.player.moving_right = False
                self.player.moving_left = False
                self.player.moving_up = True
                self.player.moving_down = False
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                self.player.speedy = 3
                self.player.moving_right = False
                self.player.moving_left = False
                self.player.moving_up = False
                self.player.moving_down = True

    def check_ghost_collision(self):
        if pygame.sprite.groupcollide(self.Blinky_g, self.vertical_wall, False, False):
            self.Blinky.speedx = 0
        elif pygame.sprite.groupcollide(self.Blinky_g, self.horizontal_wall, False, False):
            self.Blinky.speedy = 0

        elif pygame.sprite.groupcollide(self.Pinky_g, self.vertical_wall, False, False):
            self.Pinky.speedx = 0
        elif pygame.sprite.groupcollide(self.Pinky_g, self.horizontal_wall, False, False):
            self.Pinky.speedy = 0

        elif pygame.sprite.groupcollide(self.Inkey_g, self.vertical_wall, False, False):
            self.Inkey.speedx = 0
        elif pygame.sprite.groupcollide(self.Inkey_g, self.horizontal_wall, False, False):
            self.Inkey.speedy = 0

        elif pygame.sprite.groupcollide(self.Clyde_g, self.vertical_wall, False, False):
            self.Clyde.speedx = 0
        elif pygame.sprite.groupcollide(self.Clyde_g, self.horizontal_wall, False, False):
            self.Clyde.speedy = 0

    def check_events(self):
        self.key_presses()
        self.get_pathing()
        self.check_ghost_collision()
        if pygame.sprite.groupcollide(self.player_group, self.pellet_group, False, True):
            self.sounds['pacman_chomp'].play()
            self.score += 10
        if pygame.sprite.groupcollide(self.player_group, self.fruit_group, False, True):
            self.sounds['pacman_chomp'].play()
            self.score += 200

        elif pygame.sprite.groupcollide(self.player_group, self.vertical_wall, False, False):
            self.player.speedx = 0
            if self.player.moving_right:
                self.player.rect.centerx -= 1
            elif self.player.moving_left:
                self.player.rect.centerx += 1
        elif pygame.sprite.groupcollide(self.player_group, self.horizontal_wall, False, False):
            self.player.speedy = 0
            if self.player.moving_up:
                self.player.rect.y += 1
            elif self.player.moving_down:
                self.player.rect.y -= 1

        elif pygame.sprite.groupcollide(self.player_group, self.portal_groupB, False, False):
            self.player.rect.centerx = 100
        elif pygame.sprite.groupcollide(self.player_group, self.portal_groupO, False, False):
            self.player.rect.centerx = 750

        elif pygame.sprite.groupcollide(self.player_group, self.power_group, False, True):
            self.sounds['pacman_chomp'].play()
            self.score += 50

        elif pygame.sprite.groupcollide(self.player_group, self.ghost_group, False, False):
            self.sounds['pacman_death'].play()
            if self.lives <= 0:
                high_score_file = open('highscores.txt', 'a')
                high_score_file.write('\n' + 'You,' + str(self.score))
                high_score_file.close()
                self.reset()
                self.startGame = False
                self.gameOver = True
            else:
                self.lives -= 1
                self.ghost_group.empty()
                self.player_group.empty()
                self.draw_chars(result())

        if len(self.pellet_group) == len(self.pellet_group_initial) / 2:
            self.Blinky.speedx += 1
            self.Blinky.speedy += 1
        if len(self.pellet_group) <= 0:
            self.level += 1
            self.draw_chars(result())
            self.draw_pellets(result())
            self.sounds['pacman_beginning'].play()

    def draw_screen(self):
        self.check_events()
        self.Blinky.blinky_ai()
        self.check_events()
        self.Blinky.update()
        self.Blinky.blitme()

        self.check_events()
        self.Pinky.blinky_ai()
        self.check_events()
        self.Pinky.update()
        self.Pinky.blitme()

        self.check_events()
        self.Inkey.blinky_ai()
        self.check_events()
        self.Inkey.update()
        self.Inkey.blitme()

        self.check_events()
        self.Clyde.blinky_ai()
        self.check_events()
        self.Clyde.update()
        self.Clyde.blitme()

        self.player.update()
        self.player.blitme()

    def draw_stuff(self):
        self.screen.blit(self.background, (0, 0))
        self.hsInGame.draw(self.screen)
        Text(FONT, 20, str(self.score), YELLOW, 790, 67).draw(self.screen)
        self.levelText.draw(self.screen)
        Text(FONT, 20, str(self.level), YELLOW, 170, 67).draw(self.screen)

        scores = []
        with open('highscores.txt') as f:
            for line in f:
                name, score = line.split(',')
                score = int(score)
                scores.append((name, score))
        scores = sorted(scores, key=itemgetter(1), reverse=True)[:1]
        for name, score in scores:
            Text(FONT, 20, 'HighScore: ' + str(score), YELLOW, 355, 67).draw(self.screen)

    def intro_animation(self):
        global animation_count
        animation_count += 1

        if animation_count <= 200:
            self.Blinky = Blinky(self.screen, 450, 400, result())
            self.Blinky.update()
            self.Blinky.blitme()
            self.titleBlinky.draw(self.screen)
        elif animation_count <= 400:
            self.Pinky = Pinky(self.screen, 450, 400)
            self.Pinky.update()
            self.Pinky.blitme()
            self.titlePinky.draw(self.screen)
        elif animation_count <= 600:
            self.Inkey = Inkey(self.screen, 450, 400)
            self.Inkey.update()
            self.Inkey.blitme()
            self.titleInkey.draw(self.screen)
        elif animation_count <= 800:
            self.Clyde = Clyde(self.screen, 450, 400)
            self.Clyde.update()
            self.Clyde.blitme()
            self.titleClyde.draw(self.screen)
        else:
            animation_count = 0

    def start_menu_chase(self):
        if len(self.pellet_group) != 0:
            self.player.moving_right = True
            self.Blinky.moving_right = True
            self.Inkey.moving_right = True
            self.Pinky.moving_right = True
            self.Clyde.moving_right = True

        if pygame.sprite.groupcollide(self.player_group, self.pellet_group, False, True):
            self.player.moving_right = False
            self.player.moving_left = True

            self.Blinky.moving_right = False
            self.Blinky.power = True
            self.Inkey.moving_right = False
            self.Inkey.power = True
            self.Pinky.moving_right = False
            self.Pinky.power = True
            self.Clyde.moving_right = False
            self.Clyde.power = True

            self.Blinky.moving_left = True
            self.Inkey.moving_left = True
            self.Pinky.moving_left = True
            self.Clyde.moving_left = True

        self.Blinky.update()
        self.Pinky.update()
        self.Inkey.update()
        self.Clyde.update()

        self.Pinky.blitme()
        self.Inkey.blitme()
        self.Clyde.blitme()
        self.Blinky.blitme()

        self.player.update()
        self.player.blitme()
        self.pellet_group.update()

    def start_menu_init(self):
        self.player = Player(self.screen, 0, 350)
        self.player_group.add(self.player)
        self.pellet = Power(self.screen, 850, 340)
        self.pellet_group.add(self.pellet)

        self.Blinky = Blinky(self.screen, -50, 350, result())
        self.Inkey = Inkey(self.screen, -100, 350)
        self.Pinky = Pinky(self.screen, -150, 350)
        self.Clyde = Clyde(self.screen, -200, 350)

    def main(self):
        count = 0
        self.create_audio()
        self.start_menu_init()
        while True:
            # Main Screen Menu
            if self.mainScreen:
                count += 1
                self.screen.blit(self.background, (0, 0))
                self.titleText.draw(self.screen)
                self.titleText1.draw(self.screen)
                self.titleText2.draw(self.screen)

                if count <= 700:
                    self.start_menu_chase()
                elif count <= 1500:
                    self.intro_animation()
                else:
                    self.start_menu_init()
                    count = 0

                pygame.display.update()
                for events in pygame.event.get():
                    if events.type == pygame.QUIT:
                        exit()
                    if pygame.key.get_pressed()[pygame.K_h]:
                        print('Accessing high scores...')
                        self.screen.blit(self.background, (0, 0))
                        scores = []
                        x = 0
                        with open('highscores.txt') as f:
                            for line in f:
                                name, score = line.split(',')
                                score = int(score)
                                scores.append((name, score))
                        scores = sorted(scores, key=itemgetter(1), reverse=True)[:10]
                        for name, score in scores:
                            if name == 'You':
                                Text(FONT, 15, name + ': ' + str(score), RED, 195, 230 + (35 * x)).draw(self.screen)
                            else:
                                Text(FONT, 15, name + ': ' + str(score), YELLOW, 195, 230 + (35 * x)).draw(self.screen)
                            pygame.display.update()
                            x += 1
                        self.mainScreen = False
                        self.highScore = True
                    if pygame.key.get_pressed()[pygame.K_p]:
                        self.mainScreen = False
                        self.startGame = True
                        self.reset()
                        print('Starting game...')
                        self.draw_chars(result())
                        self.draw_map(result())
                        self.draw_pellets(result())

                        self.set_position()
                        # self.player = Player(self.screen, self.position.x, self.position.y - 15)
                        # self.player_group.add(self.player)
                        self.sounds['pacman_beginning'].play()

            # High Score Menu
            elif self.highScore:
                self.hsText.draw(self.screen)
                self.hsText1.draw(self.screen)
                pygame.display.update()
                for events in pygame.event.get():
                    if events.type == pygame.QUIT:
                        exit()
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        print('Returning to Main menu...')
                        self.mainScreen = True
                        self.highScore = False
                    if pygame.key.get_pressed()[pygame.K_p]:
                        print('Starting game...')
                        self.highScore = False
                        self.startGame = True

            # Start Game
            elif self.startGame:
                self.draw_stuff()

                # self.nodes.render(self.screen)

                self.vertical_wall.draw(self.screen)
                self.horizontal_wall.draw(self.screen)
                self.pellet_group.draw(self.screen)
                self.fruit_group.draw(self.screen)
                self.shield.draw(self.screen)
                self.power_group.draw(self.screen)
                self.portal_groupO.draw(self.screen)
                self.portal_groupB.draw(self.screen)
                self.draw_screen()
                self.check_events()
                pygame.display.update()

            # Game Over Menu
            elif self.gameOver:
                self.reset()
                self.screen.blit(self.background, (0, 0))
                self.loseText.draw(self.screen)
                self.hsText1.draw(self.screen)
                pygame.display.update()
                for events in pygame.event.get():
                    if events.type == pygame.QUIT:
                        exit()
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        print('Returning to Main menu...')
                        self.mainScreen = True
                        self.highScore = False
                        self.gameOver = False


if __name__ == '__main__':
    game = MainLoop()
    game.main()
