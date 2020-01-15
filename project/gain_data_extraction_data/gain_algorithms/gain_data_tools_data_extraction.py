'''ITCH data tools module.

The functions in the module do small repetitive tasks, that are used along the
whole implementation. These tools improve the way the tasks are standardized
in the modules that use them.

This script requires the following modules:
    * matplotlib
    * os
    * pickle

The module contains the following functions:
    * itch_save_data - saves computed data.
    * itch_save_plot - saves figures.
    * itch_function_header_print_data - prints info about the function running.
    * itch_function_header_print_plot - prints info about the plot.
    * itch_start_folders - creates folders to save data and plots.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from matplotlib import pyplot as plt
import os
import pickle

# -----------------------------------------------------------------------------


def itch_save_data(function_name, data, ticker_i, ticker_j, year, month, day):
    """Saves computed data in pickle files.

    Saves the data generated in the functions of the
    itch_data_analysis_data_extraction module in pickle files.

    :param function_name: name of the function that generates the data.
    :param data: data to be saved. The data can be of different types.
    :param ticker_i: string of the abbreviation of the stock to be analized
     (i.e. 'AAPL').
    :param ticker_j: string of the abbreviation of the stock to be analized
     (i.e. 'AAPL').
    :param year: string of the year to be analized (i.e '2016').
    :param month: string of the month to be analized (i.e '07').
    :param day: string of the day to be analized (i.e '07').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    # Saving data

    if (not os.path.isdir(
            f'../../itch_data/data_extraction_{year}/{function_name}/')):

        try:
            os.mkdir(
                f'../../itch_data/data_extraction_{year}/{function_name}/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    # Cross-response data
    if (ticker_i != ticker_j):

        pickle.dump(data, open(f'../../itch_data/data_extraction_{year}'
                    + f'/{function_name}/{function_name}_{year}{month}{day}'
                    + f'_{ticker_i}i_{ticker_j}j.pickle', 'wb'))

    # Self-response data
    else:

        pickle.dump(data, open(f'../../itch_data/data_extraction'
                    + f'_{year}/{function_name}/{function_name}_{year}{month}'
                    + f'{day}_{ticker_i}.pickle', 'wb'))

    print('Data Saved')
    print()

    return None

# -----------------------------------------------------------------------------


def itch_save_plot(function_name, figure, ticker_i, ticker_j, year, month):
    """Saves plot in png files.

    Saves the plot generated in the functions of the
    itch_data_plot_data_extraction module in png files.

    :param function_name: name of the function that generates the plot.
    :param figure: figure object that is going to be save.
    :param ticker_i: string of the abbreviation of the stock to be analized
     (i.e. 'AAPL').
    :param ticker_j: string of the abbreviation of the stock to be analized
     (i.e. 'AAPL').
    :param year: string of the year to be analized (i.e '2016').
    :param month: string of the month to be analized (i.e '07').
    :return: None -- The function save the plot in a file and does not return
     a value.
    """

    # Saving plot data

    if (not os.path.isdir(
            f'../../plots/itch_data_extraction_{year}/{function_name}/')):

        try:
            os.mkdir(f'../../plots/itch_data_extraction_{year}/'
                     + f'{function_name}/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    # Cross-response data
    if (ticker_i != ticker_j):

        figure.savefig(f'../../plots/itch_data_extraction_{year}/'
                       + f'{function_name}/{function_name}_{year}{month}'
                       + f'_{ticker_i}i_{ticker_j}j.png')

    # Self-response
    else:

        figure.savefig(f'../../plots/itch_data_extraction_{year}/'
                       + f'{function_name}/{function_name}_{year}{month}'
                       + f'_{ticker_i}i.png')

    print('Plot saved')
    print()

    return None

# -----------------------------------------------------------------------------


def itch_function_header_print_data(function_name, ticker_i, ticker_j, year,
                                    month, day):
    """Prints a header of a function that generates data when it is running.

    :param function_name: name of the function that generates the data.
    :param ticker_i: string of the abbreviation of the stock to be analized
     (i.e. 'AAPL').
    :param ticker_j: string of the abbreviation of the stock to be analized
     (i.e. 'AAPL').
    :param year: string of the year to be analized (i.e '2016').
    :param month: string of the month to be analized (i.e '07').
    :param day: string of the day to be analized (i.e '07').
    :return: None -- The function prints a message and does not return a
     value.
    """

    print('ITCH data')
    print(function_name)

    # Cross-response data
    if (ticker_i != ticker_j):
        print(f'Processing data for the stock i {ticker_i}  and stock j '
              + f'{ticker_j} the {year}.{month}.{day}')
    # Self-response data
    else:
        print(f'Processing data for the stock {ticker_i} the '
              + f'{year}.{month}.{day}')

    return None

# -----------------------------------------------------------------------------


def itch_function_header_print_plot(function_name, ticker_i, ticker_j, year,
                                    month, day):
    """Prints a header of a function that generates a plot when it is running.

    :param function_name: name of the function that generates the plot.
    :param ticker_i: string of the abbreviation of the stock to be analized
     (i.e. 'AAPL').
    :param ticker_j: string of the abbreviation of the stock to be analized
     (i.e. 'AAPL').
    :param year: string of the year to be analized (i.e '2016').
    :param month: string of the month to be analized (i.e '07').
    :param day: string of the day to be analized (i.e '07').
    :return: None -- The function prints a message and does not return a
     value.
    """

    print('ITCH data')
    print(function_name)

    # Cross-response data
    if (ticker_i != ticker_j):
        print(f'Processing plot for the stock i {ticker_i} and stock j '
              + f'{ticker_j} the {year}.{month}.{day}')
    # Self-response data
    else:
        print(f'Processing plot for the stock {ticker_i} the '
              + f'{year}.{month}.{day}')

    return None

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
