# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway

N = 64

#Part E
#N = 1025

#create the game of life object
life = conway.GameOfLife(N)
#life.insertBlinker((0,0))
#life.insertGlider((0,0))
#life.insertGliderGun((0,0))


#PArt D
life.insertFromPlainText("snail.cells.txt", pad=15)
#life.insertFromPlainText("fireshiptagalong.cells.txt", pad=20)
#life.insertFromPlainText("clockinsertion.cells.txt")

cells = life.getStates() #initial state

#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True)

def animate(i):
    """perform animation step"""
    global life
    
    life.evolve()
    cellsUpdated = life.getStates()
    
    img.set_array(cellsUpdated)
    
    return img,

interval = 2 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
