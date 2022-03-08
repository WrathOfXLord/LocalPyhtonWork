import time
from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

#kendi kendine dönebilmesi için zaman gibi sürekli
#değişen bir değere ihtiyaç var
start_exec_time = time.time()

def initGL(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)

def display():
    global start_exec_time
    #geçen süre
    exec_time = time.time() - start_exec_time
    day =  exec_time / 24 * 2   #dünya kendi ekseni etrafında dönüşü
    year = (day * 365)  #dünya güneş etrafında dönüşü
    earth_spin = day * 2    #dünya dönüş hızı
    sun_spin = day * 107    #güneş dönüş hızı
    moon_spin = earth_spin * 30 #ay dönüş hızı

    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glEnable( GL_DEPTH_TEST )
    
    #güneş
    glPushMatrix()
    glRotatef(sun_spin, 0.0, 0.0, 1.0)
    glColor3f (1, 0.75, 0)
    glutSolidSphere(1.0, 20, 16)     
    glPopMatrix()

    #dünya
    glPushMatrix()
    glRotatef(year, 0.0, 0.0, 1.0)
    glTranslatef(3.0, 0.0, 0.0)        
    glRotatef(earth_spin * 50, 0.0, 0.0, 1.0)
    glColor3f (0, 0.3, 0.45)
    glutSolidSphere(0.3, 10, 8)
    
    #ay
    glPushMatrix()
    glRotatef(moon_spin*12, 0.0, 0.0, 1.0)
    glTranslatef(1.0, 0.0, 0.0)
    glColor3f (0.6, 0.6, 0.6)                         
    glutSolidSphere(0.1, 10, 8)               
    glPopMatrix()
    glPopMatrix()
    glutSwapBuffers()


def ReSizeGLScene(Width, Height):
    if Height == 0:  # 0'a bölümü engellemek için
        Height = 1

    glViewport(0, 0, Width, Height)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(5.0, -5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(1024, 768)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Rotating Planes")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(ReSizeGLScene)
    initGL()
    glutMainLoop()

main()