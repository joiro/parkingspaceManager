from Tkinter import *
from urllib2 import *
import csv

url = "http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642"
webpage = urlopen(url)
datareader = csv.reader(webpage.read().decode('utf-8').splitlines())
data = list(datareader)

string_var_list=[]
start_offset=1

def carpark():
    for num in range(1,6):
        this_label=StringVar()
        Label(root, textvariable=this_label,
              width=75,height=3,bd=1,relief="solid").grid(row=num,column=0,padx=7,pady=1)
        string_var_list.append(this_label)

def Overview():
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
    can = Canvas(root,width=610,height=60,bg="grey")
    can.create_text(5,12,anchor="w",text="Overview",font=(None,"13","bold"))
    can.create_text(5,30,anchor="w",text="Spaces filled: "+str(a))
    can.create_text(300,30,text="Spaces Available: "+str(b-a))
    can.create_text(460,30,anchor="w",text="Percentage Filled: "+str(t)+"%")
    can.create_text(300,50,text="Statuses: Spaces: "+str(status("Spaces"))+", Almost Full: "+str(status("Almost"))+", Full: "+str(status(" Full"))+", Faulty: "+str(status("Faulty")))
    can.grid(row=0,column=0)
    title = Label(root,text="Car Parks",font=(None,"13","bold")).grid(row=1,column=0)

def change():
    for num in range(5):
        ## set new contents if there are any
        new_text=""
        offset=start_offset+num
        if offset >=0 and offset < len(data):
            new_text="Name"+data[offset][3]+" "+data[offset][-6]+" of"+data[offset][1]

        string_var_list[num].set(new_text)

def next():
    global start_offset
    start_offset += 5
    if start_offset > 21:
        start_offset=21
    change()

def previous():
    global start_offset
    start_offset -= 5
    if start_offset < 1:
        start_offset=1
    change()

def bottom():
    bottom = Canvas(root,width=600,height=75)
    button1 = Button(root,text="<",command=previous)
    bottom.create_window(160,15,window=button1)
    button2 = Button(root,text=">",command=next)
    bottom.create_window(420,15,window=button2)
    bottom.create_text(300,15,text=str(start_offset)+"-"+str(5)+"/"+str(len(data)-1))
    button3 = Button(root,text="Update")
    button4 = Button(root,text="Show Alphabetical")
    button5 = Button(root,text="Show Emptiest")
    button6 = Button(root,text="Show Fullest")
    bottom.create_text(300,40,text="Last update: "+data[1][-1][12:17])
    bottom.create_window(160,40,window=button3)
    bottom.create_window(160,65,window=button4)
    bottom.create_window(300,65,window=button5)
    bottom.create_window(420,65,window=button6)
    bottom.grid(row=10,column=0)
    Source = Label(text="Contains Public Sector Information licensed under the Open Government License v1.0.").grid(row=11,column=0)    

root = Tk()
Overview()
carpark()
bottom()

mainloop()
