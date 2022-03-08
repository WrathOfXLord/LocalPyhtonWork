import time
from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

start_time = time.time()
start_exec_time = time.time()

def drawAxis():
    '''
    Bu fonksiyon x ve y eksenlerini nokta şeklinde çizdiriyor.
    '''
    glColor3f(0, 1, 1)
    for i in range(-500, 500):
        glBegin(GL_POINTS)
        glVertex2f(i, 0)
        glVertex2f(0, i)
        glEnd()

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)

def display():
    global start_exec_time
    exec_time = time.time() - start_exec_time
    day      = 1.674 * (exec_time / 24) * 3
    year     = (day * 365)
    earth_spin = day * 10.700
    
    moon_spin = year * (365 / 30) * 0.003

    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glEnable( GL_DEPTH_TEST )
    
    glPushMatrix()
    glColor4f (1.0, 1.0, 0, 1)
    glutSolidSphere(1.0, 20, 16)             # sun
    glPopMatrix()

    glPushMatrix()
    glRotatef(year, 0.0, 1.0, 0.0)     # earth rotation around the sun 
    glTranslatef(3.0, 0.0, 0.0)              # earth location
    
    
    glRotatef(earth_spin, 0.0, 1.0, 0.0)      # earth spinn
    #glRotatef(90-23.4, 1.0, 0.0, 0.0)        # earth axis
    glColor3f (0, 0, 1)                      # blue
    glutWireSphere(0.3, 10, 8)               # earth
    

    glPushMatrix()
    glRotatef(moon_spin, 0.0, 1.0, 0.0) # moon sidereal
    glTranslatef(1.0, 0.0, 0.0)              # distance moon to earth
    glRotatef(90, 1.0, 0.0, 0.0)
    

    glColor4f (0.4, 0.5, 0.6, 1)                         
    glutWireSphere(0.1, 10, 8)               # moon
    
    glPopMatrix()
    glPopMatrix()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(1024, 768)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Rotate teapots")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    InitGL()
    glutMainLoop()

main()