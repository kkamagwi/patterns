
# coding: utf-8

"""
Стратегия (Strategy) - делает семейство алгоритмов взаимозаменяемыми.
Стратегия позволяет изменять алгоритмы независимо от клиентов, которые ими пользуются.
"""

class StrategyExample:
    def __init__(self, func=None):
        if func:
             self.execute = func

    def execute(self):
        print("Original text")

def executeReplacement1():
    print("First replacement")

def executeReplacement2():
    print("Second replacement")

if __name__ == "__main__":
    se0 = StrategyExample()
    se1 = StrategyExample(executeReplacement1)
    se2 = StrategyExample(executeReplacement2)

    se0.execute() # Original text
    se1.execute() # First replacement
    se2.execute() # Second replacement
