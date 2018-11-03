from graphics import GraphWin, Point, Rectangle, Polygon, Text


def main():


	win=GraphWin("Five-Click House", 500, 400) 
	win.setCoords(0.0,0.0,15.0,15.0)

	message=Text(Point(7.5,1), "Choose 5 points that draw a house and a door.") 

	message.draw(win)


	p1=win.getMouse()  #choose the five points wisely for building the house
	p1.draw(win)
	p2=win.getMouse()
	p2.draw(win)
	p3=win.getMouse()
	p4=win.getMouse()
	p5=win.getMouse()

	x1=p1.getX()        # get the corresponding values for x and y 
	y1=p1.getY()
	x2=p2.getX()
	y2=p2.getY()
	x3=p3.getX()
	y3=p3.getY()
	x4=p4.getX()
	y4=p4.getY()

	last_leg_triangle=Point(x1, y2)


	Rectangle1= Rectangle(p1, p2)     #build the rectangle; the home
	Rectangle1.draw(win)			  #draw the building 

	p_rect1 = Point((x3-(((x2-x1)/5)/2)), y3)   
	p_rect2= Point(x3+(((x2-x1)/5)/2), y1)

	p_square = Point(x4 + (((x2-x1)/5)*(3/4)), y4 +(((x2-x1)/5)*(3/4)))
	p_square_2 = Point(x4 - (((x2-x1)/5)*(3/4)), y4 - (((x2-x1)/5)*(3/4)))

	Rect=Rectangle(p_rect1,p_rect2)
	Rect.draw(win)

	Rect4=Rectangle(p_square, p_square_2)
	Rect4.draw(win)

	Triangle=Polygon(p5,p2,last_leg_triangle)
	Triangle.draw(win)


	win.getMouse()
	
main()

