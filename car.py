from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def init():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)

x = 1
angle = 0

def torus(a,b,c):
    glColor(0,1,1)
    glLoadIdentity()
    glTranslate(a,b,c)
    glRotate(angle,0,0,1)
    glutWireTorus(0.125,0.5,12,8)

def drawCar():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global angle
    glMatrixMode(GL_MODELVIEW)

    #ROAD
    glLoadIdentity()
    glColor3f(.1, .1, .1)
    glTranslate(0, -1.8, -1)
    glScale(90, .2, 10)
    glutSolidCube(1)
    #center line
    glLoadIdentity()
    glColor3f(.8, .8, .8)
    glTranslate(0, -1.8, -1)
    glScale(90, .5, 2)
    glutSolidCube(1)

    #low part
    glLoadIdentity()
    glColor(1,0,0)
    glScale(1,0.25,0.5)
    glTranslate(x,0,0)
    glutSolidCube(5)
    #high part
    glLoadIdentity()
    glColor(0,0,1)
    glTranslate(x,0.25*5,0)
    glScale(0.6,0.2,0.5)
    glutSolidCube(5)

    torus(x+1.5,-.3,1.5)
    torus(x-1.5,-.3,1.5)
    torus(x-1.5,-.3,-1.5)
    torus(x+1.5,-.3,-1.5)

    #light
    glColor(0,1,0)
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2.2,-.3,.5)
    glScale(.25,1,1)
    glutSolidSphere(.3,20,20)

    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2.2,-.3,-.9)
    glScale(.25,1,1)
    glutSolidSphere(.3,20,20)


    x += 0.01
    angle -= 0.1

    glFlush()

###########################
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Chair")
glutDisplayFunc(drawCar)
glutIdleFunc(drawCar)
init()
glutMainLoop()




