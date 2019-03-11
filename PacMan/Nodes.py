import pygame
from Constants import *


class Node(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.position = (x, y)

    def render(self, screen):
        pygame.draw.circle(screen, RED, self.position, 10)


index = 'a'
index1 = ord(index)
nodeList = []
nodeChar = []


class NodeGroup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.setup(x, y)
        self.nodeList = nodeList
        self.nodeChar = nodeChar

        self.image = pygame.image.load('images/pellet.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    @staticmethod
    def setup(x, y):
        global index1

        nodeList.append(Node(x, y))
        nodeChar.append(chr(index1))
        index1 += 1

    @staticmethod
    def render(screen):
        for node in nodeList:
            node.render(screen)
