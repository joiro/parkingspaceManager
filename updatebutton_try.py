from Tkinter import *
import urllib2
import csv
import sys

csvfile = urllib2.urlopen("http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642")
datareader = csv.reader(csvfile.read().decode('utf-8').splitlines())
data = list(datareader)

# Things to do
# 1. Install command for buttons that display different areas of the data
# 2. Frameless display of "Overview" window -> maybe use label widget instead of canvas
# 3. Correct Percentage value (total occupancy divided by total capacity is not the percentage shown
# 4. Update button should reload the data list
# 5. Sort function for the Alphabetical/Emptiest/Fullest buttons

# Creating functions for all elements apart the carpark. the functions will be called outside of the class
# the init function contains the elements for the carpark. create an instance
class elements(Canvas):

    def __init__(self,parent):
        Canvas.__init__(self,parent)
        self.config(width=600,height=40,bd=1,relief="solid")
        self.carpark()

    def carpark(self):
        colour = "blue"
        self.create_text(2,10,anchor="w",text=data[i][3])
        self.create_text(300,10,text=data[i][-6]+" of"+data[i][1]+" places filled")
        if data[i][6] == " Spaces":
            colour = "green"
        elif data[i][6] == " Almost Full":
            colour = "orange"
        elif data[i][6] == " Full":
            colour = "red"
        elif data[i][6] == " Faulty":
            colour = "white"
        self.create_rectangle(0,20,float(data[i][-5])*2,40,fill=colour)
        self.create_text(2,30,anchor="w",text=data[i][-5]+"%")
        self.create_text(230,25,anchor="w",text="Last updated at: "+data[i][-1][1:17])
        self.create_text(550,30,text="Change: "+"%")

def display():
    global i
    for i in range(start,end):
        elements(root).pack()

def top():
    a = 0
    b = 0
    c = 0
    for i in range(1,len(data)):
        a += int(data[i][-6])
        b += int(data[i][1])
        c += int(data[i][-5])
        t = c/(len(data)-1)
    def status(s):
        h = 0
        for i in range(1,len(data)):
            h = h + data[i][6].count(s)
        return h
    top = Canvas(root,width=600,height=60,bg="grey")
    top.create_text(5,12,anchor="w",text="Overview",font=(None,"13","bold"))
    top.create_text(5,30,anchor="w",text="Spaces filled: "+str(a))
    top.create_text(300,30,text="Spaces Available: "+str(b-a))
    top.create_text(460,30,anchor="w",text="Percentage Filled: "+str(t)+"%")
    top.create_text(300,50,text="Statuses: Spaces: "+str(status("Spaces"))+", Almost Full: "+str(status("Almost"))+", Full: "+str(status(" Full"))+", Faulty: "+str(status("Faulty")))
    top.pack()

def right():
    global start
    global end
    start = start + 5
    end = end + 5
    if start > 21:
        start = 21
        end = 26
    print "start "+str(start)
    print "end "+str(end)
    for i in range(start,end):
        elements(root).pack_forget()

def left():
    global start
    global end
    start = start - 5
    end = end - 5
    if start < 1:
        start = 1
        end = 6
    print start
    print end

def title():
    title = Canvas(root,width=600,height=10)
    title.create_text(300,8,text="Car Parks",font=(None,"13","bold"))
    title.pack()
    
def buttons():
    buttons = Canvas(root,width=600,height=20)
    button1 = Button(buttons,text="<",command=left)
    button2 = Button(buttons,text=">",command=right)
    buttons.create_window(160,10,window=button1)
    buttons.create_text(300,10,text=str(start)+"-"+str(end-1)+"/"+str(len(data)-1))
    buttons.create_window(420,10,window=button2)
    buttons.pack()

def push():
    global i, data
    olddata = list(data)
    csvfile = urllib2.urlopen("http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642")
    datareader = csv.reader(csvfile.read().decode('utf-8').splitlines())
    data = list(datareader)
    print "new: "+data[1][-5]
    print "old: "+olddata[1][-5]
    change = int(olddata[1][-5])-int(data[1][-5])
    print change

def console():
    update = Canvas(root,width=600,height=45)
    button3 = Button(root,text="Update",command=push)
    button4 = Button(root,text="Show Alphabetical")
    button5 = Button(root,text="Show Emptiest")
    button6 = Button(root,text="Show Fullest")
    update.create_text(300,10,text="Last update: "+data[1][-1][12:17])
    update.create_window(160,10,window=button3)
    update.create_window(160,35,window=button4)
    update.create_window(300,35,window=button5)
    update.create_window(420,35,window=button6)
    update.pack()
        
def bottom():
    bottom = Label(width=70,height=1,text="Contains Public Sector Information licensed under the Open Government License v1.0.")
    bottom.pack()

root = Tk()
root.title("Nottingham Car Parks Monitor")
start = 1
end = 6
top()
title()
display()
buttons()
console()
bottom()

mainloop()
