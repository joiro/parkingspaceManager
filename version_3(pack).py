from Tkinter import *
import urllib2
import csv

# load the csv file from the webpage and transform into list
csvfile = urllib2.urlopen("http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642")
datareader = csv.reader(csvfile.read().decode('utf-8').splitlines())
data = list(datareader)
olddata = list(data)

# Things to do
# 1. Install command for buttons that display different areas of the data
# 2. Frameless display of "Overview" window -> maybe use label widget instead of canvas
# 3. Correct Percentage value (total occupancy divided by total capacity is not the percentage shown
# 4. Update button should reload the data list
# 5. Sort function for the Alphabetical/Emptiest/Fullest buttons

# Display of the "Overview" window, which displayes the status for all carparks combined
def header():
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

    top.create_text(5,12,anchor="w",text="Overview",font=(None,"13","bold"))
    top.create_text(5,30,anchor="w",text="Spaces filled: "+str(a))
    top.create_text(300,30,text="Spaces Available: "+str(b-a))
    top.create_text(460,30,anchor="w",text="Percentage Filled: "+str(t)+"%")
    top.create_text(300,50,text="Statuses: Spaces: "+str(status("Spaces"))+", Almost Full: "+str(status("Almost"))+", Full: "+str(status(" Full"))+", Faulty: "+str(status("Faulty")))
    top.pack()

# Display of the "Carparks" header above the carparks
def title():
    title = Label(width=70,height=1,text="Carparks",font=(None,"13","bold")).pack()

# Function which formats the content of the carparks
def values():
    colour = "blue"
    carpark.create_text(2,10,anchor="w",text=data[i][3])
    carpark.create_text(300,10,text=data[i][-6]+" of"+data[i][1]+" places filled")
    if data[i][6] == " Spaces":
        colour = "green"
    elif data[i][6] == " Almost Full":
        colour = "orange"
    elif data[i][6] == " Full":
        colour = "red"
    elif data[i][6] == " Faulty":
        colour = "white"
    carpark.create_rectangle(0,20,float(data[i][-5])*2,40,fill=colour)
    carpark.create_text(2,30,anchor="w",text=data[i][-5]+"%")
    carpark.create_text(230,25,anchor="w",text="Last updated at: "+data[i][-1][1:17])
    carpark.create_text(550,30,text="Change: "+str(change)+"%")

# Function for the command of the "left" button, that displayes the previous five carparks        
def left():
    global carpark,i,j
    carpark.delete(ALL)
    buttons.delete(ALL)
    i = i - 5
    j = j - 5
    if i < 1:
        i = 1
        j = 6
    values()
    buttonvalue()

# Function for the command of the "right" button, that displayes the next five carparks
def right():
    global carpark,i,j
    carpark.delete(ALL)
    buttons.delete(ALL)
    i = i + 5
    j = j + 5
    if i > 21:
        i = 21
        j = 26
    values()
    buttonvalue()

# Function for the command of the "Update" button, that updates the csv file and adds the change to the carparks
def push():
    global i,data,change,olddata
    top.delete(ALL)
    update.delete(ALL)
    carpark.delete(ALL)
    olddata = list(data)
    csvfile = urllib2.urlopen("http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642")
    datareader = csv.reader(csvfile.read().decode('utf-8').splitlines())
    data = list(datareader)
    print "new: "+data[i][-5]
    print "old: "+olddata[i][-5]
    change = int(olddata[i][-5])-int(data[i][-5])
    print change
    header()
    values()
    console()

def buttonvalue():
    button1 = Button(buttons,text="<",command=left)
    button2 = Button(buttons,text=">",command=right)
    buttons.create_window(160,10,window=button1)
    buttons.create_text(300,10,text=str(i)+"-"+str(i+4)+"/"+str(len(data)-1))
    buttons.create_window(420,10,window=button2)
    buttons.pack()

def console():
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
i = 1
j = 6
olddata = 0
change = 0

top = Canvas(root,width=600,height=60,bg="grey")
header()
title()
for i in range(i,j):
    carpark = Canvas(root,width=600,height=40,bd=1,relief="solid")
    values()
    carpark.pack()
    
buttons = Canvas(root,width=600,height=20)
buttonvalue()
update = Canvas(root,width=600,height=45)
console()
bottom()

mainloop()
