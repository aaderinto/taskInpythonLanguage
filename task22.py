class Hunt:
    _weapon = "Assault Rifle"

    def get_weapon(self, not_available):
        return not_available


yinka = Hunt()
print(yinka.get_weapon(Hunt._weapon))
