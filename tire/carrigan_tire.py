from tire.tire import Tire

WEAR_THRESHOLD = 0.9


class CarriganTire(Tire):
    def __init__(self, wears) -> None:
        self.wears = wears

    def needs_service(self):
        for i in range(len(self.wears)):
            if self.wears[i] >= WEAR_THRESHOLD:
                return True
        return False
