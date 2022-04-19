#!/usr/bin/env python3

import sys


def factorization(number):
    factors = []
    factor = 2

    while number > 1:
        if number % factor == 0:
            factors.append(factor)
            number //= factor
        else:
            factor += 1

    return factors


def main(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()

    all_factors = set()
    for line in lines:
        number = int(line)
        print(f"Factoring {number}: ", end="")

        factors = factorization(number)
        print(factors)
        all_factors.update(set(factors))

    sorted_factors = sorted(all_factors)
    n = sorted_factors[5] * sorted_factors[-1]
    flag = n.to_bytes((n.bit_length() + 7) // 8 , "little")
    print("flagga{" + flag.hex() + "}")

    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(main(sys.argv[1]))

