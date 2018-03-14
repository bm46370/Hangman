from random import randint
from tkinter import*

def exit(event):
    Hangman.destroy()
    
def play(event):
    global init
    global word
    print (word)
    if(e1.get() in word):
        global countGood
        global countGoodMax
        x=0
        for i in word:
            if i==e1.get():
                listHiddenCharacters[x]=e1.get()
                countGood=countGood+1
            x = x + 1
            msg1.config(text=listHiddenCharacters)
        if countGood==countGoodMax:
            msg4.config(text='Eureka! YOU WIN!')
    else:
        global countBad
        listOfFails.extend(e1.get() + '|')
        msg3.config(text=listOfFails)
        if countBad==0:
            img2=PhotoImage(file="picture1.png")
            init.configure(image=img2)
            init.image = img2
        elif countBad == 1:
            img2 = PhotoImage(file="picture2.png")
            init.configure(image=img2)
            init.image = img2
        elif countBad == 2:
            img2 = PhotoImage(file="picture3.png")
            init.configure(image=img2)
            init.image = img2
        elif countBad == 3:
            img2 = PhotoImage(file="picture4.png")
            init.configure(image=img2)
            init.image = img2
        elif countBad == 4:
            img2 = PhotoImage(file="picture5.png")
            init.configure(image=img2)
            init.image = img2
        elif countBad == 5:
            img2 = PhotoImage(file="picture6.png")
            init.configure(image=img2)
            init.image = img2
        else:
            img2 = PhotoImage(file="picture7.png")
            init.configure(image=img2)
            init.image = img2
            msg4.config(text='More luck next time. YOU LOSE!')
        countBad= countBad + 1
    e1.delete(0, 'end')

def again(event):
    global init
    global countGood
    global countBad
    global countGoodMax
    global word
    global words
    global listOfFails
    global listHiddenCharacters

    word = words[randint(0, len(words) - 1)]

    countBad = 0
    countGood = 0
    countGoodMax = len(word) - 1

    img2 = PhotoImage(file="picture0.png")
    init.configure(image=img2)
    init.image = img2

    e1.delete(0, 'end')

    listHiddenCharacters.clear()
    listHiddenCharacters = ['_'] * (len(word) - 1)
    msg1.config(text=listHiddenCharacters)

    listOfFails.clear()
    listOfFails = []
    msg3.config(text=listOfFails)

    msg4.config(text='')


if __name__ == "__main__":
    text_file = open("words.txt", "r")
    words = text_file.readlines()
    text_file.close()
    word = words[randint(0, len(words) - 1)]

    countBad = 0
    countGood = 0
    countGoodMax = len(word) - 1

    Hangman=Tk()
    Hangman.title("Hangman")
    Hangman.resizable(False,False)

    img_init=PhotoImage(file="picture0.png")
    init=Label(Hangman,image=img_init)
    init.pack()

    msg=Label(Hangman, text="Write a character and then press PLAY:")
    msg.config(font=('times', 13))
    msg.place(x=500,y=150)

    e1 = Entry(Hangman)
    e1.config(font=('times', 20))
    e1.place(x=500,y=200)

    listHiddenCharacters= ['_']*(len(word) - 1)
    msg1=Label(Hangman, text=listHiddenCharacters)
    msg1.config(font=('times', 20))
    msg1.place(x=500,y=275)

    pulsante_gioco=Button(Hangman,text="GUESS")
    pulsante_gioco.config(bg="green",font=("Ariel",18))
    pulsante_gioco.place(x=500,y=350)
    pulsante_gioco.bind("<Button>",play)

    pulsante_esci=Button(Hangman,text="PLAY AGAIN")
    pulsante_esci.config(bg="pink",font=("Ariel",18))
    pulsante_esci.place(x=625,y=350)
    pulsante_esci.bind("<Button>",again)

    pulsante_esci=Button(Hangman,text="EXIT")
    pulsante_esci.config(bg="aqua",font=("Ariel",18))
    pulsante_esci.place(x=805,y=350)
    pulsante_esci.bind("<Button>",exit)

    msg2=Label(Hangman, text="List of wrong guesses:")
    msg2.config(font=('times', 10))
    msg2.place(x=500,y=425)

    listOfFails=[]
    msg3=Label(Hangman, text=listOfFails)
    msg3.config(font=('times', 14))
    msg3.place(x=500,y=450)

    msg4=Label(Hangman, text='')
    msg4.config(font=('times', 25))
    msg4.place(x=500,y=525)

    Hangman.mainloop()