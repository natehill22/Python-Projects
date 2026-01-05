class Crustacean:
    type = "Unknown"
    legs = None
    shell = None
    antennae = None
    aquatic = False
    
    def attributes(self):
        info = "\nType: {}\nLegs: {}\nShell: {}\nAntennae: {}\nAquatic: {}".format(self.type, self.legs, self.shell, self.antennae, self.aquatic)
        return info


class Shrimp(Crustacean):
    type = "shrimp"
    legs = 10
    shell = True
    antennae = 4
    aquatic = True

    def backwardSwim(self):
        message = "\nMany shrimp can swim faster backwards than forwards by quickly flexing their tail and abdomen!"
        return message




shrimp = Shrimp()
print(shrimp.attributes())
print(shrimp.backwardSwim())
