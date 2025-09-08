from turtle import Screen, Turtle
import turtle
import random

# Yazı tipi ayarları (puan ve zaman yazıları için)
FONT = ('Arial', 20, 'normal')

# Ekran ayarları
screen = Screen()
screen.bgcolor("light blue")   # Arka plan rengi
screen.setup(width=800, height=600)  # Pencere boyutu

# Kaplumbağaların yerleşiminde kullanılacak katsayı
turtle_coordinates = 10

# Kaplumbağaları ve oyunun durumunu tutacak değişkenler
turtle_list = []
score = 0
game_over = False

# Puan ve geri sayımı göstermek için ayrı kaplumbağalar
score_turtle = Turtle()
countdown_turtle = Turtle()


def setup_score_turtle():
    """Ekranın üst kısmında skor yazısını hazırlayan fonksiyon"""
    score_turtle.penup()
    score_turtle.hideturtle()
    score_turtle.color("dark blue")

    # Skoru ekranın üst kısmına yazdır
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score: 0", align="center", font=FONT)


def make_turtle(x, y):

    t = Turtle()

    # Kaplumbağaya tıklandığında çalışacak olay
    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", align="center", font=FONT)

    # Kaplumbağanın özelliklerini ayarlama
    t.onclick(handle_click)  # Tıklama olayını bağla
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark green")
    t.goto(x * turtle_coordinates, y * turtle_coordinates)
    turtle_list.append(t)  # Kaplumbağayı listeye ekle


# Kaplumbağaların konumlarını ayarlamak için koordinatlar
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]

def location_turtles():
    """Kaplumbağaları belirlenen koordinatlara yerleştirir"""
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    """Tüm kaplumbağaları gizler"""
    for k in turtle_list:
        k.hideturtle()

def show_turtles_randomly():
    """Her 0.5 saniyede rastgele bir kaplumbağayı gösterir"""
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)  # 500 ms sonra tekrar çalıştır

def countdown(time):
    """Geri sayımı ekranda gösterir ve süre bitince oyunu bitirir"""
    global game_over
    countdown_turtle.penup()
    countdown_turtle.hideturtle()
    countdown_turtle.color("red")

    # Geri sayımı ekranda skordan biraz aşağıya yazdır
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.write(arg="Time: {}".format(time), align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)  # 1 saniye sonra azalt
    else:
        game_over = True
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", align="center", font=FONT)


def game_start():
    """Oyunu başlatan ana fonksiyon"""
    turtle.tracer(0)  # Animasyonu hızlandırmak için kapat
    setup_score_turtle()
    location_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)  # 10 saniyelik süre
    turtle.tracer(1)  # Animasyonu aç

# Oyunu başlat
game_start()
turtle.mainloop()
