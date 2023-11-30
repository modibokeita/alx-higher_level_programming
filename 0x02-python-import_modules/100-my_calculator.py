if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    opsys = sys.argv[2]
    if opsys != '+' and opsys != '-' and opsys != '*' and opsys != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if opsys == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif opsys == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif opsys == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
