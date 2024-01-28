

import turtle
import random

# Ekranı oluştur
ekran = turtle.Screen()
ekran.bgcolor("lightblue")
ekran.title("Rastgele Kaplumbağa")

# Rastgele kaplumbağa pozisyonu
def rastgele_pozisyon():
    x = random.randint(-400, 400)  # x koordinatı -400 ile 400 arasında
    y = random.randint(-300, 300)  # y koordinatı -300 ile 300 arasında
    return x, y

# Kaplumbağa nesnesini oluştur

kaplumbağa = turtle.Turtle()
kaplumbağa.shape("turtle")
kaplumbağa.color("green")
kaplumbağa.speed(1)

# Skor değişkeni
skor = 0
high_score = 0
# Geri sayım süresi (saniye cinsinden)
geri_sayim_suresi = 10

# Skor gösterim nesnesini oluştur
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0  Time: {}".format(geri_sayim_suresi),
                    align="center", font=("Courier", 24, "normal"))

# Geri sayım fonksiyonu
def geri_sayim():
    global geri_sayim_suresi
    if geri_sayim_suresi > 0:
        geri_sayim_suresi -= 1
        update_score_display()
        ekran.ontimer(geri_sayim, 1000)  # 1 saniye beklet ve fonksiyonu çağır
    else:
        update_score_display()
        tekrar_basla = turtle.textinput("Süre Bitti!", "Yeniden başlamak için 'E' tuşuna basın:")
        if tekrar_basla.lower() == 'e':
            reset_game()

# İlk geri sayım başlatma
ekran.ontimer(geri_sayim, 1000)  # İlk çağrı için 1 saniye beklet

# Skoru artıran fonksiyon
def skor_artir(x, y):
    global skor, high_score
    skor += 1
    if skor > high_score:
        high_score = skor
    print("Skor:", skor)
    update_score_display()
    # Yeni bir rastgele konuma taşı
    kaplumbağa.penup()
    yeni_pozisyon = rastgele_pozisyon()
    kaplumbağa.goto(yeni_pozisyon)
    kaplumbağa.penup()

# Fare tıklama olayını ekle
kaplumbağa.onclick(skor_artir)

# Skor gösterimini güncelleme fonksiyonu
def update_score_display():
    score_display.clear()
    score_display.write("Score: {}  High Score: {}  Time: {}".format(skor, high_score, geri_sayim_suresi),
                        align="center", font=("Courier", 24, "normal"))

# Oyunu sıfırla fonksiyonu
def reset_game():
    global skor, geri_sayim_suresi
    skor = 0
    geri_sayim_suresi = 10
    update_score_display()
    ekran.ontimer(geri_sayim, 1000)  # İlk çağrı için 1 saniye beklet
    reset_turtle_positions()

# Kaplumbağaları rastgele konumlara taşıma
def reset_turtle_positions():
    for _ in range(10):  # 10 defa tekrar et
        x, y = rastgele_pozisyon()
        kaplumbağa.penup()
        kaplumbağa.goto(x, y)
        kaplumbağa.pendown()

# İlk oyun başlangıcı
reset_game()

# Ekranı kapat
turtle.mainloop()