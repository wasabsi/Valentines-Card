# Name: Sabrina Warner
# valentineGreeting.py
#
#Problem: Create a valentines day card with a heart and a shooting arrow

#Certification of Authenticity:
#   I certify that this lab is entirely my own work.

from graphics import *
from time import sleep

def valentineGreeting():

    #window
    width = 400
    height = 700
    win = GraphWin("ValentineGreeting", width, height)
    win.setBackground("pink")
    
    #Valentines day text
    text = Text(Point(200, 100), "happy valentine's \n ya filthy animal")
    text.setSize(30)
    text.setTextColor("yellow")
    text.setStyle("bold")
    text.draw(win)

    
    #grass
    grass = Rectangle (Point(200,700), Point(400, 700))
    grass.setFill("#556B2F")
    grass.setOutline("#556B2F")
    grass.draw(win)
    
    #stem
    stem = Rectangle(Point(198,240),Point(202,620))
    stem.setFill("#556B2F")
    stem.setOutline("#556B2F")
    stem.draw(win)
    #triangle of the heart
    heart1 = Polygon(Point(160,400),Point(240,400),Point(200,450))
    heart1.setFill("#6B8E23")
    heart1.setOutline("#6B8E23")
    heart1.draw(win)
    #circle of the heart (left)
    heart2 = Circle(Point(180,394), 20)
    heart2.setFill("#6B8E23")
    heart2.setOutline("#6B8E23")
    heart2.draw(win)
    #circle of the heart (right)
    heart3 = Circle(Point(220,394), 20)
    heart3.setFill("#6B8E23")
    heart3.setOutline("#6B8E23")
    heart3.draw(win)
    #circle for the flower
    flower1 = Circle(Point(width/2, 202), 50)
    flower1.setFill("red")
    flower1.setOutline("red")
    flower1.draw(win)
    #rectangle for the flower
    flower2 = Rectangle(Point(150,150), Point( 250,200))
    flower2.setFill("red")
    flower2.setOutline("red")
    flower2.draw(win)
    
    #first 3 points for the big triangle on arrow
    p1 = Point(0, 410)
    p2 = Point(-25, 425)
    p3 = Point(-25, 395)
    
    #points for second triangle
    p4 = Point(-75, 410)
    p4.draw(win)
    p5 = Point(-80, 405)
    p5.draw(win)
    p6 = Point(-80, 415)
    p6.draw(win)
    p7 = Point(-3, 410)
    
    #stem of the arrow
    line = Line(p7, p4)
    line.setWidth(5)
    line.setFill('yellow')
    line.setOutline('yellow')
    line.draw(win)

    # arrowhead
    tria = Polygon(p1, p2, p3)
    tria.setFill('yellow')
    tria.setOutline('yellow')
    tria.draw(win)
    
    #causes all the pieces to travel the screen
    for i in range (170): 
        tria.move(1,0)
        line.move(1,0)
        sleep(.005)

    #closing 
    text = Text(Point(200, 650), "Click Anywhere To Close")
    text.setSize(15)
    text.draw(win)

    win.getMouse()
    win.close()
    


valentineGreeting()
 
    
    
