# membuat class abstract
# abc = abstract base class
from abc import ABC, abstractmethod

# Class Button
class Button(ABC):

    def __init__(self, set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass

# Class PushButton
class PushButton(Button):

    def click(self):
        print("Go to: ", self.link)

    @Button.link.setter
    def link(self, input):
        self.__link = input

    @link.getter
    def link(self):
        return self.__link

tombol1 = PushButton("www.danu-portfolio.com")

tombol1.click()