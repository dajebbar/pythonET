import sys
import argparse


def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        try:
            return args.x / args.y
        except ZeroDivisionError:
            return f'Error! {y} must be different of zero.'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', 
                        type=float, 
                        default=1.0, 
                        help='What is the first number?'
                        )
    parser.add_argument('--y', 
                        type=float, 
                        default=1.0, 
                        help='What is the second number?'
                        )
    parser.add_argument('--operation', 
                        type=str, 
                        default='add', 
                        help='What operation? Can choose add, sub, mul, or div'
                        )
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

if __name__=='__main__':
    main()

# operation = 'mul'
# print(calc(5, 5, operation))