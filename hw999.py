"""The task is: Make a python program which can take a csv file of this
 structure and print on the screen solved 9x9 sudoku. The rules are:

    CSV input: e.g. A1;A2;A3;B3;17 means the sum of fields A1+A2+A3+B3 = 17
    The numbers in one sum are always unique.
    The rules for sudoku are numbers are from 1 to 9 and are unique
    in every 3x3 square and in all rows and all columns.
"""

from killer_sudoku import Killer_sudoku
import timeit
import sys


def main(path):
    """Killer Sudoku"""

    sudoku = Killer_sudoku()
    try:
        sudoku.readCSV(path)
    except Exception as e:
        print("\nError reading file. Did you inform correctly?\n")
        return False

    print("\nTrying to find the solution to the Killer Sudoku...\n")

    start = timeit.default_timer()
    try:
        message = sudoku.solver()
    except Exception as e:
        print("\nError during execution. Are your file in the correct format?\n")
        return False
    stop = timeit.default_timer()

    if(message == "Complete"):
        print(sudoku)
        print("Total running time: " + str(stop - start) + " seconds\n")
    else:
        print("It did not find a solution. Are your file in the correct format?")


if(__name__ == "__main__"):
    try:
        path = sys.argv[1]
        main(path)
    except Exception as e:
        print("\nError: You did not inform a file\n")
