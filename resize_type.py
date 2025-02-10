from PIL import Image

# Charger l'image locale
image = Image.open("img/type-inconnu.png")

# Redimensionner en conservant les proportions
new_width = 80
aspect_ratio = image.height / image.width
new_height = int(new_width * aspect_ratio)
resized_image = image.resize((new_width, new_height), Image.LANCZOS)

# Sauvegarder ou afficher l'image redimensionnée
resized_image.save("img/type-resized-1.png")

# Charger l'image locale
image = Image.open("img/type-inconnu.png")

# Redimensionner en conservant les proportions
new_width = 80
aspect_ratio = image.height / image.width
new_height = int(new_width * aspect_ratio)
resized_image = image.resize((new_width, new_height), Image.LANCZOS)

# Sauvegarder ou afficher l'image redimensionnée
resized_image.save("img/type-resized-2.png")