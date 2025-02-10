class Pokemon:
    def __init__(self, number, name, type1, height, weight, type2 = "Aucun"):
        self.number = number
        self.name = name.title()
        self.type1 = type1.title()
        self.type2 = type2.title()
        self.height = height
        self.weight = weight
        pass