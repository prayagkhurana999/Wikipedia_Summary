#main aggenda
#that we will write anything and will get 10 lines from wikipedia and save to our pc as filter
#form anaconda install wikipedia package
from tkinter import *
import wikipedia
import os
from tkinter import messagebox
#summary takes two argumet 1.word to search and 2. lines needed
# summary inbulit method in wikipedia and help to search something from wiki
#data=wikipedia.summary("python prograaming",10)  
#we want to store data in file and save for that withopen()
withopen("search_result.txt","w") as file: #there is no file with this anme it will make file and write  make file  as search..
    file.write(data)
os.system("search_result.txt") #it will open file    

master.Tk()
master.title("Wiki searcher")
label1=label(master,text="wikipedia search",font=("arial",16,"black")).grid(row=0,coloumn=0)
label2=label(master,text="Enter to search",font=("arial",12,"black")).grid(row=1,coloumn=0)
thing=Entry(master)
button1=button(master,text="searchnSave",ipadx=15,ipady=8,command=search.grid(row=3,coloumn=0,columnspan=2)
button2=button(master,text="open",ipadx=15,ipady=8,command=Open).grid(row=4,coloumn=0,columnspan=2)
thing.grid(row=2,coloumn=0,ipadx=20,ipady=10)
master.mainloop()

def search():
    data=wikipedia.summary(thing.get(),10)
    withopen("search_result.txt","w") as file: #there is no file with this anme it will make file and write  make file  as search..
        file.write(data)
    messagebox.showinfo("searched and save successsfully press open!!!")    
    
def Open():
    os.system("search_result.txt") #it will open file

