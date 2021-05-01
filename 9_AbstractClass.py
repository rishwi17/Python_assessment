import abc
from abc import ABC, abstractmethod


class AbstractClass (ABC):

    @abstractmethod
    def abstractFunc(self):
        pass

    def concreteFunc(self):
        print('This is the concreteFunc')


class MyClass(AbstractClass):
    def abstractFunc(self):
        print('abstract func')


obj = MyClass()

obj.abstractFunc()
obj.concreteFunc()
