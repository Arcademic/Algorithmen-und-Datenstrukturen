# -*- coding: utf-8 -*-

class Queue(object):
    
    def __init__(self, maxN):
        self.l = 0
        self.Q = maxN*[None]
    
    def isEmpty(self):
        return self.l == 0
    
    def put(self, x):
       if self.l < len(self.Q):
            self.Q[self.l] = x
            self.l = self.l + 1
        
    def get(self):
        tmp = None
        if self.l > 0:
            self.l = self.l - 1
            tmp = self.Q[0]
            for i in range(1,len(self.Q)):
                self.Q[i-1] = self.Q[i]
            self.Q[len(self.Q)-1] = None
        return tmp
    
    def __str__(self):
        return "{}".format(self.Q)

"""
l = 0
Q = leeres Array der Länge maxN vom Typ T

bool isEmpty():
    return l == 0

put(T x):
    if l < maxN:
        Q[l] = x
        l++

T get():
    tmp = NIL
    if l > 0:
        l--
        tmp = Q[0]
        for i=1 to maxN:
            Q[i-1] = Q[i]
        Q[maxN-1] = NIL
    return tmp
"""