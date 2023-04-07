class ShoppingCart:
    def __init__(self):
        self.items = []

    def addToCart(self, item): 
        self.items.append(item)

    def removeFromCart(self, itemIndex):
        self.items.pop(itemIndex)

    def getTotalPrice(self):
        totalPrice = 0
        for item in self.items:
            totalPrice += item[1]
        return totalPrice

    def getCartItems(self):
        return self.items

    def emptyCart(self):
        self.items.clear()
     