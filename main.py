import tkinter as tk
import random
#from tkinter.tix import COLUMN

guessNum = 0

def getWorld():
    
    correct = 0
    global guessNum

    guessWorld = EntryBox.get()
    print("Arvatud sona on:",guessWorld)
    
    if guessWorld in wordlist:
        for i in range(5):
            label = tk.Label(text = guessWorld[i].upper(),font = 12,pady = 5,borderwidth = 1, relief="solid")
            label.grid(row = guessNum, column = i, sticky= tk.NSEW)# sticky соединяет в решетку буквы
            
            if guessWorld[i] in chosenWorld:
                if guessWorld[i] == chosenWorld[i]:
                   label.config(bg = 'green') #буквы входят в верное слово и на верном месте
                   label.config(fg = 'white')
                   correct = correct + 1
                else:
                   label.config(bg = 'gold') #буквы входят в верное слово , но не на верном месте
                   label.config(fg = 'white')
            
                   

            else:
                label.config(bg = 'grey') #буквы не входят в верное слово
                label.config(fg = 'white')
                
        if correct == 5:
            GuessButton.config(state = 'disabled')
            Resultlabel.configure(text = 'Olete võitnud!',bg = 'black',fg = 'green')
        elif guessNum == 5:
            GuessButton.config(state = 'disabled')
            Resultlabel.configure(text = 'Kaotasite, proovige uue mängu!',bg = 'black',fg = 'white')
        else:
            guessNum += 1
            

    else:
      print("Vale sõna , proovige veel kord!")
       
    
f = open("sonad2.txt")
sonad2 = f.read()
f.close()

wordlist = sonad2.split('\n')

chosenWorld = random.choice(wordlist) # случайно вытаскивает слово их списка.
print(chosenWorld)

window = tk.Tk()
window.title("Wordle")
window.geometry("300x300")
window.config(bg='black')

EntryBox = tk.Entry()
EntryBox.grid(row = 99, column = 0, columnspan = 5 )
GuessButton = tk.Button(text = "OK!", command = getWorld,bg = 'black',fg = 'white')
GuessButton.grid(row = 100, column = 0, columnspan = 5)

Resultlabel = tk.Label(text = '',bg = 'black',fg = 'white')
Resultlabel.grid(row = 101, column = 0, columnspan = 5)

Userlabel = tk.Label(text = 'Kasutage sõnad "sonad2.txt" nimerkirjast!',bg = 'black',fg = 'white')
Userlabel.grid(row = 102, column = 0, columnspan = 5)


tk.mainloop()