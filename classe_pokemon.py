import os

class Pokemon:
    def __init__(self, name, type1, height, weight, type2 = "Aucun", link = ""):
        self.name = name.title()
        if os.path.exists(f"img/Type-{type1}.png"):
            self.type1 = type1.lower()
        else:
            self.type1 = "inconnu"
        if os.path.exists(f"img/Type-{type2}.png"):
            self.type2 = type2.lower()
        else:
            self.type2 = "inconnu"
        self.height = height
        self.weight = weight
        if link == "":
            potential_link = f"img/{self.name}.png"
            if os.path.exists(potential_link):
                self.link = potential_link
            else:
                self.link = "img/missingno.png"
        else:
            if os.path.exists(link):
                self.link = link
            else:
                self.link = "img/missingno.png"
        pass