# Ali Fırat ÖZEL - 18120205038

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

def rectA():
    glBegin(GL_QUADS)
    glVertex2f(220, 265)    #sol alt
    glVertex2f(420, 265)    #sağ alt
    glVertex2f(420, 315)    #sağ üst
    glVertex2f(220, 315)    #sol üst
    glEnd()

def rectB():
    glBegin(GL_QUADS)
    glVertex2f(270, 315)
    glVertex2f(370, 315)
    glVertex2f(370, 365)
    glVertex2f(270, 365)
    glEnd()

def diskA():
    posx, posy = 245, 240
    sides = 180
    radius = 100
    glBegin(GL_POLYGON)    
    for i in range(360):    
        cosine = radius * cos(i*pi/sides) + posx    
        sine  = radius * sin(i*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def diskB():
    posx, posy = 395, 240
    sides = 32
    radius = 25
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def drawCar():
    rectA()
    rectB()
    diskA()
    diskB()

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
  

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 500, 500)
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glutKeyboardFunc(keyPressed)
    drawCar()
    glutSwapBuffers()

width, height = 640, 480
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(width, height)
glutInitWindowPosition(100, 100)
glutCreateWindow("Hyper Car")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
