class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        
    def get_items_count(self):
        return len(self.items)
        
shop = Shop("My Shop", ["Son", "Ke mat", "Phan ma"])
print(shop.get_items_count())