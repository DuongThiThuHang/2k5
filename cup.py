class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
        
    def fill(self, milliliters):
        if self.quantity + milliliters <= self.size:
            self.quantity += milliliters
        else:
            pass
        
    def status(self):
        return self.size - self.quantity
        
        
cup = Cup(70, 30)
print(cup.status())
cup.fill(20)
cup.fill(20)
print(cup.status())