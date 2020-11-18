#------------------------------------------
#Joes_music_player ver 0.2 18:32 12/06/2020
#------------------------------------------

#ok so for libraries I just pulled this old code out of my collection of fails as it demostates the tkinter libary
#its still a canseld project though and usless at that
#if I was to redo it there would be some improvements to make it look better
#maybe I will do that later (all I have added are new comments as some of the old ones were rubbish)



#imports
from tkinter import *                           #imports the libary tkinter
import tkinter as tk                            #imports the libary tkinter as tk

#Lists
songs = []                                      #sets up songs as a list

#music
current = ("music/76.mp3")                      #test music

#variables 
end = 0
songnum = 0
choice = 0                                      

#window data
mainWindow = tk.Tk()                            #sets up tkinter
mainWindow.title("Joes_music_player")           #window name
mainWindow.geometry("300x100")                  #window size
mainWindow.config(bg="black")                   #window colour
#music play back data
    
#main loop

#controls
play = Button(mainWindow, text = ">")           #makes a button and puts '>' on it 
play.place(x=40, y=60)                          # X and Y of button

palse = Button(mainWindow, text = "||")         #makes a button and puts '||' on 
palse.place(x=60, y=60)                         # X and Y of button
    
rewind = Button(mainWindow, text = "<<")        #makes a button and puts '<<' on 
rewind.place(x=78, y=60)                        # X and Y of button

forward = Button(mainWindow, text = ">>")       #makes a button and puts '>>' on 
forward.place(x=106, y=60)                      # X and Y of button

skip = Button(mainWindow, text = ">|")          #makes a button and puts '>|' on 
skip.place(x=134, y=60)                         # X and Y of button

back = Button(mainWindow, text = "|<")          #makes a button and puts '|<' on 
back.place(x=157, y=60)                         # X and Y of button

#def play():                                     
#    print("test")


mainWindow.mainloop()                           #go back to the main loop
print("test")                                   #error check - left over from error testing to test when the loop breaks
