# strategy pattern

class PaymentContext:
    pass

class Payment:
    pass

class CreditCardPayment:
    pass

class PayPalPayment:
    pass







payment_context = PaymentContext(CreditCardPayment())
assert payment_context.execute_payment(100) == "cc: 100"

payment_context.set_strategy(PayPalPayment())
assert payment_context.execute_payment(200) == "pp: 200"

