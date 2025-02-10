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
liste_pokemon.place(x=10, y=120)

image_entete = ImageTk.PhotoImage(Image.open("img/logo-pokemon.png"))
entete = tk.Label(window, image=image_entete, bg="#ee1c25")
entete.place(x=260, y=10)

chemin_police1 = "polices/Pokemon-Solid.ttf"
police_pokemon = font.Font(family="Pokemon Solid", size=16)
etiquette_nom = tk.Label(window, text="Pikachu", font=police_pokemon, bg="#ee1c25", fg="white")
etiquette_nom.place(relx=0.5, y=140, anchor="center")

image_pokemon = ImageTk.PhotoImage(Image.open("img/Arcanin.png"))

# Mettre les logos des types ?



# Ajout de pokémon : faire deux combobox pour les types de pokémons

window.geometry("800x600")
window.mainloop()