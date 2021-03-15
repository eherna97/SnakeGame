import pygame

GREEN = (57, 255, 20) # Color of the body pieces
class Node:
    # definition of what a Node member contains
    #
    # self : the instance of Node
    # data : data contained in the Node
    #
    def __init__(self, surface, x, y, state = False):
        self.x = x
        self.y = y
        self.surface = surface
        self.rect = pygame.draw.rect(surface, GREEN, [x, y, 20, 20])
        self.state = state # the nodes will start dead, alive once player starts moving
        self.next = None
    
    # retrieve the x position coordinate of the node
    #
    # self: the instance of the node
    #
    def get_x(self):
        return self.x
    
    # retrieves the y position coordinate of the node
    #
    # self : the instance of the node
    #
    def get_y(self):
        return self.y


    # function for printing a Node for debugging purposes 
    #
    # self : the instance of node
    #
    def node_print(self):
        print(self.state, end="")






