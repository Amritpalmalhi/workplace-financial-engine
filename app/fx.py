class FXRateLock:
    def __init__(self, rate: float):
        self.rate = rate

    def convert(self, amount: float):
        return amount * self.rate
