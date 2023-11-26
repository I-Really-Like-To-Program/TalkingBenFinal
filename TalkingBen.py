import os
import random
from PIL import ImageTk, Image  
from playsound import playsound
import tkinter as tk
root = tk.Tk()
root.geometry("720x480")

path = "Random Projects"
os.chdir(path)
path = "Talking Ben"
os.chdir(path)

def Yes():
    num = random.randint(1,7)
    if num == 1:
        sound = str("Ben.mp3")
        playsound(sound)
    if num == 2:
        sound = str("Burp-04.mp3")
        playsound(sound)
    if num == 3:
        sound = str("hohoho.mp3")
        playsound(sound)
    if num == 4:
        sound = str("Nananana.mp3")
        playsound(sound)
    if num == 5:
        sound = str("No.mp3")
        playsound(sound)
    if num == 6:
        sound = str("Uhh.mp3")
        playsound(sound)
    if num == 7:
        sound = str("Yes.mp3")
        playsound(sound)

#Creating Objects
lblBenQuestion = tk.Label(root,text="Ask a question for Ben")
entBenQuestion = tk.Entry(root)
btnBenQuestion = tk.Button(root,text="Yes???",command=Yes)
image = Image.open("ZRFp3K.png")
photo = ImageTk.PhotoImage(image)

#Placing Objects
label = tk.Label(root, image=photo)
label.pack()
lblBenQuestion.pack()
entBenQuestion.pack()
btnBenQuestion.pack()


root.mainloop()