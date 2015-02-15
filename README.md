# parkingspaceManager
tkinter app to display parkingspaces in Nottingham, UK

This project is part of a coursework in Introduction to Programming and Software Development (G64IPD) at 
the University of Nottingham.
It displayes my first experience of coded interface design using tkinter. 
It is a very simple program in general but I enjoyed building it.


How to use the program
-
1. 
Download the zip file from Moodle and unzip all files (coursework2.py and readme.txt).
2. Open the program Idle 2.7 from your program list. 
3. Click on File > Open within Idle and navigate to the place you have saved the files. 
4. You should then open “coursework2.py”. 
5. To run the program, click on Run > Run Module or press the F5-key. The program will start to run in the Python Shell.


Functionalities
-
- The program displays status information of 25 carparks in Nottingham
- The top of the program shows cumulated status information of all carparks: 
	- total spaces filled
	- total spaces available
	- total percentage of filled spaces
- The number of carparks with specific statuses:
	“Spaces”
	”Almost Full”
	”Full”
	“Faulty” 

- Information for specific carparks where 5 carparks are shown at once
- For each carpark following information are shown: 
	- the name
	- the number of spaces filled and available
	- a bar chart showing the percentage of filled spaces
	- the date when the data has been updated the last is shown. 
- The colour of the bar chart for each carpark varies with the status of the carpark. 
- The colour will be green for the status “Spaces”,yellow for “Almost Full”, red for “Full” and white or no 
  colour for “Faulty”
- Two buttons that let the user navigate through the carparks 
- A number between the navigation buttons indicates the index of the pages and changes when the buttons are clicked

An “update” button let’s the user update the information displayed with the recent version from the website
- Next to the "update" button, the time of the last update is shown. Whenever the update button is clicked, the time will get 
  updated too.

- Three more buttons let the user to run several options on the list of the carparks. The user can either show the carparks 
  in an alphabetical order or 
sort the carparks by the occupancy, either descending or ascending. When sorted alphabetically 
for example, the carparks starting with the earliest letter in the alphabet will be displayed 
first. When the button “show fullest” is pressed, the fullest carpark will be presented first.

On the bottom of the program, a label informs the user, that the imported data is licensed under 
the Open Government License.


How the code works
-
- The program downloads a comma separated values (csv) file from the website of Nottingham Travel 
  Wise and stores the values into a list. The modules urllib2 and csv are used for this purpose. 
- The file contains information about 25 carparks in Nottingham.
- By referring to certain strings inside the list, certain values can be used for calculation or display.

The GUI elements of the program are created using the Tk inter module. 
- Overview window, carparks and the button console are created as a canvas. 
- By defining the absolute position on the canvases information like text, rectangle or strings are displayed on them.
 
- The creation of the canvases for the carparks, the overview window and the button console are separated from the values 
  like text or buttons. 
- The values are stored in functions. This way it is possible to update the content of the values without deleting 
  the actual canvas objects. Only the values will be deleted and recreated by calling the functions 
  again. 
- The five canvases for the carparks are created by running a for loop. 
  At the same time the canvas object gets appended to an empty list. The values function which only contains the text presented on 
the canvas is also running a for loop that loops through global variables. The text values refer to a 
particular position in the list where the carpark canvases had been appended to. With every loop the 
position in the list increases by one.The variables of the for loop change whenever the user clicks the 
navigation buttons. This way every click on the navigation button shows the next or previous five 
carparks.
The bar charts for the carparks is created with a rectangle on the canvases. The colour of the 
bar charts get controlled by a condition that checks which status is given for particular rows in the data 
list. For each status the rectangle gets a particular colour.
Clicking one of the four buttons will first 
delete all values (texts) presented on the carparks canvases using a for loop that loops through the length 
of the data list. Then a particular change to variables is made and the functions containing modified 
elements (overview, carparks or update time) get loaded again.
Whenever the user clicks the update button, 
the data list will be copied to a different variable called olddata and a new version of the csv file gets 
saved to the data list. By subtracting the strings for the percentage of the old data from the new data the 
change in percentage gets calculated and can be displayed on the canvases.
The current time next to the update button gets shown using the time module.

