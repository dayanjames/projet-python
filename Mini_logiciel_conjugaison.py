# Vous devez installer le module verbecc :  pip install verbecc
#from verbecc import Conjugator
from textblob import Word
from tkinter import Text
import tkinter as tk
from tkinter import ttk
 
def conjuguer():
    verbe = entrerVerbe.get()
    temps = listeVerbes.get()
    cg = Word(lang='fr')
    conjugation = cg.conjugate(verbe)
    conj = conjugation['moods']['indicatif'][temps]
    result = ""
    for element in conj:
        result = result + element + '\n'
        
    Affichage.insert(1.0 , "Conjugaison du verbe " + verbe + ' au ' + temps + '\n\n' + result)
    
 
#--------------------
# fenetre principale
#-------------------
wen = tk.Tk()
wen.title("Conjugaison")
wen.geometry("600x400")
# création du titre de la fenêtre
labelTitle = tk.Label(wen , 
                    text = " Conjugaison des verbes" , 
                    font = ("Arial" , 16) ,
                    foreground='white', 
                    background='darkblue')
labelTitle.place(x=0 , y= 0 , width=600 ) 
 
#-----------------------------------------------------
# label qui demande à l'utilisateur de saisir un verbe
#-----------------------------------------------------
labelVerbe = tk.Label(wen , text = "veuillez  saisir un verbe de votre choix:")
labelVerbe.place( x = 10 , y = 50)
 
entrerVerbe = tk.Entry(wen)
entrerVerbe.place(x = 100 , y = 50 , width = 200)
 
#------------------
# liste verbes
#-----------------
listeTemps = ["présent",  "futur-simple", "passé-simple", 
              "imparfait", "plus-que-parfait", "passé-composé", 
              "futur-antérieur",  "passé-antérieur"]
listeVerbes = ttk.Combobox(wen , values = listeTemps)
listeVerbes.place(x = 350 , y = 50 , width = 200)
listeVerbes.current(0)
 
#-----------------------------------------------------
# zone de texte pour afficher les verbes conjugués
#-----------------------------------------------------
Affichage = Text( wen )
Affichage.place(x = 100 , y = 100 , width = 450 , height = 200)
 
#------------------
# Bouton conjuguer
#-----------------
boutonConjuguer = tk.Button(wen , text = "Conjuguer le verbe au temps demandé" , command = conjuguer )
boutonConjuguer.place(x = 100 , y = 310 , width = 450)
 
wen.mainloop()
 