from OpenGL.GLUT import *
from OpenGL.GL import *


def draw():
    glColor3d(22, 33, 44)
    glutSolidCube(0.5)
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_RGB)
glutInitWindowSize(250, 250)
glutInitWindowPosition(125, 125)
glutCreateWindow(bytes("Teapot", "ascii"))
glutDisplayFunc(draw)
glutMainLoop()



