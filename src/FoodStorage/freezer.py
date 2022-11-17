from .foodStorage import FoodStorage

class Freezer(FoodStorage):
    def __init__(self, expiration_window=7):
        super().__init__(expiration_window)

