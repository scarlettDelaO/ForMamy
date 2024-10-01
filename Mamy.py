import turtle
import time

def draw_heart():
    # Configuración de la ventana
    window = turtle.Screen()
    window.title("De mi. Para mamy")
    window.setup(width=800, height=600)
    window.bgcolor("lightyellow")

    # Crear la "tortuga" para dibujar el corazón
    heart = turtle.Turtle()
    heart.speed(2)
    heart.color("red")

    # Dibujar el corazón
    heart.penup()
    heart.goto(0, 0)
    heart.pendown()
    heart.begin_fill()
    heart.left(140)
    heart.forward(180)
    heart.circle(-90, 200)
    heart.left(120)
    heart.circle(-90, 200)
    heart.forward(180)
    heart.end_fill()

    # Añadir el texto animado de forma horizontal
    animate_text(heart)

    # Ocultar la "tortuga"
    heart.hideturtle()

    # Mantener la ventana abierta
    window.mainloop()

def animate_text(t):
    # Ajustar posición y animar el texto de manera horizontal
    messages = [
        ("¡Feliz Cumpleaños, Mamá!", "purple", 30, -150),
        ("\nCon cariño, Scarlett ❤️", "blue", 18, -190)
    ]
    for message, color, font_size, y in messages:
        t.penup()
        t.goto(-350, y)  # Ajustar posición de inicio para centrar
        t.color(color)
        for char in message:
            t.write(char, align="left", font=("Bunny Runny", font_size, "bold"))
            t.setx(t.xcor() + 30)  # Mover horizontalmente por cada letra
            time.sleep(0.1)  # Delay para la animación de cada letra

# Dibujar el corazón y mostrar el texto animado
draw_heart()
