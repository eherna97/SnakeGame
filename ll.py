import random
import pygame


class Node(pygame.sprite.Sprite):
    
    # definition for the init of a Node object
    #
    # color : the color of the Node
    # x     : the x coordinate of the Node
    # y     : the y coordinate of the Node
    # state : whether the Node is alive or not
    #
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        # drawing the instance of the Node
        self.image  = pygame.Surface([20, 20])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [x, y, 20, 20])
        self.rect = self.image.get_rect()
        # attributes of the Node
        self.rect.x = x
        self.rect.y = y
        self.next = None
    
    # defines movement of a Node in the x & y directions
    #
    # x : pixels moved in the x direction
    # y : pixels moved in the y direction
    #
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
    
    # retrieves the x coordinate of the invoking Node
    #
    def get_x(self):
        return self.rect.x

    # retrieves the y coordinate of the invoking Node
    #
    def get_y(self):
        return self.rect.y



class LinkedList:
    
    # definition for a singly-linked linked-list
    #
    # surface : the surface on which the Nodes will be displayed
    #
    def __init__(self, color, x, y):
        self.head = Node(color, x, y)
        self.length = 1
    
    # return the length of the linked-list itself
    # 
    def ll_length(self):
        return self.length
    
    # inserts a node with specified data at the head of the linke-list
    #
    # surface : the surface that the Node will be added to
    #
    def ll_insert(self, color, x, y):
        new_node = Node(color, x, y)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        #new_node.next = self.head.next # link before unlinking head
        #self.head.next = new_node # now unlink head and link to new
        self.length += 1
