# strategy pattern

class PaymentContext:
    def __init__(self, payment):
        self.payment = payment

    def set_strategy(self, payment):
        self.payment = payment

    def execute_payment(self, amount):
        return self.payment.make_payment(amount)


class Payment:
    def make_payment(self, amount):
        raise NotImplementedError


class CreditCardPayment(Payment):
    def make_payment(self, amount):
        return f"cc: {amount}"


class PayPalPayment(Payment):
    def make_payment(self, amount):
        return f"pp: {amount}"


payment_context = PaymentContext(CreditCardPayment())
assert payment_context.execute_payment(100) == "cc: 100"

payment_context.set_strategy(PayPalPayment())
assert payment_context.execute_payment(200) == "pp: 200"
