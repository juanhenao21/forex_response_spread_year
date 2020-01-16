'''GAIN data tools module.

The functions in the module do small repetitive tasks, that are used along the
whole implementation. These tools improve the way the tasks are standardized
in the modules that use them.

This script requires the following modules:
    * matplotlib
    * os
    * pickle

The module contains the following functions:
    * gain_save_data - saves computed data.
    * gain_save_plot - saves figures.
    * gain_function_header_print_data - prints info about the function running.
    * gain_function_header_print_plot - prints info about the plot.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from matplotlib import pyplot as plt
import os
import pickle

# -----------------------------------------------------------------------------


def gain_save_data(function_name, data, fx_pair, year, month):
    """Saves computed data in pickle files.

    Saves the data generated in the functions of the
    gain_data_analysis_data_extraction module in pickle files.

    :param function_name: name of the function that generates the data.
    :param data: data to be saved. The data can be of different types.
    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e '2016').
    :param month: string of the month to be analized (i.e '07').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    # Saving data

    if (not os.path.isdir(
            f'../../gain_data/data_extraction_{year}/{function_name}/')):

        try:
            os.mkdir(
                f'../../gain_data/data_extraction_{year}/{function_name}/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    pickle.dump(data, open(f'../../gain_data/data_extraction_{year}'
                + f'/{function_name}/{function_name}_{year}_{fx_pair}.pickle',
                'wb'))

    print('Data Saved')
    print()

    return None

# -----------------------------------------------------------------------------


def gain_save_plot(function_name, figure, fx_pair, year, month):
    """Saves plot in png files.

    Saves the plot generated in the functions of the
    gain_data_plot_data_extraction module in png files.

    :param function_name: name of the function that generates the plot.
    :param figure: figure object that is going to be save.
    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e '2016').
    :param month: string of the month to be analized (i.e '07').
    :return: None -- The function save the plot in a file and does not return
     a value.
    """

    # Saving plot data

    if (not os.path.isdir(
            f'../../gain_plot/gain_data_extraction_{year}/{function_name}/')):

        try:
            os.mkdir(f'../../gain_plot/gain_data_extraction_{year}/'
                     + f'{function_name}/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    figure.savefig(f'../../plots/gain_data_extraction_{year}/{function_name}'
                   + f'/{function_name}_{year}{month}_{ticker_i}i.png')

    print('Plot saved')
    print()

    return None

# -----------------------------------------------------------------------------


def gain_function_header_print_data(function_name, fx_pair, year, month):
    """Prints a header of a function that generates data when it is running.

    :param function_name: name of the function that generates the data.
    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e '2016').
    :param month: string of the month to be analized (i.e '07').
    :param day: string of the day to be analized (i.e '07').
    :return: None -- The function prints a message and does not return a
     value.
    """

    print('GAIN data')
    print(function_name)

    fx_pair_upper = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()
    print(f'Processing data for the forex pair {fx_pair_upper} the '
          + f'{year}.{month}')
    print()

    return None

# -----------------------------------------------------------------------------


def gain_function_header_print_plot(function_name, fx_pair, year, month):
    """Prints a header of a function that generates a plot when it is running.

    :param function_name: name of the function that generates the plot.
    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e '2016').
    :param month: string of the month to be analized (i.e '07').
    :param day: string of the day to be analized (i.e '07').
    :return: None -- The function prints a message and does not return a
     value.
    """

    print('GAIN data')
    print(function_name)

    fx_pair_upper = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()
    print(f'Processing plot for the forex pair {fx_pair_upper} the '
          + f'{year}.{month}')
    print()

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
