'''HIST data plot module.

The functions in the module plot the data obtained in the
hist_data_analysis_avg_responses module.

This script requires the following modules:
    * matplotlib
    * numpy
    * pickle
    * hist_data_tools_avg_responses

The module contains the following functions:
    * hist_self_response_year_avg_plot - plots the self-response average for a
      year.
    * hist_cross_response_year_avg_plot - plots the cross-response average for a
      year.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# ----------------------------------------------------------------------------
# Modules

from matplotlib import pyplot as plt
import numpy as np
import pickle

import hist_data_tools_avg_responses

# ----------------------------------------------------------------------------


def hist_fx_self_response_year_avg_responses_trade_plot(year):
    """Plots the self-response average for a year.

    :param year: string of the year to be analyzed (i.e '2008').
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        function_name = hist_fx_self_response_year_avg_responses_trade_plot \
            .__name__
        hist_data_tools_avg_responses \
            .hist_function_header_print_plot(function_name, '', year)

        # Load data
        resp_g1, resp_g2, resp_g3, resp_g4, resp_g5 = pickle.load(open(
            f'../../hist_data/avg_responses_data_{year}/hist_fx_self'
            + f'_response_year_avg_responses_trade_data/hist_fx_self_response'
            + f'_year_avg_responses_trade_data_{year}_.pickle', 'rb'))

        figure = plt.figure(figsize=(16, 9))

        plt.semilogx(resp_g1, linewidth=5, label=f'Group 1')
        plt.semilogx(resp_g2, linewidth=5, label=f'Group 2')
        plt.semilogx(resp_g3, linewidth=5, label=f'Group 3')
        plt.semilogx(resp_g4, linewidth=5, label=f'Group 4')
        plt.semilogx(resp_g5, linewidth=5, label=f'Group 5')

        plt.legend(loc='best', fontsize=25)
        plt.title('Self-response', fontsize=40)
        plt.xlabel(r'$\tau \, [s]$', fontsize=35)
        plt.ylabel(r'$R_{ii}(\tau)$', fontsize=35)
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)
        plt.xlim(1, 10000)
        # plt.ylim(13 * 10 ** -5, 16 * 10 ** -5)
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        plt.grid(True)
        plt.tight_layout()

        # Plotting
        hist_data_tools_avg_responses \
            .hist_save_plot(function_name, figure, '', year)

        return None

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        return None

# ----------------------------------------------------------------------------


def hist_fx_self_response_year_avg_responses_physical_plot(year):
    """Plots the self-response average for a year.

    :param year: string of the year to be analyzed (i.e '2008').
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        function_name = hist_fx_self_response_year_avg_responses_physical_plot \
            .__name__
        hist_data_tools_avg_responses \
            .hist_function_header_print_plot(function_name, '', year, '')

        # Load data
        resp_g1, resp_g2, resp_g3, resp_g4, resp_g5 = pickle.load(open(
            f'../../hist_data/avg_responses_data_{year}/hist_fx_self'
            + f'_response_year_avg_responses_physical_data/hist_fx_self_response'
            + f'_year_avg_responses_physical_data_{year}_.pickle', 'rb'))

        figure = plt.figure(figsize=(16, 9))

        plt.semilogx(resp_g1, linewidth=5, label=f'Group 1')
        plt.semilogx(resp_g2, linewidth=5, label=f'Group 2')
        plt.semilogx(resp_g3, linewidth=5, label=f'Group 3')
        plt.semilogx(resp_g4, linewidth=5, label=f'Group 4')
        plt.semilogx(resp_g5, linewidth=5, label=f'Group 5')

        plt.legend(loc='best', fontsize=25)
        plt.title('Self-response', fontsize=40)
        plt.xlabel(r'$\tau \, [s]$', fontsize=35)
        plt.ylabel(r'$R_{ii}(\tau)$', fontsize=35)
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)
        plt.xlim(1, 10000)
        # plt.ylim(13 * 10 ** -5, 16 * 10 ** -5)
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        plt.grid(True)
        plt.tight_layout()

        # Plotting
        hist_data_tools_avg_responses \
            .hist_save_plot(function_name, figure, '', year, '')

        return None

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        return None

# ----------------------------------------------------------------------------


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
