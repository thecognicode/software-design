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
        return total - 500

class PercentageDiscount(Discount):

    def apply(self, total):
        return total * 0.9


class Cart:

    def __init__(self, total, discount):
        self.total = total
        self.discount = discount

    def checkout(self):
        return self.discount.apply(self.total)

cart = Cart(5000, PercentageDiscount())
print(cart.checkout())