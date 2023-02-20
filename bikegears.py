#!/usr/bin/env python3

import argparse

chainring = {
    '40':    [40],
    '42':    [42],
    '44':    [44],
    '50':    [50],
    '46/36': [36,46],
    '50/34': [34,50],
    '52/36': [36,52]
}

cassette = {
    '8-25': [11, 13, 15, 17, 19, 21, 23, 25],
    '25':   [11, 12, 13, 14, 15, 16, 17, 19, 21, 23, 25],
    '26':   [11, 12, 13, 14, 15, 16, 17, 19, 21, 23, 26],
    '28':   [11, 12, 13, 14, 15, 16, 17, 19, 22, 25, 28],
    '32':   [11, 12, 13, 14, 15, 17, 19, 22, 25, 28, 32],
    '36':   [11, 12, 13, 15, 17, 19, 22, 25, 28, 32, 36],
    '42':   [11, 13, 15, 17, 19, 22, 25, 28, 32, 36, 42]
}

wheel = 0.0

def gearinches(cr, cs, wheel):
    return round(cr/cs*wheel, 2)

def speedMPH(cr, cs, wheel, rpm):
    gi = gearinches(cr, cs, wheel)
    return round( (gi*rpm)/336 , 2 )

parser = argparse.ArgumentParser()
parser.add_argument(
    "wheel_Size",
    type=str,
    help="Size of your wheels; either in inches or "
)
parser.add_argument(
    "your_Chainring",
    type=str,
    help="What is your chainring size(s)"
)
parser.add_argument(
    "your_Cassette",
    type=str,
    help="What is your cassette size"
)
args = parser.parse_args()

print("Hello!\nYour wheel is %s, your chainring is %s, and your cassette is %s" % (args.wheel_Size, args.your_Chainring, args.your_Cassette))

if not args.wheel_Size.isdigit():
    print("Your Wheel has a letter")
    wheel = float(args.wheel_Size[:-1])
    wheel = float(wheel)*0.0393701
    print(wheel)
else:
    wheel = float(args.wheel_Size)

print("Your gear inch table is:\n\n\t", end="")

for cs in cassette[args.your_Cassette]:
    print(str(cs) + "\t", end="")
print("\n")
for cr in chainring[args.your_Chainring]:
    print(str(cr) + ":\t", end="")
    for cs in cassette[args.your_Cassette]:
        print(speedMPH(cr, cs, wheel, 100), end="\t")
    print("\n")
