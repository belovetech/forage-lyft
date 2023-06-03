from tire.tire import Tire

WEAR_THRESHOLD = 0.9


class CarriganTire(Tire):
    def __init__(self, tire_wears) -> None:
        self.tire_wears = tire_wears

    def needs_service(self):
        for wear in self.tire_wears:
            if wear >= WEAR_THRESHOLD:
                return True
        return False
