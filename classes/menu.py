from classes.menu_item import MenuItem


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item: MenuItem):
        self.items.append(menu_item)

    def remove_item(self, item_name: MenuItem):
        self.items.remove(item_name)

    def get_item_by_name(self, name):
        for i in self.items:
            if i.name == name:
                return i
        return f"item not fount"

    def get_items_by_category(self, category):
        category_lst = []
        for i in self.items:
            if i.category == category:
                category_lst.append(i)
        if category_lst:
            return category_lst
        return "category not found"

    def display_menu(self):
        available_item = []
        for i in self.items:
            if i.available:
                available_item.append(i)
        if available_item:
            return available_item
        return f"There are no available items"
    def get_total_items(self):
        return len(self.items)

