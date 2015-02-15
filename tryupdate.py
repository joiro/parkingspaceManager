from Tkinter import *
from urllib2 import *
import csv

url = "http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642"
webpage = urlopen(url)
datareader = csv.reader(webpage.read().decode('utf-8').splitlines())
data = list(datareader)

root = Tk()
old = 0
new = 0
def carpark():
    global old
    global new
    for i in range(1,len(data)):
        old += int(data[i][-6])
    for i in range(1,len(data)):
        new += int(data[i][-6])
    Can = Canvas(width=600,height=400)
    Can.create_text(300,100,text="new: "+str(new))
    Can.create_text(300,300,text="old: "+str(old))
    Can.pack()
    
def update():
    global data
    global olddata
    olddata = list(data)
    url = "http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642"
    webpage = urlopen(url)
    datareader = csv.reader(webpage.read().decode('utf-8').splitlines())
    data = list(datareader)
    print data[1][-1][12:17]

carpark()
button1 = Button(root,text="Update",command=update).pack()

mainloop()
