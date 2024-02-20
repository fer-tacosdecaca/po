from tkinter import*
import random

ad = Tk()
ad.title("Trata de ver esto")
ad.geometry("400x400")

ñabel = Label(ad)
ñabel.place(relx=0.5, rely=0.5, anchor=CENTER)

def randomlisto():
    ran_list = random.sample(range(0,101),1)
    prize = random.sample(range(0,101),1)
    print(ran_list)
    print(prize)
    if(ran_list == prize):
        ñabel["text"]="ganaste"
    

    
btn = Button(ad, text="ga",command=randomlisto )
btn.place(relx=0.4, rely=0.5, anchor=CENTER)


ad.mainloop()