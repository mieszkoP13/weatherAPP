import appDB

from tkinter import *
import tkinter as tk
import tkinter.font
import platform

BG_COLOR = '#afe5fc'
BOX_COLOR = '#7693be'
HBOX_COLOR = '#8dace8'

# some, at first glance, peculiar fonts definitions,
# however if defined as follows both windows and linux
# have no problem with compilation and interpretation of
# different font families and sizes
FAMILY = "Times New Roman"
FONT17 = tkinter.font.Font(family=FAMILY , size=17)
FONT18 = tkinter.font.Font(family=FAMILY, size=18)
FONT20 = tkinter.font.Font(family=FAMILY, size=20)
FONT21 = tkinter.font.Font(family=FAMILY, size=21)
FONT_HTITLE = None
if platform.system() == 'Windows':
   FONT_HTITLE = FONT20
else:
   FONT_HTITLE = FONT17

hboxImg = PhotoImage(file='./images/historyBox2.png')
Label(image=hboxImg,bg=BG_COLOR).place(x=800,y=35)
Label(text='History of recently\nsearched weather',font=FONT_HTITLE,fg='white',bg=HBOX_COLOR).place(x=820,y=55)

# initializing history tab items so that they are invisible at first
hItemImg = PhotoImage(file='./images/historyItem.png')
hBoxList=[]
hBoxCityList=[]
hBoxTimeList=[]
for i in range(4):
   hBoxList.append(Label(image=hItemImg,bg=HBOX_COLOR))
   hBoxList[i].place(x=820,y=130+i*127,width=0,height=0)
   hBoxCityList.append(Label(text='',font=FONT21,fg='white',bg=HBOX_COLOR,width=10,anchor=W))
   hBoxCityList[i].place(x=840,y=150+i*127)
   hBoxTimeList.append(Label(text='',font=FONT21,fg='white',bg=HBOX_COLOR))
   hBoxTimeList[i].place(x=840,y=190+i*127)

def addHistoryItem(city,localTime):
   hBoxList[addHistoryItem.counter].place(width=210,height=120)
   hBoxCityList[addHistoryItem.counter].config(text=city.title(),bg=BOX_COLOR)
   hBoxTimeList[addHistoryItem.counter].config(text=localTime,bg=BOX_COLOR)

   if addHistoryItem.counter < 3:
      addHistoryItem.counter += 1
   else:
      addHistoryItem.counter = 0

addHistoryItem.counter = 0

def deleteAllHistoryItems():
   for i in range(4):
      hBoxList[i].place(width=0,height=0)
      hBoxCityList[i].config(text='',bg=HBOX_COLOR)
      hBoxTimeList[i].config(text='',bg=HBOX_COLOR)
   addHistoryItem.counter = 0

def clearHistory():
   appDB.deleteAll()
   deleteAllHistoryItems()

cHistImg = PhotoImage(file='./images/cHist.png')
Button(image=cHistImg,text='Clear\nHistory',compound='center',cursor='hand2',font=FONT18,fg='white', bg=BG_COLOR,activebackground=BG_COLOR,highlightthickness=0,border=0,command=clearHistory).place(x=660,y=30)

def retrieveHistory():
   lastTuple = appDB.getUpTo4LastRecords()
   for rec in reversed(lastTuple):
      addHistoryItem(rec[0],rec[1])

   # get back to last point or start from the beginning if there are 4 or more records in the db
   n = appDB.count()[0]
   if n<4:
      addHistoryItem.counter = n % 4
      
retrieveHistory()