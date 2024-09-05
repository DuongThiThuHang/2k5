class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False
    
    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True
    
    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"
            
flower = Flower("Hane", 500)
flower.water(30)
print(flower.status()) 
flower.water(60)
print(flower.status()) 
flower.water(70)
print(flower.status())             