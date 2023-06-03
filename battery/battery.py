from abc import ABC, abstractmethod


class Battery(ABC):

    @abstractmethod
    def need_service(self):
        pass
