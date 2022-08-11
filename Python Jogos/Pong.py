from tkinter import Y
import turtle
import os

# Criando Tela
wn = turtle.Screen()
wn.title("Pong by JoaovictorLFS")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#plataforma 1
plataforma_a = turtle.Turtle()
plataforma_a.speed(0)
plataforma_a.shape("square")
plataforma_a.color("white")
plataforma_a.shapesize(stretch_wid=5, stretch_len=1)
plataforma_a.penup()
plataforma_a.goto(-350, 0)

#plataforma 2
plataforma_b = turtle.Turtle()
plataforma_b.speed(0)
plataforma_b.shape("square")
plataforma_b.color("white")
plataforma_b.shapesize(stretch_wid=5, stretch_len=1)
plataforma_b.penup()
plataforma_b.goto(350, 0)

# bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0,0)
bola.dx = 0.5
bola.dy = -0.5

# Movimentação
def plataforma_a_up():
    y = plataforma_a.ycor()
    y += 20
    plataforma_a.sety(y)

def plataforma_a_down():
    y = plataforma_a.ycor()
    y -= 20
    plataforma_a.sety(y)

def plataforma_b_up():
    y = plataforma_b.ycor()
    y += 20
    plataforma_b.sety(y)

def plataforma_b_down():
    y = plataforma_b.ycor()
    y -= 20
    plataforma_b.sety(y)

#teclas
wn.listen()
wn.onkeypress(plataforma_a_up, "w")
wn.onkeypress(plataforma_a_down, "s")
wn.onkeypress(plataforma_b_up, "Up")
wn.onkeypress(plataforma_b_down, "Down")

#Loop Tela
while True:
    wn.update()

    # Movimentação Bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)
    # Limitando a movimentação bola
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
    
    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1

    if (bola.xcor() > 340 and bola.ycor() < 350) and (bola.ycor() < plataforma_b.ycor() + 40 and bola.ycor() > plataforma_b.ycor() -40): 
        bola.setx(340)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.ycor() > -350) and (bola.ycor() < plataforma_a.ycor() + 40 and bola.ycor() > plataforma_a.ycor() -40): 
        bola.setx(-340)
        bola.dx *= -1