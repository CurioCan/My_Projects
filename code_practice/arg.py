import argparse
import sys


def main():
    parser = argparse.ArgumentParser()

    # -- is a flag which says it as an optional argument as positional arguments can not have
    # default value
    parser.add_argument('--x', type=float, default=10.0,
                        help="What is the first number?")
    parser.add_argument('--y', type=float, default=20.0,
                        help="What is the second nmber?")
    parser.add_argument('--operation', type=str, default="add",
                        help="What is the operation (add or sub or mul or div)")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)) + "\n")


def calc(args):
    x = args.x
    y = args.y
    op = args.operation

    if op == "add":
        return x + y
    elif op == "sub":
        return x - y
    elif op == "mul":
        return x * y
    elif op == "div":
        return x / y
    else:
        raise ValueError(f"Invalid operation: {op}. Use add, sub, mul or div.")

if __name__ == "__main__":
    main()

# ~/PycharmProjects/pYthon/Udemy_/code_practice$ python3 arg.py --x=20 --y=30 --operation=sub
# -10.0
# (base) charitha@charitha-IdeaPad-Slim-3-15IRH8:~/PycharmProjects/pYthon/Udemy_/code_practice$ python3 arg.py -h
# usage: arg.py [-h] [--x X] [--y Y] [--operation OPERATION]
#
# options:
#   -h, --help            show this help message and exit
#   --x X                 What is the first number?
#   --y Y                 What is the second number?
#   --operation OPERATION
#                         What is the operation (add or sub or mul or div)
