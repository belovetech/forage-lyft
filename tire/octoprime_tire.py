from tire.tire import Tire

WEAR_THRESHOLD = 3


class OctoprimeTire(Tire):
    def __init__(self, tire_wears) -> None:
        self.tire_wears = tire_wears

    def needs_service(self):
        return sum(self.tire_wears) >= WEAR_THRESHOLD
