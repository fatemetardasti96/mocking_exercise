from unittest.mock import Mock
import pytest

from src.payment import PaymentProcessor, PaymentGateway

def test_payment_processor():
    gateway = Mock()
    gateway.process_transaction.return_value = 10637

    assert PaymentProcessor(gateway).process_payment(10, '6037') == f"Payment processed successfully. Transaction ID: 10637"
    
def test_raise_error():

    with pytest.raises(ValueError, match="Invalid card number"):
        PaymentProcessor(PaymentGateway()).process_payment(10, '6037fghjk')
    
    