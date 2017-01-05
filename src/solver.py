import math


class Solver:
    def demo():
        a = int(input("a "))
        b = int(input("b "))
        c = int(input("c "))
        d = abs(b ** 2 - 4 * a * c)
        disc = math.sqrt(d)
        print(disc)


Solver.demo()