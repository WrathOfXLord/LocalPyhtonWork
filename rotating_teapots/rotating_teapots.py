'''
Bu örnekte ekrana iki çaydanlık çizdirilmektedir.
İlk çaydanlık kendi etrafında dönerken, ikinci çaydanlık sabit bir şekilde durmaktadır.
Tek bir vieport çizim ekranında nesneleri birbirnden bağımsız hareket ettirebilmek için
glPushMatrix() ve glPopMatrix fonksiyonlarının işlevi ele alınmıştır.

'''

from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

rangle = 0.0  # Rotation angle

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)


def drawAxis():
    '''
    Bu fonksiyon x ve y eksenlerini nokta şeklinde çizdiriyor.
    '''
    glColor3f(0, 1, 1)
    for i in range(-5, 5):
        glBegin(GL_POINTS)
        glVertex2f(i, 0)
        glVertex2f(0, i)
        glEnd()


# The main drawing function.
def DrawGLScene():
    global rangle
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    drawAxis()

    # Merkezdeki birinci çaydanlık örneği
     #glPushMatrix pushes the current matrix stack down by one, duplicating the current matrix.
    # That is, after a glPushMatrix call, the matrix on top of the stack is identical to the one below it.
    #glPushMatrix()
    glRotatef(rangle, 0, 1, 0) # Çaydanlık y eksenine göre dönderiliyor.
    glutSolidSphere(1, 50, 50)
    #glPopMatrix()

    #glPopMatrix pops the current matrix stack,
    # replacing the current matrix with the one below it on the stack.

    #İkinci çaydanlığı birinci çaydanlığın x eksenine göre 3 birim kaydırdık.
    #glPushMatrix()
    glTranslatef(3.0,0.0,0.0)
    glRotatef(rangle,0,1,0)
    glColor(1, 0, 0)
    glutSolidSphere(0.5, 50, 50)
    #glPopMatrix()

    glutSwapBuffers()


# The function called whenever a key is pressed.
# Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
    global rangle
    if args[0] == b"r" :
        print("rotate")
        rangle += 5

    if args[0] == b"p":
        print("rotate red")
        rangle += 5
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Rotate teapots")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL()
    glutMainLoop()


main()
