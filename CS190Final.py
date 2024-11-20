#CS 190 Final project

from tkinter import *
from PIL import ImageTk, Image
import json
import requests
import pygame

def getData():
    url = "https://open-weather13.p.rapidapi.com/city/fivedaysforcast/38.8697/-106.9878"

    headers = {
        "X-RapidAPI-Key": "7083eed481mshe8e9406af0e7a6fp115a8ejsn625968e27795",
        "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    try:
        with open("forecast.json","w") as f:
            json.dump(data,f)
    except Exception as e:
        print (e)
        
def powda(snow):
    powder = False
    if "snow" in snow:
        powder = True
    else:
        powder = False
    return powder

def BSfunction():
    pygame.init()
    pygame.mixer.music.load('pow.mp3')
    pygame.mixer.music.play()

getData()

snowD = []
tempD = []
windD = []

with open ("forecast.json","r",encoding="UTF-8") as f:
    json_object = json.loads(f.read())
    
kTemp = (int(json_object["list"][0]["main"]["temp"]))
for i in range (0,5):
    wind = json_object["list"][i]["wind"]["speed"]
    windD.append(wind)

for i in range (0,5):
    kTemp = json_object["list"][i]["main"]["temp"]
    Ctemp = kTemp - 273
    temp = Ctemp * (9/5) + 32
    temp = round(temp)
    tempD.append(str(temp) + "°")

for i in range (0,5):
    con = json_object["list"][i]["weather"][0]["description"]
    snowD.append(con)
    
powDay = powda(snowD)

r = Tk()
c = Canvas(width=1030, height=500)
c.grid()

try:
    img = ImageTk.PhotoImage(Image.open("ski.png"))
    c.create_image(20, 20, anchor=NW, image=img)
except Exception as e:
        print (e)

day1 = c.create_oval(0,0,175,175,fill="white")
c.move(day1,50,100)
day2 = c.create_oval(0,0,175,175,fill="white")
c.move(day2,240,100)
day3 = c.create_oval(0,0,175,175,fill="white")
c.move(day3,430,100)
day4 = c.create_oval(0,0,175,175,fill="white")
c.move(day4,620,100)
day5 = c.create_oval(0,0,175,175,fill="white")
c.move(day5,810,100)

day1t = c.create_text (135,60,text="Today")
day2t = c.create_text (325,60,text="Tomorrow")
day3t = c.create_text (515,60,text="Day 3")
day4t = c.create_text (705,60,text="Day 4")
day5t = c.create_text (895,60,text="Day 5")

con1t = c.create_text (135,210,text=snowD[0])
con2t = c.create_text (325,210,text=snowD[1])
con3t = c.create_text (515,210,text=snowD[2])
con4t = c.create_text (705,210,text=snowD[3])
con5t = c.create_text (895,210,text=snowD[4])

con1t = c.create_text (135,160,text=tempD[0])
con2t = c.create_text (325,160,text=tempD[1])
con3t = c.create_text (515,160,text=tempD[2])
con4t = c.create_text (705,160,text=tempD[3])
con5t = c.create_text (895,160,text=tempD[4])

if powDay == True:
    c.create_text(520,350,text="POWDER DAY! YOU SHOULD SKIP CLASS")
    BSfunction()

r.mainloop()