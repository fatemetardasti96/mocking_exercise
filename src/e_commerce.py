class ProductCatalog:
    def get_product_price(self, product_id):
        # Simulate fetching product prices from a catalog
        # In a real scenario, this would involve database queries or external API calls
        raise NotImplementedError("This method should be implemented in a real ProductCatalog")

class DiscountService:
    def apply_discount(self, total_price):
        # Simulate applying discounts based on certain criteria
        # In a real scenario, this would involve more complex business logic
        raise NotImplementedError("This method should be implemented in a real DiscountService")

class ShoppingCart:
    def __init__(self, product_catalog: ProductCatalog, discount_service: DiscountService):
        self.product_catalog = product_catalog
        self.discount_service = discount_service
        self.items = []

    def add_item(self, product_id, quantity):
        price = self.product_catalog.get_product_price(product_id)
        self.items.append({"product_id": product_id, "quantity": quantity, "price": price})

    def calculate_total_price(self):
        total_price = sum(item["price"] * item["quantity"] for item in self.items)
        return total_price
