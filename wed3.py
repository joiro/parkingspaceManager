'''Start'''
# Import of the modules for Tkinter GUI,
from Tkinter import *
import urllib2
import csv
import time

# Loads the csv file from the webpage and transform into list
csvfile = urllib2.urlopen("http://data.nottinghamtravelwise.org.uk/parking.csv")
datareader = csv.reader(csvfile.read().decode('utf-8').splitlines())
data = list(datareader)
olddata = list(data)

# Things to do
# 1. Frameless display of "Overview" window -> maybe use label widget instead of canvas
# 2. Sort function for the Alphabetical/Emptiest/Fullest buttons
# 3. Optimize structure

'''Variables'''
# Empty carparklist where the canvases get appended to, when running the for-loop in the GUI display section
carparklist = []

# Default variables that are refered to
updated = time.strftime("%H:%M")
start = 1
end = 6

'''Functions'''
# "Overview" window, which displays the status for all carparks combined
'''
def header():
    occupancy = 0
    capacity = 0
    percentage = 0
    for i in range(1,len(data)):
        occupancy += int(data[i][-6])
        capacity += int(data[i][1])
        percentage += int(data[i][-5])
        t = occupancy*100/capacity
    def status(s):
        h = 0
        for i in range(1,len(data)):
            h = h + data[i][6].count(s)
        return h
    top = Canvas(root,width=600,height=60,bg="grey")
    top.create_text(5,12,anchor="w",text="Overview",font=(None,"13","bold"))
    top.create_text(5,30,anchor="w",text="Spaces filled: "+str(occupancy))
    top.create_text(300,30,text="Spaces Available: "+str(capacity-occupancy))
    top.create_text(460,30,anchor="w",text="Percentage Filled: "+str(t)+"%")
    top.create_text(300,50,text="Statuses: Spaces: "+str(status("Spaces"))+", Almost Full: "+str(status("Almost"))+", Full: "+str(status(" Full"))+", Faulty: "+str(status("Faulty")))
    top.grid(row=0,column=0)
'''
def header():
    occupancy = 0
    capacity = 0
    percentage = 0
    for i in range(1,len(data)):
        occupancy += int(data[i][-6])
        capacity += int(data[i][1])
        percentage += int(data[i][-5])
        t = occupancy*100/capacity
    def status(s):
        h = 0
        for i in range(1,len(data)):
            h = h + data[i][6].count(s)
        return h
    overview = Label(root,text="Overview",font=(None,"13","bold"),bg="grey").grid(row=0,column=0)
    #top.create_text(5,12,anchor="w",text="Overview",font=(None,"13","bold"))
    #top.create_text(5,30,anchor="w",text="Spaces filled: "+str(occupancy))
    #top.create_text(300,30,text="Spaces Available: "+str(capacity-occupancy))
    #top.create_text(460,30,anchor="w",text="Percentage Filled: "+str(t)+"%")
    #top.create_text(300,50,text="Statuses: Spaces: "+str(status("Spaces"))+", Almost Full: "+str(status("Almost"))+", Full: "+str(status(" Full"))+", Faulty: "+str(status("Faulty")))
    #top.grid(row=0,column=0)

# "Carparks"-header above the carparks
def title():
    title = Label(root,text="Car Parks",font=(None,"13","bold")).grid(row=1,column=0)

# Function which formats and displays the content of the carparks
def values():
    global carparklist,change
    colour = ""
    a = 0
    for i in range(start,end):
        change = int(olddata[i][-5])-int(data[i][-5])
        carparklist[a].create_text(2,10,anchor="w",text=data[i][3])
        carparklist[a].create_text(300,10,text=data[i][-6]+" of"+data[i][1]+" places filled")
        if data[i][6] == " Spaces":
            colour = "green"
        elif data[i][6] == " Almost Full":
            colour = "orange"
        elif data[i][6] == " Full":
            colour = "red"
        elif data[i][6] == " Faulty":
            colour = "white"
        carparklist[a].create_rectangle(0,20,float(data[i][-5])*2,40,fill=colour)
        carparklist[a].create_text(2,30,anchor="w",text=data[i][-5]+"%")
        carparklist[a].create_text(230,25,anchor="w",text="Last updated at: "+data[i][-1][1:17])
        carparklist[a].create_text(550,30,text="Change: "+str(change)+"%")
        a = a + 1

# Code to run when the "left"-button is clicked, that displays the previous five carparks
def left():
    global start,end
    for y in range(0,len(carparklist)):
        carparklist[y].delete(ALL)
    buttons.delete(ALL)
    start = start - 5
    end = end - 5
    if start < 1:
        start = 1
        end = 6
    values()
    buttonvalue()

# Code to run when the "right"-button is clicked, that displayes the next five carparks
def right():
    global start,end
    for y in range(0,len(carparklist)):
        carparklist[y].delete(ALL)
    buttons.delete(ALL)
    start = start + 5
    end = end + 5
    if start > 21:
        start = 21
        end = 26
    values()
    buttonvalue()

# Code to run when the "Update"-button is clicked, that updates the csv file and adds the change to the carparks
def pullupdate():
    global data,change,olddata ,updated  
    update.delete(ALL)
    buttons.delete(ALL)
    for y in range(0,len(carparklist)):
        carparklist[y].delete(ALL)
    olddata = list(data)
    csvfile = urllib2.urlopen("http://data.nottinghamtravelwise.org.uk/parking.csv")
    datareader = csv.reader(csvfile.read().decode('utf-8').splitlines())
    data = list(datareader)
    updated = time.strftime("%H:%M")
    values()
    buttonvalue()
    console()

def sortalpha():
    print "sortalpha"

def sortempty():
    print "sortempty"

def sortfull():
    print "sortfull"

# Code to display the "left"/"right"-buttons, nested in a window
def buttonvalue():
    button1 = Button(buttons,text="<",command=left)
    button2 = Button(buttons,text=">",command=right)
    buttons.create_window(160,15,window=button1)
    buttons.create_text(300,15,text=str(start)+"-"+str(end-1)+"/"+str(len(data)-1))
    buttons.create_window(420,15,window=button2)
    buttons.grid(row=7,column=0)

# Code to display the "sort"- and "update"-buttons below the carparks, that are nested in windows for formatting purposes
def console():
    button3 = Button(root,text="Update",command=pullupdate)
    button4 = Button(root,text="Show Alphabetical",command=sortalpha)
    button5 = Button(root,text="Show Emptiest",command=sortempty)
    button6 = Button(root,text="Show Fullest",command=sortfull)
    update.create_text(300,10,text="Last update: "+updated)
    update.create_window(160,10,window=button3)
    update.create_window(160,35,window=button4)
    update.create_window(300,35,window=button5)
    update.create_window(420,35,window=button6)
    update.grid(row=8,column=0)

# Code to display the Label with Source information at the very bottomn of the program
def bottom():
    bottom = Label(
        text="Contains Public Sector Information licensed under the Open Government License v1.0.").grid(row=9,column=0)

'''GUI display'''
root = Tk()
# Change the title of the program window
root.title("Nottingham Car Parks Monitor")

# The tkinter object get created and the functions containing the values and elements get called
header()
title()
# Creation of five canvases
for x in range(5):
    carpark = Canvas(root,width=600,height=40,bd=1,relief="solid")
    carparklist.append(carpark)
    carparklist[x].grid(row=x+2,column=0)
values()    
buttons = Canvas(root,width=600,height=25)
buttonvalue()
update = Canvas(root,width=600,height=45)
console()
bottom()

mainloop()
