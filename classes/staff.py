class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.energy = 100

    def work(self):
        self.energy -= 10
        print("Due to the heavy workload, the energy dropped by 10.")

    def rest(self):
        if self.energy + 20 > 100:
            self.energy = 100
        else:
            self.energy += 20

    def is_tired(self):
        if self.energy < 30:
            return True
        return False

    def get_info(self):
        return f"""
                name: {self.name}
                salary: {self.salary}
                energy: {self.energy}"""
    
