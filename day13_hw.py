# 공튀기기 코드, 어떠한 이유에서인지 모르겠지만. 공이 튀기다가 사각형 밖으로 나가버리고 그게 반복됩니다..

import turtle as t
t.shape("circle")
t.speed(10)
for x in range(4):
    t.fd(500)
    t.left(90)       #길이가 500인 정사각형
import math
import random
a=random.randint(1,500)  #원의 초기의 랜덤한 위치,각도를 설정하기 위해 randint를 이용
b=random.randint(1,500) 
c=random.randint(0,360)
t.up()
t.goto(a,b)
t.down()
t.setheading(c)
c=t.heading()
k=t.towards(500,500)
d=t.towards(500,0)
h=t.towards(0,500)
j=t.towards(0,0)

deg=math.radians
def rigup():                #c가 0도에서 k사이일때
    t.fd((500-a)/abs(math.cos(deg(c))))
    t.left(abs(180-2*c))

def rigdown():                #c가 d도에서 360사이일때
    t.fd((500-a)/abs(math.cos(deg(c))))
    t.right(abs(2*c-540))

def uppright():                #c가 k와 90도 사이일때
    t.fd((500-b)/abs(math.sin(deg(c))))
    t.left(abs(360-2*c))

def uppleft():                        #c가 90도와 h각 사이일때
    t.fd((500-b)/abs(math.sin(deg(c))))
    t.left(abs(360-2*c))

def leffup():                           #h각과 180도 사이일때
    t.fd(a/abs(math.cos(deg(180-c))))
    t.right(abs(2*c-180))

def leffdown():                      #180도와 j도 사이일때
    t.fd(a/abs(math.cos(deg(180-c))))
    t.left(abs(540-2*c))

def downnleft():               #j와 270도 사이
    t.fd(b/abs(math.cos(deg(270-c))))
    t.right(abs(2*c-360))

def downnright():               #270와 d도 사이
    t.fd(b/abs(math.cos(deg(c-270))))
    t.left(abs(720-2*c))

for x in range(100):
    if c>=0 and c<=k:
        rigup()
    if c>k and c<=90:
        uppright()
    if c>90 and c<=h:
        uppleft()
    if c>h and c<=180:
        leffup()
    if c>180 and c<=j:
        leffdown()
    if c>j and c<=270:
        downnleft()
    if c>270 and c<=d:
        downnright()
    if c>d and c<=360:
        rigdown()
    a=t.xcor()
    b=t.ycor()
    c=t.heading()
