class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.available = True

    def get_info(self):
        return f"""
                The MenuItem:
                name: {self.name}
                price: {self.price}
                category: {self.category}"""
    def set_available(self, status: bool):
        self.available = status

    def is_available(self):
        return self.available



