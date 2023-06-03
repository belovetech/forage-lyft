from battery.battery import Battery

SERVICE_YEAR_DURATION = 3


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + SERVICE_YEAR_DURATION)
        return service_threshold_date < self.current_date
