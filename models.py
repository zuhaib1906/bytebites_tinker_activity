# Customer stores user information and purchase history.
# FoodItem stores item details such as name, price, category, and popularity.
# Menu manages a collection of FoodItem objects and supports category filtering.
# Order groups selected FoodItem objects and calculates the total cost.


class FoodItem:
    """One product a customer can buy (e.g. "Spicy Burger")."""

    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    """The full collection of items offered, with category filtering."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        return [item for item in self.items if item.category == category]

    def sort_by_price(self, descending=False):
        return sorted(self.items, key=lambda item: item.price, reverse=descending)

    def sort_by_popularity(self, descending=False):
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=descending)


class Order:
    """One checkout transaction: stores selected items and the total cost."""

    def __init__(self):
        self.items = []
        self.total_cost = 0.0

    def add_item(self, item):
        self.items.append(item)

    def compute_total(self):
        return sum(item.price for item in self.items)


class Customer:
    """A person using the app; tracks identity and past orders."""

    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, order):
        self.purchase_history.append(order)