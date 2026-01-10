from abc import ABC, abstractmethod

#Abstract Base Class
class FlatCake(ABC):
    @abstractmethod #This abstract method cannot be implemented unless it's through its child classes, which will need to redefine the method
    def distFeature(self):
        pass

    #A regular/concrete method (has full implementation in an abstract class). These can be inherited and used without needing to be redefined.  
    def cook(self):
        return f"{self.__class__.__name__} is an example of pan-fried, often yeasted, bread."

    @property #Abstract properties are declared in the abstract method/class, and they enforce that the child class provides the property's implementation
    @abstractmethod
    def tasteGood(self):
        pass

#The following are regular/concrete child classes that must implement the abstract (distFeature) method and (tasteGood) property of the inherited FlatCake parent class
class DutchBaby(FlatCake):
    def distFeature(self):
        return "Dutch Baby cakes are puffy, and souffle-like with crispy edges and a soft custardy center. They are known for their size and being one of the only pan cakes cooked in the oven (usually on a skillet)."
    @property
    def tasteGood(self):
        return "Very Good"

class Johnnycake(FlatCake):
    def distFeature(self):
        return "Johnnycakes are a flatbread primarily made from cornmeal and water or milk. This gives it a heartier texture and a distinct corn flavor. They are versatile for both sweet and savory uses."
    @property
    def tasteGood(self):
        return "Pretty Good"
    
class Crumpet(FlatCake):
    def distFeature(self):
        return "Crumpets are spongey and porous with a smooth flat bottom and a bubbly top. This porosity allows for better absortption of melted butter, jams, curds and other toppings."
    @property
    def tasteGood(self):
        return "Wow. So good."

#List of child functions, for more effecient printing
flatcakes = [DutchBaby(), Johnnycake(), Crumpet()]

#Object creation of child classes using abstract and regular/concrete methods
for cake in flatcakes:
    print(cake.distFeature()) #Child implementation of abstract method
    print() #Spacing
    print(cake.cook()) #Parent regular/concrete method
    print() #Spacing
    print(cake.tasteGood) #Child implementation of abstract property
    print("-" * 40)

