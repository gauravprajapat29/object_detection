import cv2
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import filedialog as fd
import pickle

def ml_work(filename,x):
    new_img = cv2.imread(filename)
    new_img = cv2.resize(new_img,(150,200))
    new_img = new_img.flatten()
    p = open("obj.txt","rb")
    model = pickle.load(p)
    ar = model.predict([new_img])
    l = ['computer mouse', 'neckband headset', 'smart watch']
    name_obj = l[int(ar[0])]
    if x == 1:
        obj_l.config(text=name_obj)
    elif x==2:
        obj_c.config(text=name_obj)









cancel = False

def prompt_ok(event = 0):
    global cancel, button, button1, button2
    cancel = True

    button.place_forget()
    button1 = Button(cam, text="Good Image!", command=saveAndExit)
    button1.place(anchor=CENTER, relx=0.2, rely=0.9, width=150, height=50)
    button2 = Button(cam, text="Try Again", command=resume)
    button2.place(anchor=CENTER, relx=0.8, rely=0.9, width=150, height=50)
    button1.focus()

def saveAndExit(event = 0):
    global img,lmain

    filepath = "imageCap.png"
    img.save(filepath)
    lmain.focus()
    ml_work(filepath, 2)

def resume(event = 0):
    global button1, button2, button, lmain, cancel

    cancel = False

    button1.place_forget()
    button2.place_forget()

    button.place(bordermode=INSIDE, relx=0.5, rely=0.9, anchor=CENTER, width=300, height=50)
    lmain.after(10, video_stream)

def video_stream():
        global img
        _, frame = cap.read()
        frame = cv2.flip(frame,1)
        frame = cv2.resize(frame,(600,500))
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        if not cancel:
            lmain.after(10, video_stream)


def open_camera():
    global cap,lmain,cam,button
    cam = Toplevel()
    cam.resizable(width=False, height=False)
    cap = cv2.VideoCapture(0)
    capWidth = cap.get(3)
    capHeight = cap.get(4)

    lmain = Label(cam, compound=CENTER, anchor=CENTER, relief=RAISED)
    lmain.pack()

    button = Button(cam, text="Capture", command=prompt_ok)
    button.place(bordermode=INSIDE, relx=0.5, rely=0.9, anchor=CENTER, width=300, height=50)
    button.focus()

    video_stream()

    cam.mainloop()


def local_com():
        filetypes = (('image jpg files', '*.jpg'),('png files', '*.png'))
        filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        ml_work(filename,1)






win = Tk()
win.geometry("1020x500")
win.resizable(False,False)
win.title("Object Classification")
win.config(bg = "yellow")



Label(win,text="Local Computer Drive",font = ("Time New Roman",30,"bold"),bg = "yellow").place(x=50,y=70,height=60,width=410)

local = Button(win,text = "Open Folder",font = ("Time New Roman",20,"bold"),command=local_com)
local.place(x=150,y=180,height=60,width=200)

canvas = Canvas(win, width=5, height=win.winfo_screenheight(), bg='yellow',borderwidth=0)
canvas.place(x = 510,y=0)
canvas.create_line((5, 0), (5, win.winfo_screenheight()), width=5, fill='gray')

Label(win,text="Object Name : ",font = ("Time New Roman",30,"bold"),bg = "yellow").place(x=50,y=290,height=60,width=410)

obj_l = Label(win,text="",font = ("Time New Roman",30,"bold"))
obj_l.place(x=50,y=370,height=60,width=410)


Label(win,text="Open Camera",font = ("Time New Roman",30,"bold"),bg = "yellow").place(x=560,y=70,height=60,width=410)

cam1 = Button(win,text = "Open Camera",font = ("Time New Roman",20,"bold"),command=open_camera)
cam1.place(x=660,y=180,height=60,width=200)

Label(win,text="Object Name : ",font = ("Time New Roman",30,"bold"),bg = "yellow").place(x=560,y=290,height=60,width=410)

obj_c = Label(win,text="",font = ("Time New Roman",30,"bold"))
obj_c.place(x=560,y=370,height=60,width=410)

win.mainloop()