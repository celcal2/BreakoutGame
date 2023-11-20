from turtle import Turtle, Screen, mainloop, listen, onkeypress, tracer, Vec2D, bgcolor
from random import choice, randint
import time


class Target(Turtle):
    colors = ['green', 'orange', 'yellow', 'pink', 'purple', 'gold', 'gray', 'brown', 'white']

    def __init__(self, x, y):
        super().__init__()
        self.hit_status = False
        self.shapesize(1, 2.5)
        self.color(choice(self.colors))
        self.shape('square')
        self.penup()
        self.goto(x, y)
        self.screen.title("Breakout game by Celina")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1, 5)
        self.color('white')
        self.shape('square')
        self.penup()
        self.goto(0, -200)

    def go_left(self):
        if self.xcor() >= -240:
            self.setx(self.xcor() - 20)

    def go_right(self):
        if self.xcor() <= 240:
            self.setx(self.xcor() + 20)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1)
        self.color('red')
        self.shape('circle')
        self.penup()


class Game():
    tx, ty = -250, 300
    dy = 1
    dx = choice([-.5, .5])
    targets = []

    def __init__(self):
        tracer(0)
        self.pl = Player()
        self.ball = Ball()
        self.screen = Screen()
        for _ in range(5):
            for _ in range(10):
                target = Target(self.tx, self.ty)
                self.targets.append(target)
                self.tx += 55
            self.ty -= 25
            self.tx = -250
        tracer(1)

    def check_border_collision(self):

        if (self.ball.ycor() < -270 or self.ball.ycor() > 270):
            self.screen.clear()
            self.screen.bgcolor('black')
            self.screen.title("Game Over")
            game_over_turtle = Turtle()
            game_over_turtle.hideturtle()
            game_over_turtle.penup()
            game_over_turtle.goto(0, 0)
            game_over_turtle.color('white')
            game_over_turtle.write("Game Over", align="center", font=("Courier", 80, "normal"))
            time.sleep(4)
            exit()

    def update(self):
        self.check_border_collision()
        if self.ball.ycor() < -300:
            exit()
        if self.ball.ycor() > 300:
            self.dy *= -1

        if self.ball.ycor() >= 175:
            for target in self.targets:
                if not target.hit_status:
                    if self.ball.ycor() >= target.ycor() - 25:
                        if self.ball.xcor() >= target.xcor() - 25:
                            if self.ball.xcor() <= target.xcor() + 25:
                                self.dy *= -1
                                target.color('black')
                                target.hit_status = True
                                break

        if self.ball.xcor() <= -270 or self.ball.xcor() >= 260:
            self.dx *= -1
        if self.ball.ycor() <= self.pl.ycor() + 25:
            if self.ball.xcor() >= self.pl.xcor() - 50:
                if self.ball.xcor() <= self.pl.xcor() + 50:
                    self.dy *= -1
        self.ball.setpos(self.ball.xcor() + self.dx * 3, self.ball.ycor() - self.dy * 3)


def enable_keys(pl):
    onkeypress(pl.go_left, "Left")
    onkeypress(pl.go_right, "Right")


def start():
    bgcolor(0, 0, 0)
    game = Game()
    enable_keys(game.pl)
    listen()

    while 1:
        game.update()


if __name__ == '__main__':
    start()
    mainloop()