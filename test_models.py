import unittest

from models import Customer, FoodItem, Menu, Order


class TestFoodItem(unittest.TestCase):
    def test_attributes(self):
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

    def test_add_item_grows_collection(self):
        menu = Menu()
        self.assertEqual(len(menu.items), 0)
        menu.add_item(self.soda)
        self.assertEqual(menu.items, [self.soda])

    def test_filter_by_category_matches(self):
        menu = Menu()
        for item in (self.soda, self.water, self.cake):
            menu.add_item(item)
        self.assertEqual(menu.filter_by_category("Drinks"), [self.soda, self.water])

    def test_filter_by_category_no_match(self):
        menu = Menu()
        menu.add_item(self.soda)
        menu.add_item(self.water)
        self.assertEqual(menu.filter_by_category("Desserts"), [])


class TestOrder(unittest.TestCase):
    def test_compute_total_empty_order(self):
        self.assertEqual(Order().compute_total(), 0.0)

    def test_compute_total_sums_prices(self):
        burger = FoodItem("Spicy Burger", 8.50, "Mains", 4.7)
        soda = FoodItem("Large Soda", 2.00, "Drinks", 4.0)
        order = Order()
        order.add_item(burger)
        order.add_item(soda)
        self.assertEqual(order.compute_total(), 10.50)

    def test_add_item_grows_order(self):
        burger = FoodItem("Spicy Burger", 8.50, "Mains", 4.7)
        order = Order()
        order.add_item(burger)
        self.assertEqual(order.items, [burger])


class TestCustomer(unittest.TestCase):
    def test_new_customer_has_no_history(self):
        self.assertEqual(Customer("Alex").purchase_history, [])

    def test_add_purchase_records_order(self):
        customer = Customer("Alex")
        order = Order()
        customer.add_purchase(order)
        self.assertEqual(customer.purchase_history, [order])
        self.assertEqual(len(customer.purchase_history), 1)


if __name__ == "__main__":
    unittest.main()