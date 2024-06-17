import math


def calculate_delta(a, b, c):
    delta = b**2 - (4 * a * c)
    return delta


def main():
    delta = calculate_delta(3, 6, 2)
    print(delta)


if __name__ == "__main__":
    main()
