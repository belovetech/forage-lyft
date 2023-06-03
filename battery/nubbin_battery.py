from battery.battery import Battery

SERVICE_DURATION = 2


class NubbinBattery(Battery):
    def __init__(self, last_service, current_date):
        self.last_service = last_service
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + SERVICE_DURATION)
        return service_threshold_date < self.current_date
