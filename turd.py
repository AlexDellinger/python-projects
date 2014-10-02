'''
var counter;

penWidth(1);
for (counter = 1; counter <= 2000; counter++) {
  penColour(colour_random());
  moveForward(counter);
  turnRight(91);
}
'''
from turtle import Turtle
turd = Turtle()
turd.pensize(7)
turd.pencolor('brown')
while True:
    turd.forward(100)
    turd.right(2500)
    turd.forward(100)
    turd.right(90) 
    turd.forward(13)
    turd.right(350)
    turd.forward(100)
    turd.right(770)
    turd.forward(165)
    turd.right(770)
    turd.forward(100)
