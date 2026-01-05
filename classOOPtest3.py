class Crustacean:
    def __init__(self, type, legs, shell, antennae, aquatic):
        self.type = type
        self.legs = legs
        self.shell = shell
        self.antennae = antennae
        self.aquatic = aquatic
    
    def attributes(self):
        info = "\nType: {}\nLegs: {}\nShell: {}\nAntennae: {}\nAquatic: {}".format(self.type, self.legs, self.shell, self.antennae, self.aquatic)
        return info




crab = Crustacean("Crab", 10, "True", 2, "Mostly")
print(crab.attributes())
