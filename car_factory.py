from car import Car
from battery import spindler_battery, nubbin_battery
from engine import capulet_engine, sternman_engine, willoughby_engine


class CarFactory(Car):
    def create_calliope(self, current_date, last_service_date,
                        current_mileage, last_service_mileage) -> Car:
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = spindler_battery(current_date, last_service_date)
        return Car(engine, battery)

    def create_glissade(self, current_date, last_service_date,
                        current_mileage, last_service_mileage) -> Car:
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = spindler_battery(current_date, last_service_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on) -> Car:
        engine = sternman_engine(warning_light_on)
        battery = spindler_battery(current_date, last_service_date)
        return Car(engine, battery)

    def create_rorschach(self, current_date, last_service_date,
                         current_mileage, last_service_mileage) -> Car:
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = nubbin_battery(current_date, last_service_date)
        return Car(engine, battery)

    def create_thovex(self, current_date, last_service_date,
                      current_mileage, last_service_mileage) -> Car:
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = nubbin_battery(current_date, last_service_date)
        return Car(engine, battery)
