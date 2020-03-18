'''HIST data plot module.

The functions in the module plot the data obtained in the
hist_data_analysis_responses_trade module.

This script requires the following modules:
    * matplotlib
    * pickle
    * hist_data_tools_data_extract

The module contains the following functions:
    * hist_fx_self_response_year_avg_responses_trade_plot - plots the self-
     response average for a year.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# ----------------------------------------------------------------------------
# Modules

from matplotlib import pyplot as plt
import pickle

import hist_data_tools_responses_trade

# ----------------------------------------------------------------------------


def hist_fx_self_response_year_avg_responses_trade_plot(fx_pair, year):
    """Plots the self-response average for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e. '2016').
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        function_name = hist_fx_self_response_year_avg_responses_trade_plot \
            .__name__
        hist_data_tools_responses_trade \
            .hist_function_header_print_plot(function_name, fx_pair, year, '')
        fx_pair_upper = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()

        figure = plt.figure(figsize=(16, 9))

        # Load data
        self_response = pickle.load(open(
                        f'../../hist_data/responses_trade_{year}/hist_fx_self'
                        + f'_response_year_responses_trade/hist_fx_self'
                        + f'_response_year_responses_trade_{year}_{fx_pair}'
                        + f'.pickle', 'rb'))

        plt.semilogx(self_response, linewidth=5, label=f'{fx_pair_upper}')
        plt.legend(loc='best', fontsize=25)
        plt.title(f'HIST data self-response', fontsize=40)
        plt.xlabel(r'$\tau \, [trades]$', fontsize=35)
        plt.ylabel(r'$R_{ii}(\tau)$', fontsize=35)
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)
        plt.xlim(1, 1000)
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        plt.grid(True)
        plt.tight_layout()

        # Plotting
        hist_data_tools_responses_trade \
            .hist_save_plot(function_name, figure, fx_pair, year, '')

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
