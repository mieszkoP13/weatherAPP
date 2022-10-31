import appDB

import json
from tkinter import *
import tkinter as tk
import tkinter.font
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import os
from dotenv import load_dotenv

load_dotenv()

BG_COLOR = '#afe5fc'
BOX_COLOR = '#7693be'
HBOX_COLOR = '#8dace8'

# w - window, root screen
w=Tk()
w.title('Weather App')
w.geometry('1100x700+800+400')
w.configure(bg=BG_COLOR)
w.resizable(False, False)

FAMILY = "Times New Roman"
FONT18 = tkinter.font.Font(family=FAMILY, size=18)
FONT19 = tkinter.font.Font(family=FAMILY, size=19)
FONT20 = tkinter.font.Font(family=FAMILY, size=20)
FONT26 = tkinter.font.Font(family=FAMILY, size=26)

import history

windDict = ((0.5,2.1,"Light Air"),(2.1,3.6,"Light Breeze"),(3.6,5.7,"Gentle Breeze"),(5.7,8.8,"Moderete Breeze"),(8.8,11.1,"Fresh Breeze"),(11.1,float('inf'),"Strong Breeze"))

def windClassification(w):
   for classif in windDict:
      if w > classif[0] and w < classif[1]:
         return str(w) + " (" + classif[2] + ")"     

def getWeather():
   try:
      btn1.config(state=DISABLED)
      btn1.update()

      city=entry.get()
      geolocator=Nominatim(user_agent="geoapiExercises")
      location=geolocator.geocode(city)
      obj=TimezoneFinder()
      res = obj.timezone_at(lng=location.longitude,lat=location.latitude)
      
      home=pytz.timezone(res)
      localTime=datetime.now(home)
      currTime=localTime.strftime('%I:%M %p')

      clock.config(text=currTime)
      name.config(text='CURRENT WEATHER')

      api="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,os.getenv('APIkey'))

      jsonData = requests.get(api).json()
      condition = jsonData['weather'][0]['main']
      description = jsonData['weather'][0]['description']
      temperature = int(jsonData['main']['temp']-273.15) # K deg --> C deg
      pressure = jsonData['main']['pressure']
      humidity = jsonData['main']['humidity']
      wind = jsonData['wind']['speed']
      if "rain" in jsonData:
         rain = jsonData['rain']['1h']
         rai.config(text=rain)
      else:
         rai.config(text="No information")

      temp.config(text=(temperature,'°'))
      cond.config(text=(condition,'|','Feels','Like',temperature,'°'))

      win.config(text=windClassification(wind))
      hum.config(text=humidity) 
      desc.config(text=description)
      pres.config(text=pressure)

      # adding a db record
      appDB.addOne(city,currTime)
      history.addHistoryItem(city,currTime)

      btn1.update()
      btn1.config(state=NORMAL)
      btn1.update()
      
   except Exception as e:
      messagebox.showerror('Weather App','Invalid entry or insufficient internet connection!')
      btn1.config(state=NORMAL)
      btn1.update()

searchBImg = PhotoImage(file='./images/searchBox2.png')
img1=Label(image=searchBImg,bg=BG_COLOR)
img1.place(x=50,y=40)

entry = Entry(width=16,font=FONT26, bg=BOX_COLOR,highlightthickness=0,border=0,fg='#FFFFFF')
entry.place(x=70,y=55)
entry.focus()

searchImg = PhotoImage(file='./images/ssearch.png')
btn1=Button(image=searchImg,cursor='hand2', bg=BOX_COLOR,activebackground=BOX_COLOR,highlightthickness=0,border=0,state=NORMAL,command=getWeather)
w.bind('<Return>',lambda event:getWeather())
btn1.place(x=420,y=50)

logoImg = PhotoImage(file='./images/logo.png')
Label(image=logoImg,bg=BG_COLOR).place(x=250,y=150)

bboxImg = PhotoImage(file='./images/bbox2.png')
Label(image=bboxImg,bg=BG_COLOR).place(x=50,y=350)


name=Label(font=FONT18,bg=BG_COLOR)
name.place(x=60,y=130)
clock=Label(font=FONT18,bg=BG_COLOR)
clock.place(x=60,y=160)


# bottom box content section

iconTuple = (PhotoImage(file='./images/wind2.png'),PhotoImage(file='./images/hum2.png'),PhotoImage(file='./images/desc2.png'),PhotoImage(file='./images/pres2.png'),PhotoImage(file='./images/rain2.png'))

for i in range(5):
   Label(image=iconTuple[i],bg=BOX_COLOR).place(x=90,y=375+i*53)

Label(text='WIND',font=FONT20,fg='white',bg=BOX_COLOR).place(x=140,y=380)
Label(text='HUMIDITY',font=FONT20,fg='white',bg=BOX_COLOR).place(x=140,y=430)
Label(text='DESCRIPTION',font=FONT20,fg='white',bg=BOX_COLOR).place(x=140,y=485)
Label(text='PRESSURE',font=FONT20,fg='white',bg=BOX_COLOR).place(x=140,y=540)
Label(text='RAIN',font=FONT20,fg='white',bg=BOX_COLOR).place(x=140,y=590)

temp=Label(font=FONT20,bg=BG_COLOR)
temp.place(x=460,y=260)
cond=Label(font=FONT20,bg=BG_COLOR)
cond.place(x=460,y=300)

win=Label(text='',font=FONT20,fg='white',width=23,anchor=W,bg=BOX_COLOR)
win.place(x=360,y=380)
hum=Label(text='',font=FONT20,fg='white',width=23,anchor=W,bg=BOX_COLOR)
hum.place(x=360,y=430)
desc=Label(text='',font=FONT20,fg='white',width=23,anchor=W,bg=BOX_COLOR)
desc.place(x=360,y=485)
pres=Label(text='',font=FONT20,fg='white',width=23,anchor=W,bg=BOX_COLOR)
pres.place(x=360,y=540)
rai=Label(text='',font=FONT20,fg='white',width=23,anchor=W,bg=BOX_COLOR)
rai.place(x=360,y=590)

w.mainloop()