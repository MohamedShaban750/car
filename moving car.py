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
    gluLookAt(0.1, -35, 0,
              0, 0, 0,
              0, 1, 0)
x = 1
angle = 0
y=0
b=0
mov=0
z=0
t=True




def keyboard(key, xx, yy):
    global mov, t

    if key == b"a":
        mov += 3.5

    if key == b"d":
        mov -= 3.5

def torus(a,b,c):
    glColor(0,1,1)
    glLoadIdentity()
    glTranslate(a,b,c)
    glRotate(angle,0,0,1)
    glutWireTorus(0.125,0.5,12,8)

def centerLine(z):
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(z+b, 0, 0)
    glScale(8, .5, 2)
    glutSolidCube(1)

def drawCar():
    glClear(GL_COLOR_BUFFER_BIT)
    global x, angle, a, b, c, z, y, t

    glMatrixMode(GL_MODELVIEW)

    #ROAD
    glLoadIdentity()
    glColor3f(.1, .1, .1)
    glTranslate(0, 0, 0)
    glScale(90, .2, 15)
    glutSolidCube(1)
    #center line
    centerLine(-10)
    centerLine(0)
    centerLine(10)
    centerLine(20)
    centerLine(30)
    centerLine(40)
    centerLine(50)
    centerLine(60)
    centerLine(70)
    centerLine(80)
    centerLine(90)
    centerLine(100)
    centerLine(110)
    centerLine(120)
    centerLine(130)
    centerLine(140)
    centerLine(150)
    centerLine(160)
    centerLine(170)
    centerLine(180)
    centerLine(190)
    centerLine(200)
    centerLine(210)
    centerLine(220)
    centerLine(230)
    centerLine(240)
    centerLine(250)

    #low part
    glLoadIdentity()
    glColor(1,0,0)
    glTranslate(x,0,0+mov)
    glScale(1,0.2,0.5)
    glutSolidCube(5)
    #high part
    glLoadIdentity()
    glColor(0,0,1)
    glTranslate(x,0,0+mov)
    glScale(0.6,0.2,0.5)
    glutSolidCube(5)

    torus(x+1.5,-.3,1.5+mov)
    torus(x-1.5,-.3,1.5+mov)
    torus(x-1.5,-.3,-1.5+mov)
    torus(x+1.5,-.3,-1.5+mov)

    #light
    glColor(0,1,0)
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2.2,-.3,.5+mov)
    glScale(.25,1,1)
    glutSolidSphere(.3,20,20)

    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2.2,-.3,-.9+mov)
    glScale(.25,1,1)
    glutSolidSphere(.3,20,20)


   # x += 0.01
    angle -= 0.1
    y -=.07
    b -=.015

#Glutkeyboard  Glutkeyboardup





    glFlush()

###########################
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"car")
glutDisplayFunc(drawCar)
glutIdleFunc(drawCar)
glutKeyboardFunc(keyboard)

init()
glutMainLoop()




