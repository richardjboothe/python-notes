# This coding exercise requires you to complete an implementation of three methods of a class:
#
# 1. The __init__ method, which should take an argument, name.
#  	It should initialise self.name to be the argument, and self.items to be an empty list.
# 2. The add_item  method, which should append a dictionary representing an item to the
# store's items  property. The dictionary should have keys name  and price .
# 3. The stock_price method, which should add up each item price inside self.items
# to come up with a total, and return that.
# Good luck!


class Store:
	def __init__(self, name):
		self.name = name
		self.items = []

	def add_item(self, name, price):
		self.items.append({
			'name': name,
			'price': price
		})

	def stock_price(self):
		return sum([item['price'] for item in self.items])
