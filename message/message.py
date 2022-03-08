from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL import glBegin
import sys

xPlane = 0.0
yPlane = 0.0
scale = 1.0

def keyPressed(*args):
    global xPlane
    global yPlane
    if args[0] == b"a":
        xPlane -= 2
    elif args[0] == b"d":
        xPlane += 2
    elif args[0] == b"w":
        yPlane += 2
    elif args[0] == b"s":
        yPlane -= 2
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

def draw():
    global xPlane
    global yPlane
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)

    glViewport(0, 0, 250, 250)
    glLoadIdentity()
    glPushMatrix()
    glColor3f(1, 0, 0)  # Draw     RED
    glScale(scale, scale, scale)
    glRotate(xPlane, 0, 1, 0)
    glRotate(yPlane, 1, 0, 0)
    glutWireCube(1.0)
    glPopMatrix()

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(250, 250)
    glutCreateWindow(b"Multi viewport sample ")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutKeyboardFunc(keyPressed)
    glutMouseWheelFunc(MouseWheel)
    glutMainLoop()


main()