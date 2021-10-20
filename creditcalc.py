from math import ceil, log, pow
import argparse


msg_error_default = "Incorrect parameters"


def calc_principal(a, n, i):
    return a / ((i / 1200) * pow(1 + i / 1200, n) / (pow(1 + i / 1200, n) - 1))


def calc_payment(p, n, i):
    return p * (i / 1200) * pow(1 + i / 1200, n) / (pow(1 + i / 1200, n) - 1)


def calc_periods(a, p, i):
    return log(a / (a - (i / 1200) * p), 1 + i / 1200)


def print_annuity(principal=0, payment=0, periods=0, interest=0):
    if not principal:
        principal = round(calc_principal(payment, periods, interest))
        print(f"Your loan principal = {principal}!")
    if not payment:
        payment = ceil(calc_payment(principal, periods, interest))
        print(f"Your annuity payment = {payment}!")
    if not periods:
        periods = ceil(calc_periods(payment, principal, interest))
        years, months = periods // 12, periods % 12
        print("It will take", f"{years} {'year' if years == 1 else 'years'}"*bool(years), "and"*bool(years)*bool(months),
              f"{months} {'month' if months == 1 else 'months'}"*bool(months), "to repay this loan!")
    print(f"Overpayment = {payment * periods - principal}")


def calc_differentiated(p, n, i, m):
    return p / n + i / 1200 * (p - (p * (m - 1)) / n)


def print_differentiated(principal, periods, interest):
    acc = 0
    for i in range(1, periods + 1):
        dm = ceil(calc_differentiated(principal, periods, interest, i))
        acc += dm
        print(f"Month {i}: payment is {dm}")
    print()
    print(f"Overpayment = {acc - principal}")
        

parser = argparse.ArgumentParser(description="Loan calculator for annuity and differentiated payments")
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()
if len(vars(args)) != 5:
    print(msg_error_default)
elif not args.type:
    print(msg_error_default)
elif not args.interest:
    print(msg_error_default)
elif args.payment and args.payment < 0 or args.principal and args.principal < 0 or args.periods and args.periods < 0 or args.interest and args.interest < 0:
    print(msg_error_default)
elif args.type == 'diff':
    if args.payment or (not args.principal and not args.periods):
        print(msg_error_default)
    else:
        print_differentiated(args.principal, args.periods, args.interest)
elif args.type == 'annuity':
    print_annuity(args.principal, args.payment, args.periods, args.interest)
