from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

shape_vertices = []


def readObj():
    my_file = open("angelDrop_fixed.txt", "r")
    lines = my_file.readlines()
    for l in lines:
        splitted_l = l.split(" ")
        if splitted_l[0] == 'v':
            shape_vertices.append([float(splitted_l[1]), float(splitted_l[2]), float(splitted_l[3])])

        print(splitted_l)        

    print("All vertices are read from file")

readObj()

