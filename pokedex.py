import tkinter as tk
from tkinter import font, ttk, Frame, messagebox
from PIL import Image, ImageTk
import pickle
from classe_pokemon import Pokemon
from tkinter import filedialog as fd
import os

# Fonction pour que les input poids et taille soit uniquement des float
def valeur_valide(new_value):
    if new_value == "":
        return True
    try:
        float(new_value.replace(",", "."))
        return True
    except ValueError:
        return False
    
# Fonction pour ajuster la taille des images de Pokemon automatiquement
def resize_pokemon(link):
    image = Image.open(f"{link}")

    new_width = 250
    aspect_ratio = image.height / image.width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

    resized_image.save(f"{link}")

# Fonction pour ajuster la taille des types automatiquement
def resize_type(type1, type2):
    image1 = Image.open(f"img/Type-{type1}.png")

    new_width = 80
    aspect_ratio = image1.height / image1.width
    new_height = int(new_width * aspect_ratio)
    resized_image = image1.resize((new_width, new_height), Image.LANCZOS)

    resized_image.save(f"img/Type-{type1}.png")

    if type2 != "aucun":
        image2 = Image.open(f"img/Type-{type2}.png")

        new_width = 80
        aspect_ratio = image2.height / image2.width
        new_height = int(new_width * aspect_ratio)
        resized_image2 = image2.resize((new_width, new_height), Image.LANCZOS)

        resized_image2.save(f"img/Type-{type2}.png")

# Fonction pour choisir l'image de son Pokémon
def select_file():
    filetypes = (('text files', '*.png *.jpg *.jpeg'), ('All files', '*.*'))

    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)

    if filename:
        label_ajout_image_propre.config(text=os.path.basename(filename))
        ajout_image.insert(0, filename)

# Fonction pour afficher le Pokémon sélectionné
def afficher_pokemon(event):
    name = liste_pokemon.curselection()
    nom_selectionne = liste_pokemon.get(name)
    pokemon = liste_des_pokemon.get(nom_selectionne, "")
    label_nom.config(text=f"{pokemon.name}")
    resize_pokemon(pokemon.link)
    image_pokemon = ImageTk.PhotoImage(Image.open(f"{pokemon.link}"))
    dessin_pokemon.config(image=image_pokemon)
    dessin_pokemon.image = image_pokemon
    resize_type(pokemon.type1, pokemon.type2)
    image_type_1 = ImageTk.PhotoImage(Image.open(f"img/Type-{pokemon.type1}.png"))
    label_type_1.config(image=image_type_1)
    label_type_1.image = image_type_1
    label_type_1.place(relx=0.27, y=550, anchor="center")
    if pokemon.type2 != "aucun":
        image_type_2 = ImageTk.PhotoImage(Image.open(f"img/Type-{pokemon.type2}.png"))
        label_type_2.config(image=image_type_2)
        label_type_2.image = image_type_2
        label_type_2.place(relx=0.38, y=550, anchor="center")
    else:
        label_type_2.place_forget()
        label_type_1.place(relx=0.32, y=550, anchor="center")
    poids_pokemon.config(text=f"{pokemon.weight} kg")
    taille_pokemon.config(text=f"{pokemon.height} m")

# Fonction pour enregistrer un Pokémon
def enregistrer_pokemon():
    name = entry_ajout_nom.get()
    type_1 = ajout_type_1.get()
    type_2 = ajout_type_2.get()
    height = ajout_taille.get()
    weight = ajout_poids.get()
    link = ajout_image.get()
    if name != "" and type_1 != "" and height != "" and weight != "":
        nom_pokemon = name.lower()
        nom_pokemon = Pokemon(name, type_1, height, weight, type_2, link)
        nom_des_pokemon.append(name.title())
        pokemon.append(nom_pokemon)
        liste_pokemon.insert(tk.END, name.title())
        liste_des_pokemon[name.title()] = nom_pokemon
        enregistrer_donnees(liste_des_pokemon)
        messagebox.showinfo("Succès", "Votre Pokémon a été enregistré")
        entry_ajout_nom.delete(0, 'end')
        ajout_taille.delete(0, 'end')
        ajout_poids.delete(0, 'end')
        ajout_image.delete(0, 'end')
        ajout_type_1.set('Normal')
        ajout_type_2.set('Aucun')
        label_ajout_image_propre.config(text="Aucune image sélectionné")
    else:
        messagebox.showinfo("Erreur", "Veuillez entrer un nom, au moins un type, une taille et un poids à votre Pokémon")


window = tk.Tk()
window.config(bg="#ee1c25")
window.resizable(False, False)
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
label_nom = tk.Label(window, text="MissingNo", font=police_pokemon, bg="#ee1c25", fg="white")
label_nom.place(relx=0.5, y=140, anchor="center")

image_pokemon = ImageTk.PhotoImage(Image.open("img/missingno.png"))
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

label_ajout_image_propre = tk.Label(window, text="Aucune image sélectionné", bg="#ee1c25", fg="white")
label_ajout_image_propre.place(relx=0.88, y=480, anchor="center")

ajout_image = tk.Entry(window)
ajout_image.place(x=1000, y=1000)

button_add_image = tk.Button(window, text="Choisir une image", command=select_file)
button_add_image.place(relx=0.88, y=503, anchor="center")

button_ajout = tk.Button(window, text="Ajouter votre Pokémon", command=enregistrer_pokemon)
button_ajout.place(relx=0.88, y=550, anchor="center")

nom_des_pokemon = []
pokemon = []

# Mise en place de pickle
fichier_de_sauvegarde = "pokemon_data.pk1"

# Chargement du dictionnaire de Pokemon
def chargement_donnees():
    if os.path.exists(fichier_de_sauvegarde):
        with open(fichier_de_sauvegarde, "rb") as file:
            return pickle.load(file)
    return {}

# Fonction d'enregistrement pickle
def enregistrer_donnees(data):
    with open(fichier_de_sauvegarde, "wb") as file:
        pickle.dump(data, file)

liste_des_pokemon = chargement_donnees()

for cle, valeur in liste_des_pokemon.items():
    liste_pokemon.insert(tk.END, cle)
    nom_des_pokemon.append(valeur.name)
    pokemon.append(valeur)

window.geometry("800x600")
window.mainloop()