from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import keyboard
import sys

w = 500
h = 500

def keyPressed(*args):
    print(args[0])
    #Escape code=\x1b
    if args[0] == b"\x1b" or args[0] == bytes('q', 'utf-8'):
        glEnd()
        sys.exit()
    elif args[0] == bytes('r', 'utf-8'):
        glColor3f(255.0, 0.0, 0.0)
    elif args[0] == bytes('g', 'utf-8'):
        glColor3f(0, 255.0, 0.0)
    elif args[0] == bytes('b', 'utf-8'):
            glColor3f(0.0, 0.0, 255.0)
    glutPostRedisplay()

def DrawQuad_1(): #arabanın alt tarafı
    glBegin(GL_QUADS)
    glutPostRedisplay()
    glVertex2f(100, 150)
    glVertex2f(200, 150)
    glVertex2f(200, 225)
    glVertex2f(100, 225)
    glEnd()

def DrawFrame_1(): #siyah çerçevelerin oluşmasını sağlar
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(100, 150)
    glVertex2f(200, 150)
    glVertex2f(200, 225)
    glVertex2f(100, 225)
    glEnd()

def DrawQuad_2(): #arabanın alt tarafı
    glBegin(GL_QUADS)
    glutPostRedisplay()
    glVertex2f(200, 150)
    glVertex2f(350, 150)
    glVertex2f(350, 225)
    glVertex2f(200, 225)
    glEnd()

def DrawFrame_2(): #siyah çerçevelerin oluşmasını sağlar
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(200, 150)
    glVertex2f(350, 150)
    glVertex2f(350, 225)
    glVertex2f(200, 225)
    glEnd()

def DrawQuad_3(): #arabanın camı
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.5, 1.0)
    glVertex2f(150, 225)
    glVertex2f(275, 225)
    glVertex2f(275, 285)
    glVertex2f(150, 285)
    glEnd()

def DrawFrame_3(): #siyah çerçevelerin oluşmasını sağlar
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    glColor3f(0.1, 0.0, 0.5)
    glVertex2f(150, 225)
    glVertex2f(275, 225)
    glVertex2f(275, 285)
    glVertex2f(150, 285)
    glEnd()

def circle_1(): #arabamızın tekerleği
    glColor3f(0.0, 0.0, 0.0)
    posx, posy = 150, 125
    sides = 32
    radius = 25
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine= radius * cos(i*2*pi/sides) + posx
        sine  = radius * sin(i*2*pi/sides) + posy
        glVertex2f(cosine,sine)
    glEnd()

def circle_2(): #arabamızın tekerleği
    glColor3f(0.0, 0.0, 0.0)
    posx, posy = 300, 125
    sides = 32
    radius = 25
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine= radius * cos(i*2*pi/sides) + posx
        sine  = radius * sin(i*2*pi/sides) + posy
        glVertex2f(cosine,sine)
    glEnd()

def resize():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def Screen():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    resize()
    glutKeyboardFunc(keyPressed)
    DrawQuad_1()
    DrawQuad_2()
    DrawQuad_3()
    DrawFrame_1()
    DrawFrame_2()
    DrawFrame_3()
    circle_1()
    circle_2()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("OpenGL ile Araba Yapımı")
    glutDisplayFunc(Screen)
    glutIdleFunc(Screen)
    glutMainLoop()

main()