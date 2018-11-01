# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 13:28:16 2018

@author: HAL900
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing

class Queue(object):
    
    def __init__(self):
        self.tail = None
        self.head = None
        
    
    def isEmpty(self):
        return self.tail == None
    
    def put(self, x):
        n = Node(x)
        n.next = None
        if self.tail == None:
            self.tail = n
            self.head = n
        else:
            self.tail.next = n
            self.tail = self.tail.next
            
        
    def get(self):
        if self.head != None:
            tmp = Node(self.head.val)
            self.head = self.head.next
            return (str)(tmp.val)
        else:
            if self.tail != None:
                self.tail = None
            return None
        
    
    def __str__(self):
        return "{}".format(self.Q)
    
