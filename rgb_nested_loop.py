#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Jan 21, 2022
# This program uses a nested loop to
# display RGB color codes


def main():
    # declare variables
    counter1 = 0
    counter2 = 0
    counter3 = 0

    # loop to increment counters
    for counter1 in range(51):
        for counter2 in range(51):
            for counter3 in range(51):
                print("RGB: {}, {}, {}". format(counter1, counter2, counter3))


if __name__ == "__main__":
    main()
