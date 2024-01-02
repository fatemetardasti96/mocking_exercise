from unittest.mock import Mock


class PaymentGateway:
    def process_transaction(self, amount, card_number):
        # Simulate processing a transaction with a payment gateway
        # In a real scenario, this would involve communication with an external payment service
        raise NotImplementedError("This method should be implemented in a real PaymentGateway")


class PaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount, card_number):
        # Validate the card number (a simplified validation for illustration purposes)
        if not card_number or not card_number.isdigit():
            raise ValueError("Invalid card number")

        # Process the payment using the payment gateway
        transaction_result = self.payment_gateway.process_transaction(amount, card_number)
        return f"Payment processed successfully. Transaction ID: {transaction_result}"


