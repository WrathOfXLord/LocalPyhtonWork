from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

weight=500
height=500
zoom=1
def test()

def draw():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(0, 0, 1)  # Draw     BLUE
    glScale(zoom,zoom,zoom)
    glutWireTeapot(1)
    glFlush()

def Mouse(button, state, x, y,):
    if(button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and x > 520 and x < 600 and y > 280 and y < 300 ):
        glRotatef(15,1.0,0.0,0.0)
        glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(weight, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D teapot Sample")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMouseFunc(Mouse)
    glutMainLoop()



main()