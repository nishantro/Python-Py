from turtle import *

speed(0)
delay(0)
pensize(5)
#tracer(100,0)
pencolor(1, 0, 0)

width = window_width()
height = window_height()

def clearscrn():
    clear()
    penup()
    drawsqr(-width/2,"red")
    drawsqr(-width/2+50,"blue")
    drawsqr(-width/2+50*2,"green")
    drawsqr(-width/2+50*3,"orange")
    drawsqr(-width/2 + 50*4, "purple")
    pencolor("red")
    fillcolor("white")
    

def drawsqr(x,colorr):
    penup()
    pencolor(colorr)
    fillcolor(colorr)
    pensize(1)
    goto(x,height/2)
    pendown()
    begin_fill()
    for i in range (0,4):
        forward(50)
        right(90)
    end_fill()
    penup()
    goto(0,0)
    pendown()
    pensize(5)

clearscrn()

def screenevent(x, y):
        if (y > height/2 - 50 and y < height/2):
            if (x > -width/2 and x < -width/2+50):
                pencolor("red")
            elif (x > -width/2 + 50 and x < -width/2 + 50*2):
                pencolor("blue")
            elif (x > -width/2 +50*2 and x < -width/2 + 50*3):
                pencolor("green")
            elif (x > -width/2 +50*3 and x < -width/2 + 50*4):
                pencolor("orange")
            elif (x > -width/2 +50*4 and x < -width/2 +50*5):
                pencolor("purple")
        else:
            goto(x,y)
        
def widthLOW():
    pensize(5)

def widthHI():
    pensize(10)

listen()

onkey(widthLOW, "[")
onkey(widthHI, "]")
onkey(clearscrn, "c")

#mouse input
onscreenclick(screenevent)


done()
