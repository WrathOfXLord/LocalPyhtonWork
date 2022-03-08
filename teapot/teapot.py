from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

def rectA():
    glBegin(GL_QUADS)
    glVertex2f(150, 275)    #sol alt
    glVertex2f(350, 275)    #sağ alt
    glVertex2f(350, 325)    #sağ üst
    glVertex2f(150, 325)    #sol üst
    glEnd()

def rectB():
    glBegin(GL_QUADS)
    glVertex2f(200, 325)
    glVertex2f(300, 325)
    glVertex2f(300, 375)
    glVertex2f(200, 375)
    glEnd()

def circleA():
    posx, posy = 175, 250
    sides = 32
    radius = 25
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine = radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def circleB():
    posx, posy = 325, 250
    sides = 32
    radius = 25
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

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

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glutKeyboardFunc(keyPressed)
    rectA()
    rectB()
    circleA()
    circleB()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()