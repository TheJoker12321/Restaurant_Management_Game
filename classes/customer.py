class Customer:
    def __init__(self, name):
        self.name = name
        self.satisfaction = 50

    def increase_satisfaction(self, amount):
        if self.satisfaction + amount > 100:
            self.satisfaction = 100
        else:
            self.satisfaction += amount

    def decrease_satisfaction(self, amount):
        if self.satisfaction - amount < 0:
            self.satisfaction = 0
        else:
            self.satisfaction -= amount

    def is_happy(self):
        if self.satisfaction > 70:
            return True
        return False

    def get_info(self):
        return f"The customer's name is {self.name} and his level of satisfaction is {self.satisfaction}"