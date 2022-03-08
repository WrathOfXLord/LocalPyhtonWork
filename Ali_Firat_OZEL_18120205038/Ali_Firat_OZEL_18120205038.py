from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import sys

Elbow = 0.0     #kol dış öteleme
ElbowR = 0.0    #kol dış dönme
Arm = 0.0       #kol iç öteleme
ArmR = 0.0      #kol iç dönme

def vucut():
    glColor4f(0, 0.5, 0.9, 1)
    glBegin(GL_QUADS)   ##kafa
    glVertex2f(175, 350)    #sol alt
    glVertex2f(325, 350)    #sağ alt
    glVertex2f(325, 450)    #sağ üst
    glVertex2f(175, 450)    #sol üst
    glEnd()

    glBegin(GL_QUADS)   ##boyun
    glVertex2f(230, 300)
    glVertex2f(270, 300)
    glVertex2f(270, 350)
    glVertex2f(230, 350)
    glEnd()

    glBegin(GL_QUADS)   ##gövde
    glVertex2f(150, 50)
    glVertex2f(350, 50)
    glVertex2f(350, 300)
    glVertex2f(150, 300)
    glEnd()

def dirsek():
    
    posx1, posy1 = 110, 280
    sides = 180
    radius = 20
    glBegin(GL_POLYGON)
    for i in range(360):
        cosine= radius * cos(i*pi/sides) + posx1
        sine  = radius * sin(i*pi/sides) + posy1
        glVertex2f(cosine,sine)
    glEnd()

    posx2, posy2 = 390, 280
    sides = 180
    radius = 20
    glBegin(GL_POLYGON)
    for i in range(360):
        cosine = radius * cos(i*pi/sides) + posx2
        sine  = radius * sin(i*pi/sides) + posy2
        glVertex2f(cosine,sine)
    glEnd()

def dirsek2():
    
    posx1, posy1 = 110, 280
    sides = 32
    radius = 20
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine= radius * cos(i*2*pi/sides) + posx1
        sine  = radius * sin(i*2*pi/sides) + posy1
        glVertex2f(cosine,sine)
    glEnd()

    posx2, posy2 = 390, 280
    sides = 32
    radius = 20
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine= radius * cos(i*2*pi/sides) + posx2
        sine  = radius * sin(i*2*pi/sides) + posy2
        glVertex2f(cosine,sine)
    glEnd()



def kol_sabit():
    glBegin(GL_QUADS)   ##sol kol iç
    glVertex2f(120, 270)
    glVertex2f(160, 270)
    glVertex2f(160, 290)
    glVertex2f(120, 290)
    glEnd()

    glBegin(GL_QUADS)   ##sol kol dış
    glVertex2f(60, 270)
    glVertex2f(100, 270)
    glVertex2f(100, 290)
    glVertex2f(60, 290)
    glEnd()

    glBegin(GL_QUADS)   ##sağ kol iç
    glVertex2f(340, 270)
    glVertex2f(380, 270)
    glVertex2f(380, 290)
    glVertex2f(340, 290)
    glEnd()

    glBegin(GL_QUADS)   ##sağ kol dış
    glVertex2f(400, 270)
    glVertex2f(440, 270)
    glVertex2f(440, 290)
    glVertex2f(400, 290)
    glEnd()
    dirsek()

def kol_hareketli():
    glPushMatrix()
    glTranslatef(Arm-1, Arm, 0)
    glRotate(-ArmR, 0, 0, 1)
    glBegin(GL_QUADS)   ##sol kol iç
    glVertex2f(120, 270)
    glVertex2f(160, 270)
    glVertex2f(160, 290)
    glVertex2f(120, 290)
    glEnd()


    glPushMatrix()

    glTranslatef(-Elbow, Elbow, 0)
    glRotate(-ElbowR, 0, 0, 1)

    # glColor3f (1, 0.75, 0)
    # glutSolidSphere(1.0, 20, 16)

    glBegin(GL_QUADS)   ##sol kol dış
    glVertex2f(60, 270)
    glVertex2f(100, 270)
    glVertex2f(100, 290)
    glVertex2f(60, 290)
    glEnd()

    glPopMatrix()
    glPopMatrix()

    glPushMatrix()

    glTranslatef(-Arm+1, -Arm, 0)
    glRotate(ArmR, 0, 0, 1)
    glBegin(GL_QUADS)   ##sağ kol iç
    glVertex2f(340, 270)
    glVertex2f(380, 270)
    glVertex2f(380, 290)
    glVertex2f(340, 290)
    glEnd()

    #glTranslatef(-1, 0, 0)
    #glutSolidSphere(2, 100, 100)
    
    glPushMatrix()

    glTranslatef(Elbow, -Elbow, 0)
    glRotate(ElbowR, 0, 0, 1)
    glBegin(GL_QUADS)   ##sağ kol dış
    glVertex2f(400, 270)
    glVertex2f(440, 270)
    glVertex2f(440, 290)
    glVertex2f(400, 290)
    glEnd()

    glPopMatrix()
    glPopMatrix()

    dirsek2()


def robot():
    vucut()
    kol_sabit()
    
    glViewport(500, 0, 500, 500)
    glLoadIdentity()
    glFlush()
    
    ## ikinci görüntü

    vucut()
    kol_hareketli()



def keyPressed(*args):
    global Elbow
    global ElbowR
    global Arm
    global ArmR

    if args[0] == b"w" or args[0] == b"W":
        Elbow += 5
        ElbowR += 1
        Arm += 2.5
        ArmR += 0.5
        
    elif args[0] == b"s" or args[0] == b"S":
        Elbow -= 5
        ElbowR -= 1
        Arm -= 2.5
        ArmR -= 0.5

    else:
        pass
    glutPostRedisplay()

def draw():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(50.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    robot()
    glutSwapBuffers()

def resize_shape(Width, Height):
    if Height == 0:  # 0'a bölümü engellemek için
        Height = 1

    glViewport(0, 0, Width, Height)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70.0, Width/Height, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(1000, 500)
    glutInitWindowPosition(250, 250)
    glutCreateWindow(b"Robot")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutKeyboardFunc(keyPressed)
    glutReshapeFunc(resize_shape)
    glutMainLoop()


main()