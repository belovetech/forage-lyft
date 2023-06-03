from abc import ABC, abstractmethod


class Battery(ABC):

    @abstractmethod
    def needs_service(self):
        """Interface!! it will be implmented by battery types
        """
        pass
