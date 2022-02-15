# Simlple script to determine amount of agrobaceria suspended in
# media to add into wt cells for transformation

import sys


def print_help():
    print("OD calculator script by Jake Landers")
    print(
        "Input the OD concentration recieved with a 1:100 dilutiion of 600 wavelength"
    )
    print("USAGE:")
    print("python od_transformation.py (OD value)")
    print("-h to print this screen")


if len(sys.argv) < 2:
    print("ERROR: There were no arguments passed")
    print_help()
    exit(1)

try:
    arg1 = sys.argv[1]
    if arg1 == "-h":
        print_help()
        exit(0)
    od = float(arg1)

    ml = (0.5 / od) * 100

    print(
        "Put {}mL of agrobacteria into wt cells suspended in 10mL of media".format(
            int(ml)
        )
    )
    exit(0)
except Exception as error:
    print("Please make sure the provided OD is in number format.")
    exit(1)

