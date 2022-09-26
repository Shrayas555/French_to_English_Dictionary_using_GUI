
from tkinter import *
import random
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
currentcard={}
newdict={}
try:
    data=pd.read_csv('/Users/shrayasraju/Downloads/flash-card-project-start/data/words to learn.csv')
except FileNotFoundError:
    original=pd.read_csv('/Users/shrayasraju/Downloads/flash-card-project-start/data/french_words.csv')
    newdict=original.to_dict(orient='records')
else:
    newdict=data.to_dict(orient='records')


def buttonpressed():
    global currentcard,fliptimer
    window.after_cancel(fliptimer)
    currentcard=random.choice(newdict)
    canvas.itemconfig(b, text='French', font=('Ariel', 40, 'italic'), fill='black')
    canvas.itemconfig(a,text=f"{currentcard['French']}",fill='black')
    canvas.itemconfig(back, image=image1)
    fliptimer=window.after(3000, func=flipcard)
def flipcard():
    global  currentcard

    canvas.itemconfig(b,text='English',font=('Ariel',40,'italic'),fill='white')
    canvas.itemconfig(a,text=f"{currentcard['English']}",fill='white' )
    canvas.itemconfig(back,image=image4)

def right():
    newdict.remove(currentcard)
    print(len(newdict))
    data=pd.DataFrame(newdict)
    data.to_csv('/Users/shrayasraju/Downloads/flash-card-project-start/data/words to learn.csv',index=False)
    buttonpressed()





window=Tk()
window.config(padx=50,pady=50,bg="#B1DDC6",highlightthickness=0)
fliptimer=window.after(3000,func=flipcard)

window.title('Flash cards')
image1=PhotoImage(file='/Users/shrayasraju/Downloads/flash-card-project-start/images/card_front.png')

canvas=Canvas(height=526,width=800,highlightthickness=0)
back=canvas.create_image(400,263,image=image1)
b=canvas.create_text(400,150,text='French',font=('Ariel',40,'italic'),fill='black')
a=canvas.create_text(400,263,text='word',font=('Ariel',60,'bold'),fill='black')
canvas.config(bg='#B1DDC6',highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

image2=PhotoImage(file='/Users/shrayasraju/Downloads/flash-card-project-start/images/wrong.png')

button1=Button(image=image2,highlightthickness=0,bg=BACKGROUND_COLOR,command=buttonpressed)
button1.grid(row=1,column=0)

image3=PhotoImage(file='/Users/shrayasraju/Downloads/flash-card-project-start/images/right.png')
image4=PhotoImage(file='/Users/shrayasraju/Downloads/flash-card-project-start/images/card_back.png')
button2=Button(image=image3,highlightthickness=0,bg=BACKGROUND_COLOR,command=right)
button2.grid(row=1,column=1)




buttonpressed()

















window.mainloop()

