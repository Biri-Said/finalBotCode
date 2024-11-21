import random


def sifre_olusturucu(sifre_uzunlugu):
    ogeler = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-/*!&$#?=@<>"
    sifre = ""

    for i in range(sifre_uzunlugu):
        sifre += random.choice(ogeler)

    return sifre


def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"
    
def film_öner():
    filmler = ["Oppenheimer" , "Yıldızlararası" , "Fnaf" , "Hungry Games" , "John wick"]
    film = random.choice(filmler)
    return film

def dizi_öner():
    diziler = ["The Boys" , "Breaking Bad" , "Prison Break" "Game of Thrones" , "Rick and Morty" , "South Park" , "Güç Yüzükleri" , "the Office" , "Invincible" , "The Walking Dead" , "Young Sheldon" , "The Platform"]
    dizi = random.cgoice(diziler)
    return dizi


def topla(ctx, x = 0 , y = 0):
    return x + y


def çarp(ctx, a = 0 , b = 0):
    return(a * b)


def böl(ctx, a = 0 , b = 0):
    if a % b > 0:
        return "bu sayı bölünemiyor"
    else:
        return a / b



    

def faktoriyel(ctx, n = 0):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)
