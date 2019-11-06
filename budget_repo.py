from abc import ABCMeta, abstractmethod


class BudgetRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    def findAll(self):
        pass
