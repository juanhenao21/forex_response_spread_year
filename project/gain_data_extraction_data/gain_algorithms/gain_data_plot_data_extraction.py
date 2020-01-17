'''GAIN data plot module.

The functions in the module plot the data obtained in the
gain_data_analysis_data_extraction module.

This script requires the following modules:
    * matplotlib
    * pickle
    * gain_data_tools_data_extract

The module contains the following functions:
    * gain_fx_quotes_year_plot - plots the forex quotes for a year.
    * gain_fx_midpoint_year_plot - plots the forex quotes for a year.
    * gain_fx_spread_year_plot - plots the forex quotes for a year.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# ----------------------------------------------------------------------------
# Modules

from matplotlib import pyplot as plt
import pickle

import gain_data_tools_data_extraction

# ----------------------------------------------------------------------------


def gain_fx_quotes_year_plot(fx_pair, year):
    """Plots the quotes price for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e. '2016').
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        function_name = gain_fx_quotes_year_plot.__name__
        gain_data_tools_data_extraction \
            .gain_function_header_print_plot(function_name, fx_pair, year, '')
        fx_pair_upper = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()

        figure = plt.figure(figsize=(16, 9))

        # Load data
        fx_data = pickle.load(open(
                        f'../../gain_data/data_extraction_{year}/gain_fx_year'
                        + f'_extract_data/gain_fx_year_extract_data_{year}'
                        + f'_{fx_pair}.pickle', 'rb'))

        plt.plot(fx_data['RateBid'], linewidth=5, label='Bid')
        plt.plot(fx_data['RateAsk'], linewidth=5, label='Ask')
        plt.legend(loc='best', fontsize=25)
        plt.title(f'GAIN quotes price - {fx_pair_upper}', fontsize=40)
        plt.xlabel(r'Time $[s]$', fontsize=35)
        plt.ylabel(r'Quotes $[\$]$', fontsize=35)
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)
        plt.grid(True)
        plt.tight_layout()

        # Plotting
        gain_data_tools_data_extraction \
            .gain_save_plot(function_name, figure, fx_pair, year, '')

        del fx_data
        del figure

        return None

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        return None

# ----------------------------------------------------------------------------


def gain_fx_midpoint_year_plot(fx_pair, year):
    """Plots the midpoint price for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e. '2016').
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        function_name = gain_fx_midpoint_year_plot.__name__
        gain_data_tools_data_extraction \
            .gain_function_header_print_plot(function_name, fx_pair, year, '')
        fx_pair_upper = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()

        figure = plt.figure(figsize=(16, 9))

        # Load data
        fx_data = pickle.load(open(
                        f'../../gain_data/data_extraction_{year}/gain_fx_year'
                        + f'_extract_data/gain_fx_year_extract_data_{year}'
                        + f'_{fx_pair}.pickle', 'rb'))

        plt.plot((fx_data['RateBid'] + fx_data['RateAsk'] ) / 2, linewidth=5)
        plt.title(f'GAIN midpoint price - {fx_pair_upper}', fontsize=40)
        plt.xlabel(r'Time $[s]$', fontsize=35)
        plt.ylabel(r'$m(t) [\$]$', fontsize=35)
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)
        plt.grid(True)
        plt.tight_layout()

        # Plotting
        gain_data_tools_data_extraction \
            .gain_save_plot(function_name, figure, fx_pair, year, '')

        del fx_data
        del figure

        return None

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        return None

# ----------------------------------------------------------------------------


def gain_fx_spread_year_plot(fx_pair, year):
    """Plots the spread for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e. '2016').
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        function_name = gain_fx_spread_year_plot.__name__
        gain_data_tools_data_extraction \
            .gain_function_header_print_plot(function_name, fx_pair, year, '')
        fx_pair_upper = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()

        figure = plt.figure(figsize=(16, 9))

        # Load data
        fx_data = pickle.load(open(
                        f'../../gain_data/data_extraction_{year}/gain_fx_year'
                        + f'_extract_data/gain_fx_year_extract_data_{year}'
                        + f'_{fx_pair}.pickle', 'rb'))

        plt.plot(fx_data['RateAsk'][::100] - fx_data['RateBid'][::100],
                 linewidth=5)
        plt.title(f'GAIN spread price - {fx_pair_upper}', fontsize=40)
        plt.xlabel(r'Time $[s]$', fontsize=35)
        plt.ylabel(r'Spread $[\$]$', fontsize=35)
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)
        plt.grid(True)
        plt.tight_layout()

        # Plotting
        gain_data_tools_data_extraction \
            .gain_save_plot(function_name, figure, fx_pair, year, '')

        del fx_data
        del figure

        return None

    except FileNotFoundError as e:
        print('No data')
        print(e)
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


if __name__ == "__main__":
    main()
