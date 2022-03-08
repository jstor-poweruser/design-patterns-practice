from abc import ABC, abstractmethod


class Beverage(ABC):
    """Here's the base class for a beverage"""
    def __init__(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod:
    def cost(self):
        pass
