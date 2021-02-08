import tkinter
from tkinter import Label, Entry, Button, StringVar, END
import random
from tkinter import messagebox
from random import shuffle
answer = ['car', 'youtube', 'spotify', 'download', 'mobile', 'phone', 'laptop', 'computer', 'case', 'keyboard', 'print', 'tablet', 'fax', 'monitor', 'motherboard', 'cpu', 'gpu', 'power', 'fan', 'lamp', 'microphone', 'windows', 'linux', 'ubuntu', 'debian', 'android', 'blackberry', 'sofa', 'table', 'bed', 'mouse', 'asus', 'samsung', 'nokia', 'lg', 'motorola', 'apacer', 'acer', 'intel', 'amd', 'nvidia', 'genius', 'tesla', 'mercedes-benz', 'volkswagon', 'bmw', 'mitsubishi', 'toyota', 'honda', 'hyundai', 'ford', 'nissan', 'renault', 'peugeot', 'xantia', 'chevorlet', 'dodge', 'mack', 'porsche', 'audi', 'hard', 'hardware', 'software', 'lamborghini', 'bugatti', 'ferrari', 'maserati', 'bentley', 'morgan', 'linkedin', 'facebook', 'instagram', 'whatsapp', 'telegram', 'snappcaht', 'viber', 'sms', 'call', 'pencil', 'book', 'mug', 'digital', 'bicycle', 'banana', 'apple', 'grape', 'lemon', 'orange', 'kiwi', 'python', 'java', 'golang', 'microsoft', 'xbox', 'skype', 'sky', 'cloud', 'sun', 'weather', 'airplane', 'bus', 'truck', 'finance', 'atom', 'lego', 'iran', 'usa', 'uk', 'germany', 'denmark', 'poland', 'switzerland', 'portugal', 'mongolia', 'jordan', 'saudi arabia', 'uae', 'afghanistan', 'turkmenistan', 'turkey', 'tajikistan', 'iraq', 'russia', 'georgia', 'azerbaijan', 'namibia', 'virtualbox', 'tehran', 'baku', 'washington', 'virginia', 'texas', 'nevada', 'california', 'florida', 'detroit', 'alaska', 'hawaii', 'brazil', 'colombia', 'argentina', 'mexico', 'peru', 'chile', 'venezuela', 'bogota', 'india', 'china', 'canada', 'spain', 'morocco', 'egypt', 'south africa', 'cairo', 'istanbul', 'toronto', 'vancouver', 'rwanda', 'uganda', 'singapore', 'vietnam', 'thailand', 'philippines', 'japan', 'taiwan', 'shanghai', 'ireland', 'dublin', 'iceland', 'netherlands', 'amsterdam', 'tbilisi', 'colorado', 'oman', 'yemen', 'pig', 'horse', 'chicken', 'duck', 'cow', 'sheep', 'wolf', 'koala', 'house', 'doctor', 'lion', 'goose', 'crows', 'chough', 'columbidae', 'owl', 'cat', 'dog', 'bat', 'snake', 'cheese', 'cheetah', 'firefox', 'tea', 'cofee', 'nescafe', 'cappuccino', 'skoda', 'donkey', 'mule', 'zebra', 'giraffe', 'adena', 'tomato', 'potato']
words = []
for i in answer:
    word = list(i)
    shuffle(word)
    words.append(word)
num = random.randint(0, len(words))
def initial():
    global words, num, answer
    label1.configure(text = words[num])
def answer_check():
    global num, words, answer
    user_input = entry1.get()
    if user_input == answer[num]:
        messagebox.showinfo('Yes', 'Good job')
        Reset()
    else:
        messagebox.showinfo('No', 'Try again')
        entry1.delete(0, END)
def Reset():
    global words, num, answer
    num = random.randint(0, len(words))
    label1.configure(text = words[num])
    entry1.delete(0, END)
root = tkinter.Tk()
root.geometry('300x300')
label1 = Label(root, font = 'times 20')
label1.pack(pady = 30, ipady = 10, ipadx = 10)
answers = StringVar()
entry1 = Entry(root, textvariable = answers)
entry1.pack(ipady = 5, ipadx = 5)
button1 = Button(root, text = 'Check', width = 20, command = answer_check)
button1.pack(pady = 40)
button2 = Button(root, text = 'Reset', width = 20, command = Reset)
button2.pack()
initial()
root.mainloop()
