from src.Session.profile import Profile

class Commands:
    def __init__(self):
        self.profile = None

    def add_food(self):
        pass

    def remove_food(self):
        pass

    def create_freezer(self):
        pass

    def create_fridge(self):
        pass

    def create_profile(self):
        profile_name = input("What would you like to name your profile?: ")

        if self.profile and self.profile.name != profile_name:
            self.profile.save()

        self.profile = Profile(profile_name)
        print(f"Successfully created profile. Now switching to profile: {profile_name}.")

    def help(self):
        pass

    def list_food_storages(self):
        pass

    def list_fridges(self):
        pass

    def list_freezers(self):
        pass

    def load(self, profile):
        pass
    
    def open(self, food_storage):
        pass

    def save(self):
        pass

    def delete(self, food_storage):
        pass
    
    def delete_profile(self):
        pass