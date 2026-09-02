# Cryptarithmetic Problem
# SEND + MORE = MONEY

from itertools import permutations

def solve_cryptarithmetic():
    letters = 'SENDMORY'

    # Try all possible digit combinations
    for digits in permutations(range(10), len(letters)):

        # Assign digits to letters
        S, E, N, D, M, O, R, Y = digits

        # First letters cannot be zero
        if S == 0 or M == 0:
            continue

        # Form the numbers
        SEND = 1000*S + 100*E + 10*N + D
        MORE = 1000*M + 100*O + 10*R + E
        MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

        # Check the equation
        if SEND + MORE == MONEY:
            print("Solution found:")
            print("SEND  =", SEND)
            print("MORE  =", MORE)
            print("MONEY =", MONEY)
            print()
            print(SEND, "+", MORE, "=", MONEY)
            return

    print("No solution found.")


solve_cryptarithmetic()
