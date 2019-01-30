# Lab No. 3
# CTEC 121
# Colin Young

import graphics

def snowman():
    # create the graphics window
    win = graphics.GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3
    circle1 = graphics.Circle(graphics.Point(150,250),60)
    circle1.move(0,100)
    circle2 = circle1.clone()
    circle2.move(0,120)
    circle3 = circle1.clone()
    circle3.move(0,240) 
    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)




    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2
    eye1 = graphics.Circle(graphics.Point(10,20),10)
    eye1.setFill('black')
    eye1.move(110,300)
    eye1.draw(win)
    eye2 = eye1.clone()
    eye2.move(60,0)
    eye2.setFill('black')
    eye2.draw(win)



    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose

    nose = graphics.Polygon(graphics.Point(-10,0),graphics.Point(0,30),graphics.Point(10,0))
    nose.draw(win)
    nose.setFill('orange')
    nose.move(150,335)


    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat
    hat = graphics.Rectangle(graphics.Point(40,0),graphics.Point(0,60))
    hat.draw(win)
    hat.setFill('black')
    hat.move(130,230)



    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline
    brim = graphics.Rectangle(graphics.Point(160,0),graphics.Point(0,20))
    brim.draw(win)
    brim.setFill('black')
    brim.move(70,280)





    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()