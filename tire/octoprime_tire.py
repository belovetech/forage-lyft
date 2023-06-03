from tire.tire import Tire

WEAR_THRESHOLD = 3


class OctoprimeTire(Tire):
    def __init__(self, wears) -> None:
        self.wears = wears

    def needs_service(self):
        _sum = 0
        for i in range(len(self.wears)):
            _sum += self.wears[i]
        return _sum >= WEAR_THRESHOLD
