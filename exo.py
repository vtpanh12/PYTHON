import turtle

# Thiết lập môi trường vẽ
window = turtle.Screen()
window.bgcolor("white")

# Tạo một đối tượng Turtle
pen = turtle.Turtle()
pen.speed(3)  # Tốc độ vẽ (chậm)

# Vẽ chữ 
pen.backward(60)
pen.right(90)
pen.forward(40)
pen.right(90)
pen.backward(60)
pen.forward(60)
pen.left(90)
pen.forward(40)
pen.right(90)
pen.backward(60)

pen.penup()
pen.goto(0, -80)
pen.pendown()
pen.right(130)
pen.forward(100)
pen.backward(50)
pen.left(80)
pen.forward(50)
pen.backward(100)

pen.penup()
pen.goto(120, -70)
pen.pendown()
pen.right(90)
pen.circle(40)

window.exitonclick()
