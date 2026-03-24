class Score:
    def __init__(self):
        self.points = 0

    def add_points(self, amount):
        if amount < 0:
            raise ValueError("amount cannot be negative")
        self.points += amount

    def reset(self):
        self.points = 0