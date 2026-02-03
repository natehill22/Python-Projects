#Creates a parent class and its default class attributes
class Crustacean:
    type = "Unknown"
    legs = None
    shell = None
    antennae = None
    habitat = "Unknown"

    #Parent class methods (variations of these will be inherited by the child classes)
    def attributes(self):
        info = "\nType: {}\nLegs: {}\nShell: {}\nAntennae: {}\nHabitat: {}".format(self.type, self.legs, self.shell, self.antennae, self.habitat)
        return info

    def eat(self):
        eating = "\nCrustaceans eat through mandibles, maxillae, and maxillipeds."
        return eating
    
    def scuttle(self):
        move = "\nCrustaceans move around by scuttling over terrain or swimming through water."
        return move

#Creates a child class that uses the Crustacean class as its parent
class Shrimp(Crustacean):
    type = "shrimp"
    legs = 10
    shell = "Exoskeleton"
    antennae = 4
    habitat = "Aquatic"
    #Child-specific attributes below
    parentalCare = "All Parents"
    locationOfHeart = "Head"
    circulatorySystem = "Open"

    #Inherited methods adjusted to include child specific attributes and updated names
    def attributes(self):
        info = "\nType: {}\nLegs: {}\nShell: {}\nAntennae: {}\nHabitat: {}\
            \nParental Care: {}\nLocation of Heart: {}\nCirculatory System: {}\
            ".format(self.type, self.legs, self.shell, self.antennae, \
            self.habitat, self.parentalCare, self.locationOfHeart, self.circulatorySystem)
        return info

    def eat(self):
        eating = "\nShrimp eat through mandibles, maxillae, and maxillipeds."
        return eating
    
    def scuttle(self):
        move = "\nShrimp move around by scuttling over terrain or swimming through water."
        return move

    #Child-specific method
    def backwardSwim(self):
        message = "\nMany shrimp can swim faster backwards than forwards by quickly flexing their tail and abdomen!"
        return message

#Creates a child class that uses the Crustacean class as its parent
class Crab(Crustacean):
    type = "crab"
    legs = 10
    shell = "Exoskeleton"
    antennae = 4
    habitat = "Mostly Aquatic"
    #Child-specific attributes below
    regeneration = True
    parentalCare = "Mother"
    eyes = "Compound on stalks, allowing 360-degree view."

    #Inherited methods adjusted to include child specific attributes and updated names
    def attributes(self):
        info = "\nType: {}\nLegs: {}\nShell: {}\nAntennae: {}\nHabitat: {}\
            \nRegeneration: {}\nParental Care: {}\nEyes: {}".format(self.type, \
            self.legs, self.shell, self.antennae, self.habitat, self.regeneration, \
            self.parentalCare, self.eyes)
        return info

    def eat(self):
        eating = "\nCrabs eat through mandibles, maxillae, and maxillipeds."
        return eating
    
    def scuttle(self):
        move = "\nCrabs move around by scuttling over terrain or swimming through water."
        return move

    #Child-specific method
    def sidewaysWalk(self):
        message = "\nCrabs walk sideways due to their leg joints being built for lateral movement. It's often the quickest and most efficient way for them to move."
        return message

#Creates a child class that uses the Crustacean class as its parent
class Woodlouse(Crustacean):
    type = "woodlice"
    legs = 14
    shell = "Exoskeleton"
    antennae = 4
    habitat = "Terrestrial"
    #Child-specific attributes below
    conglobation = True
    timeActive = "Nocturnal"

    #Inherited methods adjusted to include child specific attributes and updated names
    def attributes(self):
        info = "\nType: {}\nLegs: {}\nShell: {}\nAntennae: {}\nHabitat: {}\
            \nConglobation: {}\nTime Active: {}".format(self.type, self.legs, \
            self.shell, self.antennae, self.habitat, self.conglobation, \
            self.timeActive)
        return info

    def eat(self):
        eating = "\nWoodlice eat through mandibles, maxillae, and maxillipeds."
        return eating
    
    def scuttle(self):
        move = "\nWoodlice move around by scuttling over terrain."
        return move

    #Child-specific method
    def rollUp(self):
        message = "\nWoodlice roll up into a ball to use their hard exoskeleton to protect their soft underside from predators."
        return message

#Creates a list of child classes (i.e. parent instances). This will be used in the following loop.
crustaceans: list[Crustacean] = [
    Shrimp(),
    Crab(),
    Woodlouse()
]

for crustacean in crustaceans:
    #Prints all data (in 'attributes') and methods of the Crustacean parent class through all its child classes
    if isinstance(crustacean, Crustacean):
        print(crustacean.attributes())
        print(crustacean.eat())
        print(crustacean.scuttle())
        #Checks if subclasses have these methods and prints them, if so. This is means to print child-specific methods alongside the inherited (and adjusted) parent methods
        if hasattr(crustacean, 'backwardSwim'):
            print(crustacean.backwardSwim())
        if hasattr(crustacean, 'sidewaysWalk'):
            print(crustacean.sidewaysWalk())
        if hasattr(crustacean, 'rollUp'):
            print(crustacean.rollUp())
        print("-" * 80) # Adds section barries for read-ability
