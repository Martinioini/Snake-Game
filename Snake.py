from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:    
    
    def __init__(self):

        self.startingPositions = [(0, 0), (-20, 0), (-40, 0)]
        self.tiles = []

        for pos in self.startingPositions:
            self.addSegment(pos)
        
        self.head = self.tiles[0]

    def reset(self):
        
        for seg in self.tiles:
            seg.goto(1000, 1000)
            
        self.tiles.clear()
        for pos in self.startingPositions:
            self.addSegment(pos)

        self.head = self.tiles[0]
        

    def addSegment(self, position):
        
        newTile = Turtle()
        newTile.color("white")
        newTile.shape("square")
        newTile.penup()
        newTile.goto(position)
        self.tiles.append(newTile)

    def extend(self):

        self.addSegment(self.tiles[-1].position())


    def up(self):

        if self.tiles[0].heading() != DOWN:
            
            self.tiles[0].setheading(UP)

    def down(self):
        
        if self.tiles[0].heading() != UP:
            
            self.tiles[0].setheading(DOWN)

    def right(self):

        if self.tiles[0].heading() != LEFT:
            
            self.tiles[0].setheading(RIGHT)

    def left(self):

        if self.tiles[0].heading() != RIGHT:

            self.tiles[0].setheading(LEFT)

    def move(self):

        for segNum in range(len(self.tiles) - 1, 0, -1):
            newX = self.tiles[segNum - 1].xcor()
            newY = self.tiles[segNum - 1].ycor()
            self.tiles[segNum].goto(newX, newY)

        self.tiles[0].forward(MOVE_DISTANCE)