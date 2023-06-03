from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def needs_service(self):
        """ Will be implemented by the engine type classes
        """
        pass
