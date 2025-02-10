import tkinter as tk
from tkinter import font, ttk, Frame
from PIL import Image, ImageTk
import pickle
from classe_pokemon import Pokemon

# Fonction pour que les input poids et taille soit uniquement des float
def valeur_valide(new_value):
    if new_value == "":
        return True
    try:
        float(new_value.replace(",", "."))
        return True
    except ValueError:
        return False

# Fonction pour afficher le Pokémon sélectionné
def afficher_pokemon(event):
    name = liste_pokemon.curselection()
    nom_selectionne = liste_pokemon.get(name)
    pokemon = liste_des_pokemon.get(nom_selectionne, "")
    label_nom.config(text=f"{pokemon.number}")
    pass

# Fonction pour enregistrer un Pokémon
def enregistrer_pokemon():
    pass




window = tk.Tk()
window.config(bg="#ee1c25")
window.title("Pokédex")

# Numéro du pokémon, nom, image, types, taille, poids

# Interface
image_logo = ImageTk.PhotoImage(Image.open("img/logo.png"))
logo = tk.Label(window, image=image_logo, bg="#ee1c25")
logo.place(x=20, y=10)

liste_pokemon = tk.Listbox(window, height=29, borderwidth=0, highlightthickness=0)
liste_pokemon.place(x=12, y=120)
liste_pokemon.bind("<<ListboxSelect>>", afficher_pokemon)

image_entete = ImageTk.PhotoImage(Image.open("img/logo-pokemon.png"))
entete = tk.Label(window, image=image_entete, bg="#ee1c25")
entete.place(relx=0.5, y=60, anchor="center")

chemin_police1 = "polices/Pokemon-Solid.ttf"
police_pokemon = font.Font(family="Pokemon Solid", size=16)
label_nom = tk.Label(window, text="#000 MissingNo", font=police_pokemon, bg="#ee1c25", fg="white")
label_nom.place(relx=0.5, y=140, anchor="center")

image_pokemon = ImageTk.PhotoImage(Image.open("img/image_resized.png"))
dessin_pokemon = tk.Label(window, image=image_pokemon, bg="#ee1c25")
dessin_pokemon.place(relx=0.5, y=350, anchor="center")

label_types = tk.Label(window, text="Type(s) :", bg="#ee1c25", fg="white")
label_types.place(relx=0.32, y=500, anchor="center")

image_type_1 = ImageTk.PhotoImage(Image.open("img/Type-resized-1.png"))
label_type_1 = tk.Label(window, image=image_type_1, bg="#ee1c25")
label_type_1.place(relx=0.27, y=550, anchor="center")

image_type_2 = ImageTk.PhotoImage(Image.open("img/Type-resized-2.png"))
label_type_2 = tk.Label(window, image=image_type_1, bg="#ee1c25")
label_type_2.place(relx=0.38, y=550, anchor="center")

label_taille = tk.Label(window, text="Taille :", bg="#ee1c25", fg="white")
label_taille.place(relx=0.5, y=500, anchor="center")

petite_police_pokemon = font.Font(family="Pokemon Solid", size=12)
taille_pokemon = tk.Label(window, text="0 m", font=petite_police_pokemon, bg="#ee1c25", fg="white")
taille_pokemon.place(relx=0.5, y=547, anchor="center")

label_poids = tk.Label(window, text="Poids :", bg="#ee1c25", fg="white")
label_poids.place(relx=0.68, y=500, anchor="center")

poids_pokemon = tk.Label(window, text="0.0 kg", font=petite_police_pokemon, bg="#ee1c25", fg="white")
poids_pokemon.place(relx=0.68, y=547, anchor="center")

# Ajout de pokémon :

frame_ajout = Frame(window, height=450, width=190, bg="#ee1c25", highlightbackground="black", highlightthickness=4)
frame_ajout.place(relx=0.88, y=350, anchor="center")

moyenne_police_pokemon = font.Font(family="Pokemon Solid", size=13)
label_ajout_pokemon = tk.Label(window, text="Ajouter un Pokémon", font=moyenne_police_pokemon, bg="#ee1c25", fg="white")
label_ajout_pokemon.place(relx=0.88, y=170, anchor="center")

label_ajout_nom = tk.Label(window, text="Nom", bg="#ee1c25", fg="white")
label_ajout_nom.place(relx=0.88, y=210, anchor="center")

entry_ajout_nom = tk.Entry(window, width=23)
entry_ajout_nom.place(relx=0.88, y=230, anchor="center")

label_ajout_types = tk.Label(window, text="Type(s)", bg="#ee1c25", fg="white")
label_ajout_types.place(relx=0.88, y=270, anchor="center")

ajout_type_1 = ttk.Combobox(window)
ajout_type_1.place(relx=0.88, y=295, anchor="center")
ajout_type_1['values'] = ('Acier', 'Combat', 'Dragon', 'Eau', 'Electrik', 'Fée', 'Feu', 'Glace', 'Inconnu', 'Insecte', 'Normal', 'Plante', 'Poison', 'Psy', 'Roche', 'Sol', 'Spectre', 'Ténebres', 'Vol')
ajout_type_1.set('Normal')

ajout_type_2 = ttk.Combobox(window)
ajout_type_2.place(relx=0.88, y=320, anchor="center")
ajout_type_2['values'] = ('Aucun', 'Acier', 'Combat', 'Dragon', 'Eau', 'Electrik', 'Fée', 'Feu', 'Glace', 'Inconnu', 'Insecte', 'Normal', 'Plante', 'Poison', 'Psy', 'Roche', 'Sol', 'Spectre', 'Ténebres', 'Vol')
ajout_type_2.set('Aucun')

label_ajout_taille = tk.Label(window, text="Taille (en m)", bg="#ee1c25", fg="white")
label_ajout_taille.place(relx=0.88, y=360, anchor="center")

vcmd = window.register(valeur_valide)
ajout_taille = tk.Entry(window, width=23, validate="key", validatecommand=(vcmd, "%P"))
ajout_taille.place(relx=0.88, y=380, anchor="center")

label_ajout_poids = tk.Label(window, text="Poids (en kg)", bg="#ee1c25", fg="white")
label_ajout_poids.place(relx=0.88, y=420, anchor="center")

ajout_poids = tk.Entry(window, width=23, validate="key", validatecommand=(vcmd, "%P"))
ajout_poids.place(relx=0.88, y=440, anchor="center")

label_ajout_image = tk.Label(window, text="Lien vers l'image", bg="#ee1c25", fg="white")
label_ajout_image.place(relx=0.88, y=480, anchor="center")

texte_defaut = tk.StringVar(value=".png")
ajout_image = tk.Entry(window, textvariable=texte_defaut, width=23)
ajout_image.place(relx=0.88, y=500, anchor="center")

button_ajout = tk.Button(window, text="Ajouter votre Pokémon")
button_ajout.place(relx=0.88, y=550, anchor="center")

arcanin = Pokemon("059", "arcanin", "feu", 1.9, 155.0)
bulbizarre = Pokemon("001", "Bulbizarre", "Plante", 0.7, 7.9, "Poison")
dracaufeu = Pokemon("006", "Dracaufeu", "Feu", 1.7, 90.5, "Vol")
spectrum = Pokemon("093", "Spectrum", "Spectre", 1.6, 0.1, "Poison")
liste_pokemon.insert(tk.END, "Bulbizarre")
liste_pokemon.insert(tk.END, "Dracaufeu")
liste_pokemon.insert(tk.END, "Spectrum")
liste_pokemon.insert(tk.END, "Arcanin")

nom_des_pokemon = ["Bulbizarre", "Dracaufeu", "Spectrum", "Arcanin"]
pokemon = [bulbizarre, dracaufeu, spectrum, arcanin]


liste_des_pokemon = dict(zip(nom_des_pokemon, pokemon))

window.geometry("800x600")
window.mainloop()