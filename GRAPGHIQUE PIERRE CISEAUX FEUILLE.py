from tkinter import*
from random import*
fenetre= Tk()                            #Pour créer la fenêttre
fenetre.title("pierre,papier,ciseaux")   #Pour donner untitre à la fenêttre


ciseaux=PhotoImage(file= 'ciseaux.gif ')
pierre=PhotoImage(file= 'pierre.gif ')
papier=PhotoImage(file= 'papier.gif ')
point=PhotoImage(file= 'point.gif ')

def jouer_pierre():
    joueur(1)
    point1.config(image=pierre)
def jouer_ciseaux():
    joueur(2)
    point1.config(image=ciseaux)
def jouer_papier():
    joueur(3)
    point1.config(image=papier)

joueurtexte=Label(fenetre,text="joueur",font=("Helvetica",16))
ordi=Label(fenetre,text="ordinateur",font=("Helvetica",16))
ligne0=Label(fenetre,text="vous avez...",font=("Helvetica",16))
ligne3=Label(fenetre,text="pour jouer,cliquez sur une des icônes ci-dessous",font=("Helvetica",12))
ligne2=Label(fenetre,text="versus",font=("Helvatica",14))
point1=Label(fenetre, image = point)
point2=Label(fenetre, image = point)
ciseaux1=Button(fenetre, image = ciseaux,command=jouer_ciseaux)
papier1=Button(fenetre,image= papier,command=jouer_papier)
pierre1=Button(fenetre,image=pierre,command=jouer_pierre)
versus=Label(fenetre,text="VERSUS",font=("Helvetica",17))
versus.grid(row=2,column=1)
quitter=Button(fenetre, text='quitter',command=fenetre.destroy)
quitter.grid(row=5, column=0,columnspan=3 ,padx=0,pady=0)


joueurtexte.grid(row=1 , column=0 , padx=0 , pady=0)
ordi.grid(row=1 , column=2 , padx=0 , pady=0)
point1.grid(row=2 , column=0, padx=0, pady=0)
point2.grid(row=2 , column=2, padx=0, pady=0)
ciseaux1.grid(row=4 , column=2, padx=0, pady=0)
pierre1.grid(row=4 , column=0, padx=0, pady=0)
papier1.grid(row=4 , column=1, padx=0, pady=0)
ligne0.grid(row=0, columnspan=3, padx=1, pady=1)
ligne3.grid(row=3, columnspan=3, padx=1, pady=1)
ligne2.grid(row=2, column=2,padx=0,pady=0)


def joueur(coup_joueur):
    coup_ordi=randint(1,3)
    #1=pierre
    #2=ciseaux
    #3=papier
    if coup_joueur==1 and coup_ordi==1:
        point2.config(image=pierre)
        ligne0.config(text="Egalité")
    elif coup_joueur==2 and coup_ordi==2:
        point2.config(image=ciseaux)
        ligne0.config(text="Egalité")
    elif coup_joueur==3 and coup_ordi==3:
        point2.config(image=papier)
        ligne0.config(text="Egalité")
    elif coup_joueur==1 and coup_ordi==2:
        point2.config(image=ciseaux)
        ligne0.config(text="vous gagnez")
    elif coup_joueur==1 and coup_ordi==3:
        point2.config(image=papier)
        ligne0.config(text="vous perdez")
    elif coup_joueur==2 and coup_ordi==1:
        point2.config(image=pierre)
        ligne0.config(text="vous perdez")
    elif coup_joueur==2 and coup_ordi==3:
        point2.config(image=papier)
        ligne0.config(text="vous gagnez")
    elif coup_joueur==3 and coup_ordi==1:
        point2.config(image=pierre)
        ligne0.config(text="vous gagnez")
    elif coup_joueur==3 and coup_ordi==2:
        point2.config(image=ciseaux)
        ligne0.config(text="vous perdez")

fenetre.mainloop()