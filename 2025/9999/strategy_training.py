# strategy pattern

class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError()


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"cc: {amount}"


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"pp: {amount}"


class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        return self._strategy.pay(amount)


payment_context = PaymentContext(CreditCardPayment())
assert payment_context.execute_payment(100) == "cc: 100"

payment_context.set_strategy(PayPalPayment())
assert payment_context.execute_payment(200) == "pp: 200"
