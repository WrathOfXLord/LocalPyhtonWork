from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL import glBegin
import sys

xPlaneR = 0.0   #bu dört değişken wasd tuşlarıyla küpü hareket ettirmek için
yPlaneR = 0.0
xPlaneT = 0.0
yPlaneT = 0.0
scale = 1.0     #mouse tekerleği ile ölçeklendirmek için
rotateX = 0.0   #çaydanlığı döndürmek için

def rotateDisplay(x, y):    #çaydanlık döndürme fonksiyonu
    global rotateX
    rotateX += 1
    glutPostRedisplay

def keyPressed(*args):
    global xPlaneR
    global yPlaneR
    global xPlaneT
    global yPlaneT
    if args[0] == b"a" or args[0] == b"A":
        xPlaneR -= 2
        xPlaneT -= 0.01
    elif args[0] == b"d" or args[0] == b"D":
        xPlaneR += 2
        xPlaneT += 0.01
    elif args[0] == b"w" or args[0] == b"W":
        yPlaneR += 2
        yPlaneT += 0.01
    elif args[0] == b"s" or args[0] == b"S":
        yPlaneR -= 2
        yPlaneT -= 0.01
    else:
        pass
    glutPostRedisplay()

def MouseWheel(*args):
    global scale
    print(args)
    if args[1]==-1:
        scale -= 0.05
    elif args[1]==1:
        scale += 0.05
    else:
        pass
    glutPostRedisplay()

def Mouse(*args):
    if args[1] == GLUT_:
        glutMotionFunc(rotateDisplay)
    else:
        pass
    glutPostRedisplay()

def draw():
    global xPlaneR
    global yPlaneR
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)

    glViewport(0, 0, 500, 500)
    glLoadIdentity()
    glPushMatrix()
    glColor3f(0.8, 0, 0.3)  # crimson red
    glScale(scale, scale, scale)    #ölçeklendirme
    glTranslatef(xPlaneT, 0, 0)     #öteleme
    glTranslatef(0, yPlaneT, 0)
    glRotate(xPlaneR, 0, 1, 0)      #öteleme ve dönme için
    glRotate(yPlaneR, 1, 0, 0)
    glutWireCube(1.0)               #3d hareketleri görüntülemek için tel küp
    glPopMatrix()

    glViewport(500, 0, 500, 500)
    glLoadIdentity()
    glPushMatrix()
    glColor3f(0, 0.3, 0.45)  # dark blue
    glRotate(rotateX, 0, 0, 1) #çaydanlık
    glutSolidTeapot(0.3)
    glPopMatrix()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 500)
    glutInitWindowPosition(250, 250)
    glutCreateWindow(b"Rotating Objects")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutKeyboardFunc(keyPressed)
    glutMouseWheelFunc(MouseWheel)
    glutMouseFunc(Mouse)
    glutMainLoop()


main()


#testing comment