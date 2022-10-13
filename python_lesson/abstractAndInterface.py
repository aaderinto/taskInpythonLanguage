from abc import ABCMeta


import abc
class webElement(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def get_locator(self, locator):
        pass

class DivElement(webElement):

    def get_name(self):
        return "div"

    def get_locator(self, locator):
        return locator

class ButtonElement(webElement):
    def get_name(self):
        return "button"
    
    def get_locator(self, locator):
        return locator

div_Element = DivElement()
print(div_Element.get_name(), div_Element.get_locator("C#H"))


