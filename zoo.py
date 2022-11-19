from abc import ABC, abstractmethod

# Template Method in Python With Abstract Class

class AbstractZoo(ABC):

    def PresentAnimal(self):
        self.AnimalName()
        self.WalkAnimal()
        self.ObservedByHumanHook()

    @abstractmethod
    def AnimalName(self):
        pass

    def WalkAnimal(self):
        print("Is On Walk")

    def ObservedByHumanHook(self):
        pass


class Wolf(AbstractZoo):
    def AnimalName(self):
        print("Wolf")

    def ObservedByHumanHook(self):
        print("5 Humans Observing")


class Elephant(AbstractZoo):
    def AnimalName(self):
        print("Elephant")

    def ObservedByHumanHook(self):
        print("10 Humans Observing")


class Bear(AbstractZoo):
    def AnimalName(self):
        print("Bear")


def PresentationClient(abstract_class: AbstractZoo):
    print("")
    abstract_class.PresentAnimal()


PresentationClient(Wolf())
PresentationClient(Elephant())
PresentationClient(Bear())
