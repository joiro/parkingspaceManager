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
'''TEST CODE ON LAB COMPUTERS!!!!'''
# 1. check variable names
# 2. Try reusing code

'''Variables'''
# Empty carparklist where the canvases get appended to, when running the for-loop in the GUI display section
carparklist = []

# Set the time for "last updated" when the program gets openend
updated = time.strftime("%H:%M")

# Default variables that are refered to
start = 1
end = 6

'''Functions'''
# "Overview" window, which displays the status for all carparks combined
def header():
    occupancy = 0
    capacity = 0
    percentage = 0
    for i in range(1,len(data)):
        occupancy += int(data[i][-6])
        capacity += int(data[i][1])
        percentage += int(data[i][-5])
        totalpercentage = occupancy*100/capacity
    def status(s):
        h = 0
        for i in range(1,len(data)):
            h = h + data[i][6].count(s)
        return h
    top.create_text(5,12,anchor="w",text="Overview",font=(None,"13","bold"))
    top.create_text(5,30,anchor="w",text="Spaces filled: "+str(occupancy))
    top.create_text(305,30,text="Spaces Available: "+str(capacity-occupancy))
    top.create_text(610,30,anchor="e",text="Percentage Filled: "+str(totalpercentage)+"%")
    top.create_text(305,50,text="Statuses: Spaces: "+str(status("Spaces"))+", Almost Full: "+str(status("Almost"))+", Full: "+str(status(" Full"))+", Faulty: "+str(status("Faulty")))
    top.grid(row=0,column=0)

# "Carparks" header above the carparks
def title():
    titlelabel = Label(root,height=1,text="Car Parks",font=(None,"13","bold")).grid(row=1,column=0)

# Format and display the content of the carparks for each row in the list
def values():
    global carparklist
    colour = ""
    a = 0
    for i in range(start,end):
        change = int(data[i][-5])-int(olddata[i][-5])
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
    global data,olddata,updated
    top.delete(ALL)
    update.delete(ALL)
    buttons.delete(ALL)
    for y in range(0,len(carparklist)):
        carparklist[y].delete(ALL)
    olddata = list(data)
    csvfile = urllib2.urlopen("http://data.nottinghamtravelwise.org.uk/parking.csv")
    datareader = csv.reader(csvfile.read().decode('utf-8').splitlines())
    data = list(datareader)
    updated = time.strftime("%H:%M")
    header()
    values()
    buttonvalue()
    console()
    #for i in range(start,end):
        #change = int(data[i][-5])-int(olddata[i][-5])

# Sort the datalist alphabetically 
def sortalpha():
    for y in range(0,len(carparklist)):
        carparklist[y].delete(ALL)
    del data[0]
    data.sort(key=lambda ShortDescription: ShortDescription[3], reverse=False)
    values()

# Sort the datalist by Occupancy Percentage ascending
def sortempty():
    for y in range(0,len(carparklist)):
        carparklist[y].delete(ALL)
    data.sort(key=lambda OccupancyPercentage: OccupancyPercentage[9], reverse=False)
    values()

# Sort the datalist by Occupancy Percentage decending
def sortfull():
    for y in range(0,len(carparklist)):
        carparklist[y].delete(ALL)
    data.sort(key=lambda OccupancyPercentage: OccupancyPercentage[9], reverse=True)
    values()

# Display the "left"/"right" buttons, nested in a window
def buttonvalue():
    button1 = Button(buttons,text="<",command=left)
    button2 = Button(buttons,text=">",command=right)
    buttons.create_window(160,15,window=button1)
    buttons.create_text(300,15,text=str(start)+"-"+str(end-1)+"/"+str(len(data)-1))
    buttons.create_window(420,15,window=button2)
    buttons.grid(row=7,column=0)

# Display the "sort"- and "update" buttons below the carparks, that are nested in windows for formatting purposes
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

# Display the Label with Source information at the very bottomn of the program
def bottom():
    bottom = Label(
        text="Contains Public Sector Information licensed under the Open Government License v1.0.").grid(row=9,column=0)

'''GUI display'''
root = Tk()
# Change the title of the program window
root.title("Nottingham Car Parks Monitor")

# Create canvas for the overview and call the functions containing the values and elements
top = Canvas(root,width=610,height=55,bg="grey",highlightbackground="grey")
header()
title()
# Create five canvases for the carparks
for x in range(5):
    carpark = Canvas(root,width=600,height=40,bd=1,relief="solid")
    carparklist.append(carpark)
    carparklist[x].grid(row=x+2,column=0,pady=2)
values()
# Create canvas for Navigation buttons and call the function for text and windows
buttons = Canvas(root,width=600,height=25)
buttonvalue()
# Create canvas for update and sorting buttons and call the function for the text and windows
update = Canvas(root,width=600,height=45)
console()
bottom()

mainloop()
