import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import pickle

window = tk.Tk()
window.config(bg="#ee1c25")

# Numéro du pokémon, nom, image, types, taille, poids

# Interface
image_logo = ImageTk.PhotoImage(Image.open("img/logo.png"))
logo = tk.Label(window, image=image_logo, bg="#ee1c25")
logo.place(x=20, y=10)

liste_pokemon = tk.Listbox(window, height=29, borderwidth=0, highlightthickness=0)
liste_pokemon.place(x=12, y=120)

image_entete = ImageTk.PhotoImage(Image.open("img/logo-pokemon.png"))
entete = tk.Label(window, image=image_entete, bg="#ee1c25")
entete.place(relx=0.5, y=60, anchor="center")

chemin_police1 = "polices/Pokemon-Solid.ttf"
police_pokemon = font.Font(family="Pokemon Solid", size=16)
etiquette_nom = tk.Label(window, text="#000 Nom Pokemon", font=police_pokemon, bg="#ee1c25", fg="white")
etiquette_nom.place(relx=0.5, y=140, anchor="center")

image_pokemon = ImageTk.PhotoImage(Image.open("img/image_resized.png"))
dessin_pokemon = tk.Label(window, image=image_pokemon, bg="#ee1c25")
dessin_pokemon.place(relx=0.5, y=350, anchor="center")

label_types = tk.Label(window, text="Type(s) :", bg="#ee1c25", fg="white")
label_types.place(relx=0.32, y=500, anchor="center")

image_type_1 = ImageTk.PhotoImage(Image.open("img/Type-resized.png"))
label_type_1 = tk.Label(window, image=image_type_1, bg="#ee1c25")
label_type_1.place(relx=0.27, y=550, anchor="center")

image_type_2 = ImageTk.PhotoImage(Image.open("img/Type-resized.png"))
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

# Mettre les logos des types ?



# Ajout de pokémon : faire deux combobox pour les types de pokémons

window.geometry("800x600")
window.mainloop()