import turtle
b=turtle.Screen()
c=turtle.Turtle()
#help (turtle.shape)
c.shape('arrow')
# c.shape('circle')
# c.shape('triangle')
# c.shape('classic')
# c.shape('arrow')
# c.shape('square')
#colour and the place
c.color('green','yellow')
# c.forward(100)
# c.backward(200)
b.bgcolor('black')
b.title('arrow')
b.screensize(400,400)
c.pensize(4)
# c.forward(100)
#Drawing square using forward and right
# c.speed(3)
# c.right(90)
# c.forward(100)
# c.speed(1)
#
# c.right(90)
# c.forward(100)
# c.speed(7)
# c.right(90)
# c.forward(100)

#to hide the line that is drawn
# c.clear()
#To hide turtle
# c.ht()
#To fill colour in the shape
# c.begin_fill()
# c.fillcolor('black')
#Drwaing square using for loop
# for i in range (4):
#     c.forward(100)
#     c.right(90)
#     c.ht()
# c.end_fill()
#
# #Drawing pentagon
# for i in range(5):
#     c.forward(100)
#     c.right(72)
#
# #Drawing Hexagon
# for i in range(6):
#     c.forward(100)
#     c.right(60)
#
# for i in range (7):
#     c.forward(100)
#     c.right(51.42)
#
# for i in range(9):
#     c.forward(100)
#     c.right(45)
#
# for i in range(10):
#     c.forward(100)
#     c.right(36)

# c.dot(100)
# c.ht()
#To change the position of the shapes
#Home work
# c.begin_fill()
# c.fillcolor('black')
# c.up()
# c.goto(0,0)
# c.down()
# c.circle(50)
# c.end_fill()
#
# c.begin_fill()
# c.fillcolor('black')
# c.up()
# c.goto(200,-200)
# c.down()
# c.circle(50)
# c.end_fill()
#
# c.begin_fill()
# c.fillcolor('black')
# c.up()
# c.goto(200,150)
# c.down()
# c.circle(50)
# c.end_fill()
#
# c.begin_fill()
# c.fillcolor('black')
# c.up()
# c.goto(-200,150)
# c.down()
# c.circle(50)
# c.end_fill()
#
# c.begin_fill()
# c.fillcolor('black')
# c.up()
# c.goto(-200,-200)
# c.down()
# c.circle(50)
# c.ht()
# c.end_fill()
#To make plus sign
#Set direction at 0
# #angle usinng seth
# c.seth(0)
# #motion
# c.forward(80)
# c.write('East')
# c.home()
#
# c.setheading(90)
# c.forward(80)
# c.write('North')
# c.home()
#
# c.seth(180)
# c.forward(80)
# c.write('west')
# c.home()
#
# c.seth(270)
# c.forward(80)
# c.write('south')
# c.home()

# b.bgcolor('black')
# c.pensize(2)
# c.speed(0)
#
# while (True):
#     for i in range(6):
#         for colors in ['red','blue','magenta','green','yellow','white']:
#             c.color(colors)
#             c.circle(100)
#             c.left(10)
#     break
# c.ht()
# turtle.done()



#HOME WORK
#Draw Star
#Draw circle in five different stop with different fill colour ()
c.left(65)
c.forward(150)
c.right(125)
c.forward(150)
c.right(150)
c.forward(170)
c.right(150)
c.forward(150)
c.right(147)
c.forward(167)
c.ht()

for i in range(8):
    c.forward(200)
    c.right(144)



turtle.mainloop()