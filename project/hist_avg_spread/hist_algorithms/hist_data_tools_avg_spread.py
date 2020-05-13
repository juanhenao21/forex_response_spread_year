''' HIST data tools module.

The functions in the module do small repetitive tasks, that are used along the
whole implementation. These tools improve the way the tasks are standardized
in the modules that use them.

This script requires the following modules:
    * typing

The module contains the following functions:
    * hist_function_header_print_data - prints info about the function running.
    * hist_initial_message - prints the initial message with basic information.
    * hist_weeks - generates a tuple with the number of weeks in a year.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from typing import List, Tuple

# -----------------------------------------------------------------------------


def hist_function_header_print_data(function_name: str, fx_pair: str,
                                    year: str, week: str) -> None:
    """Prints a header of a function that generates data when it is running.

    :param function_name: name of the function that generates the data.
    :param year: string of the year to be analyzed (i.e '2016').
    :return: None -- The function prints a message and does not return a
     value.
    """

    print('HIST data')
    print(function_name)

    fx_pair_upper: str = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()
    print(f'Processing data for the forex pair {fx_pair_upper} in the week '
          + f'{week} of {year}')
    print()

# -----------------------------------------------------------------------------


def hist_initial_message() -> None:
    """Prints the initial message with basic information.

    :return: None -- The function prints a message and does not return a value.
    """

    print()
    print('###################')
    print('Hist Average Spread')
    print('###################')
    print('AG Guhr')
    print('Faculty of Physics')
    print('University of Duisburg-Essen')
    print('Author: Juan Camilo Henao Londono')
    print('More information in:')
    print('* https://juanhenao21.github.io/')
    print('* https://github.com/juanhenao21/forex_response_spread_year')
    print('* https://forex-response_spread-year.readthedocs.io/en/latest/')
    print()

# -----------------------------------------------------------------------------


def hist_weeks() -> Tuple[str, ...]:
    """Generates a tuple with the numbers from 0 to 53 representing the weeks
       in a year.

    :return: tuple.
    """

    week_num: List[str] = []

    val: int
    for val in range(1, 54):
        if val < 10:
            val_str: str = f'0{val}'
            week_num.append(f'{val_str}')
        else:
            week_num.append(f'{val}')

    return tuple(week_num)

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
