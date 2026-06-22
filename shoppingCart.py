from abc import ABC, abstractmethod

class Discount(ABC):

    @abstractmethod
    def apply(self, total):
        pass


class NoDiscount(Discount):

    def apply(self, total):
        return total

class FlatDiscount(Discount):

    def apply(self, total):
        return total

