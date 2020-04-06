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
    * hist_save_data - saves computed data.
    * hist_save_plot - saves figures.
    * hist_function_header_print_data - prints info about the function running.
    * hist_function_header_print_plot - prints info about the plot.
    * hist_start_folders - creates folders to save data and plots.
    * hist_initial_data - takes the initial values for the analysis.
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


def hist_save_data(function_name, data, fx_pair, year, week):
    """ Saves computed data in pickle files.

    Saves the data generated in the functions of the
    hist_data_analysis_avg_responses_physical module in pickle files.

    :param function_name: name of the function that generates the data.
    :param data: data to be saved. The data can be of different types.
    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e '2016').
    :param week: string of the week to be analyzed (i.e '07').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    # Saving data

    if (not os.path.isdir(f'../../hist_data/avg_responses_data_{year}/'
                          + f'{function_name}/')):

        try:
            os.mkdir(f'../../hist_data/avg_responses_data_{year}/'
                     + f'{function_name}/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    pickle.dump(data, open(f'../../hist_data/avg_responses_data_{year}/'
                + f'{function_name}/{function_name}_{year}{week}_{fx_pair}'
                + f'.pickle', 'wb'))

    print('Data Saved')
    print()

    return None

# -----------------------------------------------------------------------------


def hist_save_plot(function_name, figure, fx_pair, year):
    """Saves plot in png files.

    Saves the plot generated in the functions of the
    hist_data_plot_avg_responses_physical module in png files.

    :param function_name: name of the function that generates the plot.
    :param figure: figure object that is going to be save.
    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
    :param year: string of the year to be analyzed (i.e '2016').
    :return: None -- The function save the plot in a file and does not return
     a value.
    """

    # Saving plot data

    if (not os.path.isdir(f'../../hist_plot/avg_responses_plot_{year}'
                          + f'/{function_name}/')):

        try:
            os.mkdir(f'../../hist_plot/avg_responses_plot_{year}/'
                     + f'{function_name}/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    figure.savefig(f'../../hist_plot/avg_responses_plot_{year}/{function_name}'
                    + f'/{function_name}_{year}_{fx_pair}.png')

    print('Plot saved')
    print()

    return None

# -----------------------------------------------------------------------------


def hist_function_header_print_data(function_name, fx_pair, year, week):
    """Prints a header of a function that generates data when it is running.

    :param function_name: name of the function that generates the data.
    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e '2016').
    :param week: string of the week to be analyzed (i.e '07').
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


def hist_function_header_print_plot(function_name, fx_pair, year):
    """Prints a header of a function that generates a plot when it is running.

    :param function_name: name of the function that generates the plot.
    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e '2016').
    :return: None -- The function prints a message and does not return a
     value.
    """

    print('HIST data')
    print(function_name)

    fx_pair_upper = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()
    print(f'Processing plot for the forex pair {fx_pair_upper} the {year}')
    print()

    return None

# -----------------------------------------------------------------------------


def hist_start_folders(year):
    """Creates the initial folders to save the data and plots.

    :param year: string of the year to be analyzed (i.e '2016').
    :return: None -- The function creates folders and does not return a value.
    """

    try:
        os.mkdir(f'../../hist_data/avg_responses_data_{year}')
        os.mkdir(f'../../hist_plot/avg_responses_plot_{year}')

        print('Folder to save data created')
        print()

    except FileExistsError as e:
        print('Folder exists. The folder was not created')
        print(e)
        # raise Exception('Check the folders')

    return None

# -----------------------------------------------------------------------------


def hist_initial_data():
    """Takes the initial values for the analysis

    :return: None -- The function prints the message and does not return a
     value.
    """

    print()
    print('##################################')
    print('Average Response Function Analysis')
    print('##################################')
    print('AG Guhr')
    print('Faculty of Physics')
    print('University of Duisburg-Essen')
    print('Author: Juan Camilo Henao Londono')
    print('More information in:')
    print('  * https://juanhenao21.github.io/')
    print('  * https://github.com/juanhenao21/forex')
    print('  * https://forex.readthedocs.io/en/latest/')
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
