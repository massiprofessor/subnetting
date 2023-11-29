import tkinter as tk
from  tkinter import ttk
from tkinter import *
from tkinter.simpledialog import askstring
import re
import sys
import ipaddress
from PIL import Image, ImageTk
from base64 import b64decode

import os
window = tk.Tk()
window.geometry("500x400")
window.title("Subnet Calculator 1.0 - Massimo Mezzina")
window.configure(background="white")
window.resizable(False,False)
directory=os.getcwd()



img64=b'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'
b'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'

pic_bytes = b64decode(img64)  
image1 = ImageTk.BytesIO(pic_bytes) 


pil_photo = Image.open(image1)  
test = ImageTk.PhotoImage(pil_photo)
label1 = tk.Label(image=test)
label1.image = test
# Position image
label1.place(x=375, y=2)

reti={}
val=[]


def change():
    global calcol
    calcol= ttk.Button(window, text="Calcola", command= calcola, state="enabled")
    calcol.grid(row=3, column=1, sticky= W, padx=5, pady=5)

def clear():
    global reti
    global val
    global row
    global rigahost_label
    global rigarete
    global cidr
    global nm
    global maschere
    for label in window.winfo_children():
        if type(label) == Label :
            label.destroy()
    text_ind.delete(0, END)
    text_nret.delete(0, END)
    ind_label = Label(window, text = " Inserisci indirizzo di partenza", font=40)
    ind_label.grid(row = 0, column = 0, sticky = W, pady = 2, padx= 5)
    nret_label = Label(window, text = " Inserisci Numero di reti", font=40)
    nret_label.grid(row = 1, column = 0, sticky = W, pady = 2, padx= 5)
    global calcol
    calcol= ttk.Button(window, text="Calcola", command= calcola, state="disabled")
    calcol.grid(row=3, column=1, sticky= W, padx=5, pady=5)
    reti={}
    val=[]
    row=3
    cidr=0
    nm=[]
    maschere=[]
    pil_photo = Image.open(image1)  
    test = ImageTk.PhotoImage(pil_photo)
    label1 = tk.Label(image=test)
    label1.image = test
    # Position image
    label1.place(x=375, y=2)
    
def calcolasub(numero_host):
    bithost=0
    while (2 ** bithost - 2) < numero_host:
        bithost += 1
    return bithost

def inserisci_host():
    try:
        change()
        global row
        row=3
    
        nreti= int(text_nret.get())
        if nreti != "":
        
            for i in range(1,nreti+1):
            

                text_host = int(askstring("Inserisci il numero di Host","Inserisci il numero di Host: ",parent=window))
                val.append(text_host)
            val.sort(reverse=True)
            h=1
            for valore in val:
                global rigahost_label
                rigahost_label = Label(window, text = "RETE " + str(h) + " con " + str(valore) + " Host: ", font=40)
                rigahost_label.grid(row = row + h, column = 0, sticky = W, pady = 2, padx= 5)
                h=h+1
            i=1
            for elem in val:
                reti.update({i:[[],elem]})
                i=i+1
        clear()
    except TypeError:
        print("Errore")
    except ValueError:
        print("Errore")
        

    

def calcola():
        try:
            indirizzop= text_ind.get()
            indirizzop=re.findall(r"[\d']+", indirizzop)
            global indirizzor
            global cidr
            global nm
            indirizzor=indirizzop[:4]
            cidr=indirizzop[-1]
            print(reti)
            nm=[]
            maschere=[]
            for elem in reti:
                bithost=calcolasub(int(reti[elem][1]))
                maschera=32 - bithost
                numeromagico=2**bithost
                maschere.append(maschera)
                nm.append(numeromagico)
            indirizzo= ".".join(indirizzor)
            smnm=0
            for elem in nm:
                smnm=smnm + elem
            nhostsub= 2**(32-int(cidr)) - 2

    
            if smnm < nhostsub:
                j=0
                for i in range(len(nm)):
                    if i == 0:
                        global rigarete
                        rigarete = Label(window, text = str(indirizzo) + "/" + str(maschere[i]), font=40)
                        rigarete.grid(row = row + i + 1, column = 1, sticky = W, pady = 2, padx= 5)
                        print(indirizzo,maschere[i])

                    else:
                        indirizzo=str(ipaddress.ip_address(indirizzo) + nm[j])
                        rigarete = Label(window, text = str(indirizzo) + "/" + str(maschere[i]), font=40)
                        rigarete.grid(row = row + i +1, column = 1, sticky = W, pady = 2, padx= 5)
                        print(indirizzo,maschere[i])
                        j=j+1
            else:
                for label in window.winfo_children():
                    if type(label) == Label :
                        label.destroy()
                ind_label = Label(window, text = " Inserisci indirizzo di partenza", font=40)
                ind_label.grid(row = 0, column = 0, sticky = W, pady = 2, padx= 5)
                nret_label = Label(window, text = " Inserisci Numero di reti", font=40)
                nret_label.grid(row = 1, column = 0, sticky = W, pady = 2, padx= 5)
                rigarete = Label(window, text ="Il numero di host è troppo grande\nper la sbunet di partenza" , font=40)
                rigarete.grid(row = row + 1, column = 0, sticky = W, pady = 2, padx= 5)
        except IndexError:
            print("Errore")

ind_label = Label(window, text = " Inserisci indirizzo di partenza", font=40)
ind_label.grid(row = 0, column = 0, sticky = W, pady = 2, padx= 5)
text_ind = tk.Entry(window)
text_ind.grid(row=0, column=1, sticky="W", padx=5)
nret_label = Label(window, text = " Inserisci Numero di reti", font=40)
nret_label.grid(row = 1, column = 0, sticky = W, pady = 2, padx= 5)
text_nret = tk.Entry(window)
text_nret.grid(row=1, column=1, sticky="W", padx=5)
calcol= ttk.Button(window, text="Calcola", command= calcola, state="disabled")
calcol.grid(row=3, column=1, sticky= W, padx=5, pady=5)
ins_host= ttk.Button(window, text="Inserisci Host", command= inserisci_host)
ins_host.grid(row=3, column=0, sticky= W, padx=5, pady=5)
clear= ttk.Button(window, text="Clear", command= clear)
clear.grid(row=3, column=2, sticky= W, padx=5, pady=5)

window.mainloop()
