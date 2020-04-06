''' HIST data tools module.

The functions in the module do small repetitive tasks, that are used along the
whole implementation. These tools improve the way the tasks are standardized
in the modules that use them.

This script requires the following modules:
    * matplotlib
    * numpy
    * os
    * pandas
    * pickle

The module contains the following functions:
    * hist_function_header_print_data - prints info about the function running.
    * hist_initial_data - takes the initial values for the analysis.
    * hist_weeks - list with the number of weeks in a year.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle

# -----------------------------------------------------------------------------


def hist_function_header_print_data(function_name, fx_pair, year, week):
    """Prints a header of a function that generates data when it is running.

    :param function_name: name of the function that generates the data.
    :param year: string of the year to be analyzed (i.e '2016').
    :return: None -- The function prints a message and does not return a
     value.
    """

    print('HIST data')
    print(function_name)

    fx_pair_upper = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()
    print(f'Processing data for the forex pair {fx_pair_upper} in the week '
          + f'{week} of {year}')
    print()

    return None

# -----------------------------------------------------------------------------


def hist_initial_data():
    """Takes the initial values for the analysis

    :return: String -- The function returns a string with the year to be
     analyzed.
    """

    print()
    print('##############')
    print('Average Spread')
    print('##############')
    print('AG Guhr')
    print('Faculty of Physics')
    print('University of Duisburg-Essen')
    print('Author: Juan Camilo Henao Londono')
    print('More information in:')
    print('  * https://juanhenao21.github.io/')
    print('  * https://github.com/juanhenao21/spread_impact_analysis')
    print('  * https://spread-impact-analysis.readthedocs.io/en/latest/')
    print()

    print('Please enter the year to be analyzed (i.e. 2008): ')
    year = input()
    print()

    return year

# -----------------------------------------------------------------------------


def hist_weeks():
    """Generates a list with the number of weeks in a year.

    :return: list.
    """

    week_num = []

    for val in range(1, 54):
        if (val < 10):
            val = f'0{val}'
        week_num.append(f'{val}')

    return week_num

# -----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

    pass

    return None

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
