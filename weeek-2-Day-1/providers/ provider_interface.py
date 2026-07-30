from abc import ABC, abstractmethod


class Provider(ABC):
    """
    Base provider class.

    Every AI provider should inherit this class.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from the model.
        """
        pass