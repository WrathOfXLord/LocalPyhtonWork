import time
from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

year = 0
day = 0

start_time = time.time()

def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)


def display():
    
    t = time.time() - start_time
    year_period = 25.0                  # 5 seconds for simulating one year 
    year     = (t / year_period)
    day      = 365 * year
    moon_sid = (365 / 27.3) * year

    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glEnable( GL_DEPTH_TEST )
    
    glPushMatrix()
    glColor4f (1.0, 1.0, 0, 1)
    glutSolidSphere(1.0, 20, 16)             # sun
    glPopMatrix()

    glPushMatrix()
    glRotatef(year*360.0, 0.0, 1.0, 0.0)     # earth rotation around the sun 
    glTranslatef(3.0, 0.0, 0.0)              # earth location
    
    
    #glRotatef(day*360.0, 0.0, 1.0, 0.0)      # earth spinn
    #glRotatef(90-23.4, 1.0, 0.0, 0.0)        # earth axis
    glColor3f (0, 0, 1)                      # blue
    glutWireSphere(0.3, 10, 8)               # earth
    

    glPushMatrix()
    glRotatef(moon_sid*360.0, 0.0, 1.0, 0.0) # moon sidereal
    glTranslatef(1.0, 0.0, 0.0)              # distance moon to earth
    glRotatef(90, 1.0, 0.0, 0.0)
    

    glColor4f (0.4, 0.5, 0.6, 1)                         
    glutWireSphere(0.1, 10, 8)               # moon
    
    glPopMatrix()
    glPopMatrix()
    glutSwapBuffers()


def reshape(w, h):
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   gluPerspective(70.0, w/h, 1.0, 20.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition (100, 100)
glutCreateWindow("Transformation")
init ()
glutDisplayFunc(display)
glutIdleFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()