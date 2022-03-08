from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math as m
import sys

def drawHalfSphere(radius, xPos, yPos, zPos):
    glPushMatrix()
    glBegin(GL_POLYGON)
    for i in range(180):
        for j in range(180):
            x = radius * m.cos(i * m.pi / 180) * m.sin(j * m.pi / 180) + xPos
            y = radius * m.sin(i * m.pi / 180) * m.sin(j * m.pi / 180) + yPos
            z = radius * m.cos(j * m.pi / 180) + zPos
            glVertex3d(x, y, z)
    glEnd()
    glPopMatrix()

def init():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1, 1, 1, 1)
    glOrtho(-5, 5, -5, 5, -5, 5)
    glLoadIdentity()
    drawHalfSphere(1, 0, 0, 0)
    glFlush()    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Sphere");
    glutDisplayFunc(init)
    glutIdleFunc(init)
    glutMainLoop()

main()



    
        


        

