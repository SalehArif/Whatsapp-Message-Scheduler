from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pywhatkit
import tkinter.messagebox

class gui:
    def __init__(self):
        window = Tk()
        window.title("Whatup Scheduler")
        window.resizable(False, False)
        canvas1 = Canvas(window, width = 400, height = 300)
        canvas1.pack(fill = "both", expand= True)

        img1 = Image.open("bg.jpg")

        photoimg =  ImageTk.PhotoImage(img1)
        canvas1.create_image( 0, 0, image = photoimg, anchor = "nw") 


        # width = 100
        # height = 100
        img = Image.open("resized icon.png")
        photoImg =  ImageTk.PhotoImage(img)
        canvas1.create_image(200,40, image=photoImg)

        canvas1.create_text( 90, 120, text = "Phone Number", fill="white", font="Roboto 10")
        canvas1.create_text( 100, 160, text = "Message", fill="white", font="Roboto 10") 
        canvas1.create_text( 100, 200, text = "Time", fill="white", font="Roboto 10") 
        canvas1.create_text( 195, 200, text = ":", font= "Arial 16 bold") 

        self.entry = Entry(window)
        canvas1.create_window(200,120,window=self.entry)

        self.entry1 = Entry(window)
        canvas1.create_window(200,160,window=self.entry1)
        
        hours = [x for x in range(24)]
        mins = [x for x in range(60)]

        self.variable = StringVar(window)
        hour = ttk.Combobox(window, width = 2, textvariable = self.variable)
        hour['values'] = hours
        canvas1.create_window(170,200,window=hour)
        hour.current()

        self.variable1 = StringVar(window)
        min = ttk.Combobox(window, width = 2, textvariable = self.variable1)
        min['values'] = mins
        canvas1.create_window(220,200,window=min)
        min.current()

        bt = Button(window,text="Schedule Msg",fg="#333", font="Roboto 10",command=self.gettext)
        canvas1.create_window(200,250,window=bt)


        # self.entry.pack()
        # bt.pack()
        self.warning()
        window.mainloop()

    def gettext(self):
        text = []
        text.append(self.entry.get())
        text.append(self.entry1.get())
        text.append(self.variable.get())
        text.append(self.variable1.get())
        
        self.show(text[0])
        self.schedule(text)


    def schedule(self, text):
        hour = int(text[2])
        min = int(text[3])
        pywhatkit.sendwhatmsg(text[0],text[1],hour,min,wait_time=15)
        show(text[0])

    def show(self, num):
        # tkinter.messagebox.showinfo("showwarning", "This is a warning")
        msg = "Your Text is scheduled to be sent to "+num+" in 15 seconds after Whatsapp loads."
        tkinter.messagebox.showinfo("Succesfull",msg)
    def warning(self):
        tkinter.messagebox.showinfo("Disclaimer","Sign in your Whatsapp Web on your default browser before scheduling a message.")

gui()
# pywhatkit.sendwhatmsg('+923341272207','meep morp, I\'m a bot again.',21,50)
