from classes.customer import Customer
from classes.menu_item import MenuItem


class Order:
    def __init__(self, customer: Customer, order_number):
        self.customer = customer
        self.order_number = order_number
        self.items = []
        self.status = "pending"
        self.total_price = 0

    def add_item(self, menu_item: MenuItem):
        self.items.append(menu_item)
        self.total_price += 1

    def remove_item(self, menu_item: MenuItem):
        self.items.remove(menu_item)
        self.total_price -= 1

    def get_total(self):
        return self.total_price

    def set_status(self, new_status):
        statuses = ["pending", "cooking", "ready", "delivered"]
        if new_status in statuses:
            self.status = new_status
        else:
            print(f"This status is not legal")

    def display_order(self):
        print(f"""
                number: {self.order_number}
                customer: {self.customer.name}
                items: {[i.get_info() for i in self.items]}
                total price: {self.total_price}
                status: {self.status}""")

    def is_complete(self):
        if self.status == "delivered":
            return True
        return False
