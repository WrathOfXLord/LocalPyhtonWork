import PIL as pillow
from PIL import Image
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
################### OBJ dosyası değişkenleri
vertexCoords = [] # v değerleri
textCoords = []   # vt değerleri
normCoords = []   # vn değerleri
###################
vertexIndex = []  # v dizi indeksi
textIndex = []    # vt dizi indeksi
normIndex = []    # vn dizi indeksi
################### Mouse değişkenleri
oldX = 0          # eski mouse işaretçi pozisyonları
oldY = 0          #
dx = 0            # işaretçi yer değişimi
dy = 0            #
scale = 0.15      # büyütüp küçültme
################### MTL (materyal dosyası değişkenleri)
alpha = 0.0       # texture alpha, mtl dosyası
ns = 0.0          # texture exponent
ni = 0.0          # texture yoğunluk
dif = []          # texture diffuse 
amb = []          # texture ambient
spec = []         # texture specular
illum = 0         # texture illumination
###################
###################
mtlFile = []      # materyal dosyası adı
###################
width = 500       #
height = 500      #
###################
texture = [0 for x in range(3)] #texture id dizini


def init():

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glEnable(GL_DEPTH_TEST)
    

def lighting():
    glMaterialfv(GL_FRONT, GL_AMBIENT, amb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, dif)
    glMaterialfv(GL_FRONT, GL_SPECULAR, spec)
    

def texturing(file):
    
    im = Image.open(file)
    xSize = im.size[0]
    ySize = im.size[1]
    rawReference = im.tobytes("raw", "RGB")
    id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, id)  # bind Texture, 2d texture (x and y size)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, xSize, ySize, 0, GL_RGB, GL_UNSIGNED_BYTE, rawReference)
    glEnable(GL_TEXTURE_2D)

    return id


def readObj(file):
    global vertexCoords, textCoords, normCoords
    objFileLoader = open(file)
    lines = objFileLoader.readlines()
    for l in lines:
        splitSpaceObj = l.split(" ")
        
        if splitSpaceObj[0] == 'v':
            v = list(map(float, splitSpaceObj[1:4]))
            vertexCoords.append(v)

        elif splitSpaceObj[0] == 'vt':
            v = list(map(float, splitSpaceObj[1:3]))
            textCoords.append(v) 
        
        elif splitSpaceObj[0] == 'vn':
            v = list(map(float, splitSpaceObj[1:4]))
            normCoords.append(v)

        elif splitSpaceObj[0] == 'f':
            global vertexIndex, textIndex, normIndex
            faceVertex = []
            texcoords = []
            norms = []
            for v in splitSpaceObj[1:]:
                w = v.split('/')
                faceVertex.append(int(w[0]) - 1)

                if len(w) >= 2 and len(w[1]) > 0:
                    texcoords.append(int(w[1]) - 1)
                else:
                    texcoords.append(0)

                if len(w) >= 3 and len(w[2]) > 0:
                    norms.append(int(w[2]) - 1)
                else:
                    norms.append(0)

            vertexIndex.append(faceVertex)
            textIndex.append(texcoords)
            normIndex.append(norms)

        elif splitSpaceObj[0] == 'mtllib':
            global mtlFile
            mtlFile = splitSpaceObj[1]
            mtlFile = mtlFile.rstrip("\n")
        
        elif splitSpaceObj[0] == 'usemtl':
            global alpha, ns, ni, amb, dif, spec, illum
            mtlFileLoader = open(mtlFile, "r")
            rows = mtlFileLoader.readlines()
            
            for l in rows:
                splitSpaceMtl = l.split(" ")
                if splitSpaceMtl[0] == 'd':
                    alpha = 1 - float(splitSpaceMtl[1])

                elif splitSpaceMtl[0] == 'Ns':
                    ns = float(splitSpaceMtl[1])

                elif splitSpaceMtl[0] == 'Ni':
                    ni = float(splitSpaceMtl[1])

                elif splitSpaceMtl[0] == 'Ka':
                    amb = list(map(float, splitSpaceMtl[1:4]))
                    
                elif splitSpaceMtl[0] == 'Kd':
                    dif = list(map(float, splitSpaceMtl[1:4]))

                elif splitSpaceMtl[0] == 'Ks':
                    spec = list(map(float, splitSpaceMtl[1:4]))
                    
                elif splitSpaceMtl[0] == 'illum':
                    illum = int(splitSpaceMtl[1])
                
                # elif splitSpaceMtl[0] == '':
                #     texture = int()

    # print(normCoords[normIndex[0][0]])    #hata ayıklama
    # print(vertexCoords)  #hata ayıklama
    # print("")  #hata ayıklama
    # print(vertexIndex)  #hata ayıklama
    # print("")  #hata ayıklama
    # print(len(vertexIndex))  #hata ayıklama
    print("Loading Object File is done")   
    print("Mtl and Obj values are read from files")

def mouseMotion(x, y):
    global oldX, oldY, dx, dy   
    speed = 1.2   
    dx += (x - oldX) * speed
    dy += (y - oldY) * speed
    oldX = x
    oldY = y
    glutPostRedisplay()

def mouse(button, state, x, y):
    global oldX, oldY
    # print("oldX is " + str(oldX)) #hata ayıklama
    # print("oldY is " + str(oldY)) #hata ayıklama
    oldX = x
    oldY = y
    glutMotionFunc(mouseMotion)

    # print("newX is " + str(args[2]))  #hata ayıklama
    # print("newY is " + str(args[3]))  #hata ayıklama
    # print("dx is " + str(dx))  #hata ayıklama
    # print("dy is " + str(dy))  #hata ayıklama

def MouseWheel(*args):
    global scale
    if scale < 0.015:
        scale = 0.015
    if scale > 0.170:
        scale = 0.165

    if args[1] == 1:
        scale += 0.005

    elif args[1] == -1:
        scale -= 0.005
    # print(scale)  #hata ayıklama
    glutPostRedisplay()

def ground():
    global dy
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture[1])
    if dy < 1:
        dy = 1
    if dy > 135:
        dy = 135
    glRotatef(dy, 1, 0, 0)
    glRotatef(dx, 0, 1, 0)
    glScalef(scale, 0.0, scale)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-2000.0, 0.0, -2000.0)
    glTexCoord2f(0, 1)
    glVertex3f(-2000.0, 0.0, 2000.0)
    glTexCoord2f(1, 1)
    glVertex3f(2000.0, 0.0, 2000.0)
    glTexCoord2f(1, 0)
    glVertex3f(2000.0, 0.0, -2000.0)
    glEnd()
    glPopMatrix()

def background():
    global dy
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture[2])
    if dy < 2:
        dy = 1
    glRotatef(dy, 1, 0, 0)
    glRotatef(180, 0, 0, 1)
    glTranslatef(0, -9, -14)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-15, 0.0, 0.0)
    glTexCoord2f(0, 1)
    glVertex3f(-15.0, 15.0, 0.0)
    glTexCoord2f(1, 1)
    glVertex3f(15.0, 15.0, 0.0)
    glTexCoord2f(1, 0)
    glVertex3f(15.0, 0.0, 0.0)
    glEnd()
    glPopMatrix()

def mainObject():
    global vertexCoords, textCoords, normCoords
    global vertexIndex, textIndex, normIndex
    global dy
    if dy < 2:
        dy = 1
    glPushMatrix()
    glRotatef(dy, 1, 0, 0)
    glRotatef(dx, 0, 1, 0)
    glScalef(scale, scale, scale)
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_TRIANGLES)
    for i in range(len(vertexIndex)):
        for j in range(len(vertexIndex[i])):
            # print("index : " + str(i) + " " + str(j))  #hata ayıklama
            # print("vertexIndex at : " + str(vertexCoords[vertexIndex[i][j]]))  #hata ayıklama
            # print("normIndex at : " + str(normCoords[normIndex[i][j]]))  #hata ayıklama
            glTexCoord2fv(textCoords[textIndex[i][j]])
            glNormal3fv(normCoords[normIndex[i][j]])
            glVertex3fv(vertexCoords[vertexIndex[i][j]])

    glEnd()
    glPopMatrix()

def draw():    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.18, 0.32, 0.6, 1.0)   
    glMatrixMode(GL_PROJECTION)
    lighting()
    gluPerspective(40.0, 5.0 / 3.0, 1, 20)
    background()
    gluLookAt(0, 1, 5, 0, 1, -5, 0.0, 1.0, 0.0)
    ground()
    mainObject()
    glLoadIdentity()
    glutSwapBuffers()

def main():
    readObj("fox.obj")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Fox with 3D Obj Model")
    init()
    texture[0] = texturing("fur.bmp")
    texture[1] = texturing("terrain.bmp")
    texture[2] = texturing("bg.bmp")
    glutIdleFunc(draw)
    glutDisplayFunc(draw)
    glutMouseFunc(mouse)
    glutMouseWheelFunc(MouseWheel)
    glutMainLoop()

main()

#End of the Code