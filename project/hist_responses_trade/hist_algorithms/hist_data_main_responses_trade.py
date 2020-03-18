'''Gain data main module.

The functions in the module compute the responses of the Historic Rate data
from HIST Capital in a year.

This script requires the following modules:
    * itertools.product
    * multiprocessing
    * hist_data_analysis_responses_trade
    * hist_data_plot_responses_trade
    * hist_data_tools_responses_trade

The module contains the following functions:
    * hist_data_plot_generator - generates all the analysis and plots from the
      HIST data.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from itertools import product as iprod
import multiprocessing as mp

import hist_data_analysis_responses_trade
import hist_data_plot_responses_trade
import hist_data_tools_responses_trade

# -----------------------------------------------------------------------------


def hist_data_plot_generator(fx_pairs, year):
    """Generates all the analysis and plots from the HIST data.

    :param fx_pairs: list of the string abbreviation of the forex pairs to be
     analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    # Parallel computing
    with mp.Pool(processes=mp.cpu_count()) as pool:

        # Specific functions
        # pool.starmap(hist_data_analysis_responses_trade
        #              .hist_fx_self_response_year_responses_trade,
        #              iprod(fx_pairs, [year]))

        # Plot
        pool.starmap(hist_data_plot_responses_trade
                     .hist_fx_self_response_year_avg_responses_trade_plot,
                     iprod(fx_pairs, [year]))

    return None

# -----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    # Tickers and days to analyze
    # year, fx_pairs = hist_data_tools_responses_trade.hist_initial_data()
    # To be used when run in server
    year = '2016'
    fx_pairs = ['eur_usd']
    # fx_pairs = ['eur_usd', 'gbp_usd', 'usd_jpy', 'aud_usd',
    #             'usd_chf', 'usd_cad', 'nzd_usd']

    # Basic folders
    hist_data_tools_responses_trade.hist_start_folders(year)

    # Run analysis
    # Analysis and plot
    hist_data_plot_generator(fx_pairs, year)

    print('Ay vamos!!')

    return None

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
