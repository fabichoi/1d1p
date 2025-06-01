# strategy pattern

class PaymentContext:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def set_strategy(self, payment_method):
        self.payment_method = payment_method

    def execute_payment(self, amount):
        return self.payment_method.pay(amount)


class Payment:
    def pay(self, amount):
        raise NotImplementedError()


class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"cc: {amount}"


class PayPalPayment:
    def pay(self, amount):
        return f"pp: {amount}"


payment_context = PaymentContext(CreditCardPayment())
assert payment_context.execute_payment(100) == "cc: 100"

payment_context.set_strategy(PayPalPayment())
assert payment_context.execute_payment(200) == "pp: 200"
