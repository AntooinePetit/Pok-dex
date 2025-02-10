from PIL import Image

# Charger l'image locale
image = Image.open("img/missingno (2).png")

# Redimensionner en conservant les proportions
new_width = 250
aspect_ratio = image.height / image.width
new_height = int(new_width * aspect_ratio)
resized_image = image.resize((new_width, new_height), Image.LANCZOS)

# Sauvegarder ou afficher l'image redimensionnée
resized_image.save("img/image_resized.png")