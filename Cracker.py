from Crackers.ACracker import ACracker
from Crackers.BCracker import BCracker
from Crackers.CCracker import CCracker
from Crackers.DCracker import DCracker
from Crackers.ECracker import ECracker
from Crackers.Strategy import Strategy

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, encrypted_message, n, e):
        self._strategy.execute(encrypted_message, n, e)

if __name__ == "__main__":
    strategies = {'A': ACracker(), 'B': BCracker(), 'C': CCracker(), 'D': DCracker(), 'E': ECracker()}
    context = Context(None)

    for i in range(30):
        paket = input("\nEnter paket soal (A, B, C, D, E): ").upper()
        n = int(input("Input n: "))
        e = int(input("Input e: "))
        encrypted_message = int(input("Input encrypted message (c): "))

        if paket in strategies:
            context.set_strategy(strategies[paket])
            context.execute_strategy(encrypted_message, n, e)
        else:
            print("Invalid paket soal.")
