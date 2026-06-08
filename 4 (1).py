from itertools import permutations

def solve_cryptarithmetic():
    letters = "SENDMORY"

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        S = mapping['S']
        E = mapping['E']
        N = mapping['N']
        D = mapping['D']
        M = mapping['M']
        O = mapping['O']
        R = mapping['R']
        Y = mapping['Y']

        if S == 0 or M == 0:
            continue

        SEND = 1000*S + 100*E + 10*N + D
        MORE = 1000*M + 100*O + 10*R + E
        MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

        if SEND + MORE == MONEY:
            print("Solution Found:")
            print("SEND =", SEND)
            print("MORE =", MORE)
            print("MONEY =", MONEY)
            print("Mapping:", mapping)
            return

    print("No solution found.")


solve_cryptarithmetic()