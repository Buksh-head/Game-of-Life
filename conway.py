# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import signal
import rle


'''
Part B
Looks like glider from the lecture examples. By analysis using glider_simple
you can see the rules work and the pattern repeats and gliders are made

Part C
There was a duplication of +17 for an alive cell, tried change in to 16, then
tried 18 and that worked after running glider example.

Part H
GoL is Turing complete - anything that can be computed algorithmically can be 
computed within Conway's Game of Life. Gliders like signals, and interactions 
between them is like logic gate.

From the link we can see in the videos provided that it can simulate a turning
machine that can read, write and move to the next state which simulates a 
turning machine.

it take 11k plus generations for one cycle

reference theory of turing machine and different componets of the turing machine
pattern provided using this link "http://rendell-attic.org/gol/tm.htm" 
'''


class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.int64)
        self.neighborhood = np.ones((3,3), np.int64) # 8 connected kernel
        self.neighborhood[1,1] = 0 #do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        
    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid
    
    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()
               
    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''
        #get weighted sum of neighbors
        #PART A & E CODE HERE 
        
        # weighted_sum = np.zeros_like(self.grid)
        # for i in range(self.grid.shape[0]): #Rows
        #     for j in range(self.grid.shape[1]): #Columns
        #         for k in [-1, 0, 1]: #Neighbor rows
        #             for l in [-1, 0, 1]: #Neighbor columns
        #                 if k == 0 and l == 0:
        #                     continue # Center
        #                 x = (i + k) % self.grid.shape[0]
        #                 y = (j + l) % self.grid.shape[1]
        #                 weighted_sum[i, j] += self.grid[x, y]
        
        #Part E
        weighted_sum = signal.convolve2d(self.grid, self.neighborhood, mode='same', boundary='wrap')


        #implement the GoL rules by thresholding the weights
        #PART A CODE HERE
        self.grid = np.where((self.grid == 1) & ((weighted_sum < 2) | (weighted_sum > 3)), self.deadValue, self.grid)
        self.grid = np.where((self.grid == 1) & ((weighted_sum == 2) | (weighted_sum == 3)), self.aliveValue, self.grid)
        self.grid = np.where((weighted_sum == 3) & (self.grid == 0), self.aliveValue, self.grid) 
        
        #update the grid
#        self.grid = #UNCOMMENT THIS WITH YOUR UPDATED GRID
    
    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        
    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue
        
    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0]+1, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+2, index[1]+23] = self.aliveValue
        self.grid[index[0]+2, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+3, index[1]+13] = self.aliveValue
        self.grid[index[0]+3, index[1]+14] = self.aliveValue
        self.grid[index[0]+3, index[1]+21] = self.aliveValue
        self.grid[index[0]+3, index[1]+22] = self.aliveValue
        self.grid[index[0]+3, index[1]+35] = self.aliveValue
        self.grid[index[0]+3, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+4, index[1]+12] = self.aliveValue
        self.grid[index[0]+4, index[1]+16] = self.aliveValue
        self.grid[index[0]+4, index[1]+21] = self.aliveValue
        self.grid[index[0]+4, index[1]+22] = self.aliveValue
        self.grid[index[0]+4, index[1]+35] = self.aliveValue
        self.grid[index[0]+4, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+5, index[1]+1] = self.aliveValue
        self.grid[index[0]+5, index[1]+2] = self.aliveValue
        self.grid[index[0]+5, index[1]+11] = self.aliveValue
        self.grid[index[0]+5, index[1]+17] = self.aliveValue
        self.grid[index[0]+5, index[1]+21] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue
        
        self.grid[index[0]+6, index[1]+1] = self.aliveValue
        self.grid[index[0]+6, index[1]+2] = self.aliveValue
        self.grid[index[0]+6, index[1]+11] = self.aliveValue
        self.grid[index[0]+6, index[1]+15] = self.aliveValue
        self.grid[index[0]+6, index[1]+17] = self.aliveValue
        #Duplicated 17 changed to 18
        self.grid[index[0]+6, index[1]+18] = self.aliveValue
        self.grid[index[0]+6, index[1]+23] = self.aliveValue
        self.grid[index[0]+6, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+7, index[1]+11] = self.aliveValue
        self.grid[index[0]+7, index[1]+17] = self.aliveValue
        self.grid[index[0]+7, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+8, index[1]+12] = self.aliveValue
        self.grid[index[0]+8, index[1]+16] = self.aliveValue
        
        self.grid[index[0]+9, index[1]+13] = self.aliveValue
        self.grid[index[0]+9, index[1]+14] = self.aliveValue
        
    def insertFromPlainText(self, txtString, pad=0):
        '''
        Assumes txtString contains the entire pattern as a human readable pattern without comments
        ''' 
        with open(txtString, 'r') as file:
            for i, line in enumerate(file):
                if line [0] == '!':
                    continue
                for j, char in enumerate(line.strip()):
                    if char == 'O':
                        self.grid[i+pad, j+pad] = self.aliveValue
                    else:
                        self.grid[i+pad, j+pad] = self.deadValue
        return self.grid


#Part f
    def insertFromRLE(self, rleString, pad=0):
        '''
        Given string loaded from RLE file, populate the game grid
        '''
        parsed = rle.RunLengthEncodedParser(rleString)

        data = parsed.human_friendly_pattern

        for i, line in enumerate(data.split('\n')):
            for j, char in enumerate(line):
                if char == '.':
                    self.grid[i+pad, j+pad] = self.deadValue
                else:
                    self.grid[i+pad, j+pad] = self.aliveValue
        return self.grid


            
        
        