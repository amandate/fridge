from .foodStorage import FoodStorage

class Fridge(FoodStorage):
    def __init__(self, expiration_window=7):
        super().__init__(expiration_window)