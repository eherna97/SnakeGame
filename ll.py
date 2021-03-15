from node import Node
import random


class LinkedList:
    
    # definition for a singly-linked linked-list
    #
    # self : the instance of LinkedList itself
    #
    def __init__(self, surface):
        x = random.randint(0, 800) // 20
        y = random.randint(0, 600) // 20
        self.head = Node(surface, x, y)
        self.length = 1
    
    # return the length of the linked-list itself
    # 
    # self : the instance of LinkedList itself
    #
    def ll_length(self):
        return self.length
    
    # inserts a node with specified data at the head of the linke-list
    #
    # self : the instance of LinkedList itself
    # data : the data that will be held by the node
    #
    def ll_insert(self, surface):
        new_node = Node(surface)
        new_node.next = self.head.next # link before unlinking head
        self.head.next = new_node # now unlink head and link to new
        self.length += 1 # increment length
    
    # traverses the linkedlist and searches for an occurance of data 
    # in the linked-list
    #
    # self : the instance of LinkedList itself
    # data : the data that will be held by the node
    #
    def ll_search(self, state):
        temp_node = self.head.next  # don't need head value, it is Null
        while temp_node != None:
            if temp_node.state == state:
                return temp_node  # return the node if the value is equal
            temp_node = temp_node.next
    
    # prints a LinkedList's members
    #
    # self : the instance of LinkedList itself
    #
    def ll_print(self):
        temp_node = self.head.next  # don't need to print head, go to next
        while temp_node != None:
            temp_node.node_print()
            print(" -> ", end="")
            temp_node = temp_node.next  # move to the next node
        print("\n")
