import random
import pygame


GREEN = (57, 255, 20)
class Node:
    
    # definition for the init of a Node object
    #
    # surface : he game surface as defined in main game file
    # x       : the x coordinate of the Node
    # y       : the y coordinate of the Node
    # state   : whether the Node is alive or not
    #
    def __init__(self, surface, x, y, state = False):
        self.x = x
        self.y = y
        self.image  = pygame.draw.rect(surface, GREEN, [x, y, 20, 20])
        self.state  = state
        self.next = None
    
    # defines the left movement of a single Node
    #
    def move_left(self):
        self.x -= 20
    
    # defines the right movement of a singe Node
    #
    def move_right(self):
        self.x += 20
    
    #defines the up movement of a single Node
    #
    def move_up(self):
        self.y += 20

    # defines the down movement of a single Node
    #
    def move_down(self):
        self.y -= 20


class LinkedList:
    
    # definition for a singly-linked linked-list
    #
    # surface : the surface on which the Nodes will be displayed
    #
    def __init__(self, surface):
        x = random.randint(0, 800) // 20
        y = random.randint(0, 600) // 20
        self.head = Node(surface, x, y)
        self.length = 1
    
    # return the length of the linked-list itself
    # 
    def ll_length(self):
        return self.length
    
    # inserts a node with specified data at the head of the linke-list
    #
    # surface : the surface that the Node will be added to
    #
    def ll_insert(self, surface):
        new_node = Node(surface, self.head.get_x(), self.head.get_y())
        new_node.next = self.head.next # link before unlinking head
        self.head.next = new_node # now unlink head and link to new
        self.length += 1
    
    # traverses the linkedlist and searches for the state of the Node
    #
    # state : the state of the Node, dead or alive
    #
    def ll_search(self, state):
        temp_node = self.head.next
        while temp_node != None:
            if temp_node.state == state:
                return state  # return the state if the value is equal
            temp_node = temp_node.next
        return None

    # prints a LinkedList's members
    #
    def ll_print(self):
        temp_node = self.head.next
        while temp_node != None:
            temp_node.node_print()
            print(" -> ", end="")
            temp_node = temp_node.next  # move to the next node
        print("\n")
