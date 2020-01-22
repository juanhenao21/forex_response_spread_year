'''Gain data main module.

The functions in the module compute the responses of the Historic Rate data
from GAIN Capital in a year.

This script requires the following modules:
    * itertools.product
    * multiprocessing
    * gain_data_analysis_responses_trade
    * gain_data_plot_responses_trade
    * gain_data_tools_responses_trade

The module contains the following functions:
    * gain_data_plot_generator - generates all the analysis and plots from the
      GAIN data.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from itertools import product as iprod
import multiprocessing as mp

import gain_data_analysis_responses_trade
import gain_data_plot_responses_trade
import gain_data_tools_responses_trade

# -----------------------------------------------------------------------------


def gain_data_plot_generator(fx_pairs, year):
    """Generates all the analysis and plots from the GAIN data.

    :param fx_pairs: list of the string abbreviation of the forex pairs to be
     analized (i.e. ['eur_usd', 'gbp_usd']).
    :param year: string of the year to be analized (i.e. '2016').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    # Parallel computing
    with mp.Pool(processes=mp.cpu_count()) as pool:

        # Especific functions
        pool.starmap(gain_data_analysis_responses_trade
                     .gain_fx_self_response_year_responses_trade,
                     iprod(fx_pairs, [year]))

        # Plot
        pool.starmap(gain_data_plot_responses_trade
                     .gain_fx_self_response_year_avg_responses_trade_plot,
                     iprod(fx_pairs, [year]))

    return None

# -----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    # Tickers and days to analyze
    fx_pairs = ['eur_usd']
    year = '2016'

    # Run analysis
    gain_data_plot_generator(fx_pairs, year)

    print('Ay vamos!!')

    return None

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
