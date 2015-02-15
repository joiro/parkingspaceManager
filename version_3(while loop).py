from Tkinter import *
import urllib2
import csv

# load the csv file from the webpage and transform into list
csvfile = urllib2.urlopen("http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642")
datareader = csv.reader(csvfile.read().decode('utf-8').splitlines())
data = list(datareader)
olddata = list(data)

root = Tk()

'''
def change():
    global car,x
    x = x + 5
    car.delete(ALL)
    display()
'''
def change():
    global x
    a = 5
    print a
    x = x + 5
    i = 1
    display()

def display():
    global i,x
    if a == 5:
        print a
        car.delete(ALL)
    while i <= 5:
        car = Canvas(root,width=400,height=40)
        car.create_text(200,20,text=data[x][3])
        car.grid(row=i,column=0)
        i = i + 1
        x = x + 1


i = 1
x = 1
a = 0
display()

Button1 = Button(root,text="Change",command=change)
Button1.grid(row=7,column=0)

mainloop()
