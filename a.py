from tkinter import*
import random



a = Tk()
a.geometry("1000x1001")
a.title("esto no es un cuadrado perfecto")

ñabel = Label(a)
ñabel.place(relx=0.5, rely=0.5, anchor=CENTER)
ñabel2 = Label(a)
ñabel2.place(relx=0.5, rely=0.7, anchor=CENTER)

list = ["uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","pppppppppppppppppppp                                       ppppppppppppppppppppppppppppppppppppppppppppp"]
print(list)



def randomlisto():
    random_no = random.randint(0,2)
    if(random_no == 0):
        ñabel["text"]="salio 1"
        g=list[random_no]
    if(random_no == 1):
        ñabel["text"]="salio 2"
        g=list[random_no]
    if(random_no == 2):
        g=list[random_no]
        ñabel["text"]="salio 3"
        ñabel2["text"]=g
        
btn = Button(a, text="ga",command=randomlisto )
btn.place(relx=0.5, rely=0.7, anchor=CENTER)

a.mainloop()
