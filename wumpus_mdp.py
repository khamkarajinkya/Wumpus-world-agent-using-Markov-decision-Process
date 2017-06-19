# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:01:22 2016

@author: Ajinkya
"""

from operator import itemgetter
import solver


class WumpusMDP:
    # wall_locations is a list of (x,y) pairs
    # pit_locations is a list of (x,y) pairs
    # wumnpus_location is an (x,y) pair
    # gold_location is an (x,y) pair
    # start_location is an (x,y) pair representing the start location of the agent


    def __init__(self, wall_locations, pit_locations, wumpus_location, gold_location, start_location):
        self.wall_locations = wall_locations
        self.pit_locations = pit_locations
        self.wumpus_location = wumpus_location
        self.gold_location = gold_location
        self.start_location = start_location
        self.wumpus_shot=False

    def A(self):
        return ["do nothing","left", "right", "up", "down","shoot right","shoot left","shoot down","shoot up"]

    def S(self):
        x = max(self.wall_locations, key=itemgetter(0))
        y = max(self.wall_locations, key=itemgetter(1))
        s = []
        a = ()
        for i in range(y[1] + 1):
            for j in range(x[0] + 1):
                a = (j, i)
                if a not in self.wall_locations:
                   s.append(a)
        return s

    def P(self, s, a, u):
        x,y=s
        l = (x,y-1)
        r= (x,y+1)
        up=(x-1,y)
        d = (x+1,y)
        if self.wumpus_shot==False:
            wx, wy = self.wumpus_location
            if a == 'shoot down' and wx > x and wy == y:
                #print ('Wumpus shot down from'+str(s)+'with wumpus in'+str(self.wumpus_location)+'with probability 1')
                self.wumpus_shot=True
                return 1
            if a == 'shoot up' and wx < x and wy == y:
                #print ('Wumpus shot up from'+str(s)+'with wumpus in'+str(self.wumpus_location)+'with probability 1')
                self.wumpus_shot=True
                return 1
            if a == 'shoot right' and wx == x and wy > y:
                #print ('Wumpus shot right from'+str(s)+'with wumpus in'+str(self.wumpus_location)+'with probability 1')
                self.wumpus_shot=True
                return 1
            if a == 'shoot left' and wx == x and wy < y:
                #print ('Wumpus shot left from'+str(s)+'with wumpus in'+str(self.wumpus_location)+'with probability 1')
                self.wumpus_shot=True
                return 1
        
        if a=='right' and u==r and u in self.wall_locations:
            return 0
        if a=='left' and u==l and u in self.wall_locations:
            return 0
        if a=='up' and u==up and u in self.wall_locations:
            return 0
        if a=='down' and u==d and u in self.wall_locations:
            return 0
            
        if a=='right' and u==r and u==self.gold_location:
            return 1
        if a=='right' and u in (up,d,l) and u==self.gold_location:
            return 0
        
        if a=='left' and u==l and u==self.gold_location:
            return 1
        if a=='right' and u in (r,d,up) and u==self.gold_location:
            return 0
            
        if a=='up' and u==up and u==self.gold_location:
            return 1
        if a=='right' and u in (l,d,r) and u==self.gold_location:
            return 0
            
        if a=='down' and u==d and u==self.gold_location:
            return 1
        if a=='right' and u in (up,l,r) and u==self.gold_location:
            return 0
        
        if (u in self.pit_locations and u in (r,l,up,d)):
            return 0
        if (u==self.wumpus_location and u in (r,l,up,d)):
            return 0
        if a == 'right' and u==r:
            return 0.9
        elif a == 'right' and u in (l,up,d):
            return 0.1
        if a == 'up' and u==up:
            return 0.9
        elif a == 'up' and u in (l,r,d):
            return 0.1
        if a == 'down' and u==d:
            return 0.9
        elif a == 'down' and u in (l,r,up):
            return 0.1
        if a == 'left' and u==l:
            return 0.9
        elif a == 'left' and u in (r,up,d):
            return 0.1
        if a == "do nothing" and s==self.gold_location and s==u:
            return 1
        elif a== "do nothing" and u in (l,r,up,d):
            return 0
        return 0

    def R(self, s):
        if s in self.pit_locations:
            return -100
        if self.wumpus_shot==False and s == self.wumpus_location:
            return -100
        if self.wumpus_shot and s==self.wumpus_location:
            return -1
        if s == self.gold_location:
            return 100
        return -1

    def initial_state(self):
        return self.start_location

    def gamma(self):
        return 0.99


# EXAMPLE USAGE:
mdp = WumpusMDP([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1)],
                [(2,2)], (1,2), (1, 1), (2, 1))
s = solver.Solver(mdp)
policy = s.solve()
print (policy)
