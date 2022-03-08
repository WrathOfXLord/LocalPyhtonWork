from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

shape_vertices = []


def readObj():
    my_file = open("angelDrop_fixed.txt", "r")
    lines = my_file.readlines()
    for l in lines:
        splitted_l = l.split(" ")
        if splitted_l[0] == 'v':
            shape_vertices.append([float(splitted_l[1]), float(splitted_l[2]), float(splitted_l[3])])

    print("All vertices are read from file")


weight = 500
height = 500
rangle = 1
readObj()


def draw():
    global shape_vertices, rangle
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0, 0, 500, 500)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)

    glTranslatef(0, -0.3, 0)
    glScale(0.5, 0.5, 0.5)
    glRotatef(rangle, 0, 1, 0)
    glColor3f(0.5, 1, 0.5)  # Draw     BLUE

    glBegin(GL_POINTS)
    for i in shape_vertices:
        glVertex3f(i[0], i[1], i[2])
    glEnd()

    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(weight, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Obj File Sample")
    glutIdleFunc(draw)
    glutDisplayFunc(draw)
    glutMainLoop()
main()
