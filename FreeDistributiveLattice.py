"""
The free (bounded) distributive lattice on three generators

This program draws the free distributive lattice on three generators (hereafter FD3) as a 3d object using the Sage computer algebra system.
A more detailed description of the mathematics depicted in this program can be found here: https://youtu.be/Y-U_CTfDhro

Charlotte Aten (charlotte.aten@rochester.edu) 2018, updated 2020
"""

import sage.all
from sage.plot.plot3d.shapes import LineSegment,Sphere
from sage.combinat.posets.posets import Poset
from sage.functions.other import sqrt

# Create FD3 as a poset and view it.
P = Poset((range(20),[[0,1],[1,2],[1,3],[1,4],[2,5],[2,6],[3,5],[3,7],[4,6],[4,7],[5,8],[5,9],[6,9],[6,10],[7,9],[7,11],[8,12],[9,12],[9,13],[9,14],[10,13],[11,14],[12,15],[12,16],[13,15],[13,17],[14,16],[14,17],[15,18],[16,18],[17,18],[18,19]]))
P.show()

# Set some constants for brevity.
a = 1/(2*sqrt(3))
b = 1/2
c = 1/sqrt(3)

# List the vertices of the top cube.
cube0 = [(0,0,0),(1+a-b,a-b,c),(a-b,1+a-b,c),(-c,-c,c),(c,c,2*c),(1-a-b,-a-b,2*c),(-a-b,1-a-b,2*c),(0,0,3*c)]

# List the vertices of the bottom cube.
cube1 = [(0,0,0),(1+a-b,a-b,-c),(a-b,1+a-b,-c),(-c,-c,-c),(c,c,-2*c),(1-a-b,-a-b,-2*c),(-a-b,1-a-b,-2*c),(0,0,-3*c)]

# List the edges in the top cube.
edges0 = [(cube0[0],cube0[1]),(cube0[0],cube0[2]),(cube0[0],cube0[3]),(cube0[1],cube0[4]),(cube0[1],cube0[5]),(cube0[2],cube0[4]),(cube0[2],cube0[6]),(cube0[3],cube0[5]),(cube0[3],cube0[6]),(cube0[4],cube0[7]),(cube0[5],cube0[7]),(cube0[6],cube0[7])]

# List the edges in the bottom cube
edges1 = [(cube1[0],cube1[1]),(cube1[0],cube1[2]),(cube1[0],cube1[3]),(cube1[1],cube1[4]),(cube1[1],cube1[5]),(cube1[2],cube1[4]),(cube1[2],cube1[6]),(cube1[3],cube1[5]),(cube1[3],cube1[6]),(cube1[4],cube1[7]),(cube1[5],cube1[7]),(cube1[6],cube1[7])]

# List the spoke edges in the xy-plane corresponding to the generators.
edges2 = [(cube0[1],(2*(1+a-b),2*(a-b),0)),(cube1[1],(2*(1+a-b),2*(a-b),0)),(cube0[2],(2*(a-b),2*(1+a-b),0)),(cube1[2],(2*(a-b),2*(1+a-b),0)),(cube0[3],(-2*c,-2*c,0)),(cube1[3],(-2*c,-2*c,0))]

# Combine these together with the edges to the top and bottom elements of FD3.
edges = edges0+edges1+edges2+[((0,0,3*c),(0,0,3*c+1)),((0,0,-3*c),(0,0,-3*c-1))]

# Assemble the lattice as a 3d object whose vertices are spheres and whose edges are cylinders, all of radius 0.1.
L = None
for edge in edges:
    L += LineSegment(edge[0],edge[1],radius=0.1)
vertices = cube0+cube1[1:]+[(2*(1+a-b),2*(a-b),0),(2*(a-b),2*(1+a-b),0),(-2*c,-2*c,0),(0,0,3*c+1),(0,0,-3*c-1)]
for vert in vertices:
    L += Sphere(0.1).translate(vert)

# Display FD3.
L.show(viewer='jmol')

# View this using jmol in Sage and then right-click and export as stl.
# You will obtain a file that can be printed.
# This wire-frame model is too fine for me to print successfully but a solid model might work.
# In any case this exhibits a general technique for drawing models in Sage and obtaining printable stl files.