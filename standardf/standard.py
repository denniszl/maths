"""
This file contains the complexity classes are that discussed most often
in classes, O(1), O(logn), O(n), and O(n^2). Eventually I'll add more, like
the inverse ackermann function once I figure out how to implement it without
crashing my machine...
"""
import math


def constant_time(n):
    return float(1)


def logarithmic_time(n):
    # I'm using 2 because I'm a programmer and I think in base 2.
    # Realistically you could use whatever you'd like.
    return math.log(n, 2)


def linear_time(n):
    return float(n)


def quadratic_time(n):
    # I've opted to call this quadratic because polynomial time would be a
    # misnomer, given I'm only going to be returning n^2.
    return float(n**2)


if __name__ == '__main__':
    ret = constant_time(4)
    print ret
    ret = logarithmic_time(4)
    print ret
    ret = linear_time(4)
    print ret
    ret = quadratic_time(4)
    print ret
