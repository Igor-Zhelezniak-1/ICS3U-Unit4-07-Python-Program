#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is math_program


def main():
    loop_counter = 1000

    # process & output
    for loop_counter in range(1000, 2001):
        if loop_counter % 5 == 4:
            print(loop_counter, "")
        else:
            print(loop_counter, "", end="")
        loop_counter = loop_counter + 1
    print("Done.")


if __name__ == "__main__":
    main()
