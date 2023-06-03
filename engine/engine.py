from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def need_service(self):
        pass
