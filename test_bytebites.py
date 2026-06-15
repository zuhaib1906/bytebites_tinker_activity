import unittest

from models import Customer, FoodItem, Menu, Order


class TestFoodItem(unittest.TestCase):
    def test_init_stores_all_attributes(self):
        item = FoodItem("Spicy Burger", 8.50, "Mains", 4.7)
        self.assertEqual(item.name, "Spicy Burger")
        self.assertEqual(item.price, 8.50)
        self.assertEqual(item.category, "Mains")
        self.assertEqual(item.popularity_rating, 4.7)


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.soda = FoodItem("Large Soda", 2.00, "Drinks", 4.0)
        self.water = FoodItem("Water", 1.00, "Drinks", 3.5)
        self.cake = FoodItem("Cheesecake", 5.00, "Desserts", 4.9)

    def _full_menu(self):
        menu = Menu()
        for item in (self.soda, self.water, self.cake):
            menu.add_item(item)
        return menu

    # __init__
    def test_init_starts_empty(self):
        self.assertEqual(Menu().items, [])

    # add_item
    def test_add_item_appends(self):
        menu = Menu()
        menu.add_item(self.soda)
        self.assertEqual(menu.items, [self.soda])
        menu.add_item(self.water)
        self.assertEqual(menu.items, [self.soda, self.water])

    # filter_by_category
    def test_filter_by_category_matches(self):
        self.assertEqual(self._full_menu().filter_by_category("Drinks"), [self.soda, self.water])

    def test_filter_by_category_no_match(self):
        self.assertEqual(self._full_menu().filter_by_category("Sides"), [])

    # sort_by_price
    def test_sort_by_price_ascending(self):
        self.assertEqual(self._full_menu().sort_by_price(), [self.water, self.soda, self.cake])

    def test_sort_by_price_descending(self):
        self.assertEqual(self._full_menu().sort_by_price(descending=True), [self.cake, self.soda, self.water])

    # sort_by_popularity
    def test_sort_by_popularity_ascending(self):
        self.assertEqual(self._full_menu().sort_by_popularity(), [self.water, self.soda, self.cake])

    def test_sort_by_popularity_descending(self):
        self.assertEqual(self._full_menu().sort_by_popularity(descending=True), [self.cake, self.soda, self.water])

    def test_sorting_is_non_mutating(self):
        menu = self._full_menu()
        original = [self.soda, self.water, self.cake]
        menu.sort_by_price()
        menu.sort_by_popularity(descending=True)
        self.assertEqual(menu.items, original)


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.burger = FoodItem("Spicy Burger", 8.50, "Mains", 4.7)
        self.soda = FoodItem("Large Soda", 2.00, "Drinks", 4.0)

    # __init__
    def test_init_starts_empty(self):
        order = Order()
        self.assertEqual(order.items, [])
        self.assertEqual(order.total_cost, 0.0)

    # add_item
    def test_add_item_appends(self):
        order = Order()
        order.add_item(self.burger)
        self.assertEqual(order.items, [self.burger])

    # compute_total
    def test_compute_total_empty(self):
        self.assertEqual(Order().compute_total(), 0.0)

    def test_compute_total_sums_prices(self):
        order = Order()
        order.add_item(self.burger)
        order.add_item(self.soda)
        self.assertEqual(order.compute_total(), 10.50)


class TestCustomer(unittest.TestCase):
    # __init__
    def test_init_stores_name_and_empty_history(self):
        customer = Customer("Ada")
        self.assertEqual(customer.name, "Ada")
        self.assertEqual(customer.purchase_history, [])

    # add_purchase
    def test_add_purchase_records_order(self):
        customer = Customer("Ada")
        order = Order()
        customer.add_purchase(order)
        self.assertEqual(customer.purchase_history, [order])

    def test_add_purchase_multiple(self):
        customer = Customer("Ada")
        o1, o2 = Order(), Order()
        customer.add_purchase(o1)
        customer.add_purchase(o2)
        self.assertEqual(customer.purchase_history, [o1, o2])


if __name__ == "__main__":
    unittest.main()