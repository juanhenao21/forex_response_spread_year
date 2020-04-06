'''HIST data main module.

The functions in the module run the complete extraction, analysis and plot of
the HIST data.

This script requires the following modules:
    * itertools.product
    * multiprocessing
    * os
    * pandas
    * pickle
    * hist_data_analysis_avg_responses
    * hist_data_plot_avg_responses
    * hist_data_tools_avg_responses

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
import os
import pandas as pd
import pickle

import hist_data_analysis_avg_responses
import hist_data_plot_avg_responses
import hist_data_tools_avg_responses

# -----------------------------------------------------------------------------


def hist_data_plot_generator(year):
    """Generates all the analysis and plots from the HIST data.

    :param div: integer of the number of divisions in the tickers (i.e. 5).
    :param year: string of the year to be analyzed (i.e '2016').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    fx_pairs = hist_data_analysis_avg_responses \
        .hist_fx_pair_spread_data(year)

    for t_idx, ticker in enumerate(tickers):
        print(f'GROUP {t_idx + 1}')
        for t in ticker:
            print(t)
        print(f'Number of tickers group {t_idx + 1}: {len(ticker)}')
        print()

    hist_data_analysis_avg_responses \
        .hist_fx_self_response_year_avg_responses_trade_data(fx_pairs, year)

    hist_data_analysis_avg_responses \
        .hist_fx_self_response_year_avg_responses_physical_data(fx_pairs, year)

    hist_data_plot_avg_responses \
        .hist_fx_self_response_year_avg_responses_trade_plot(year)

    hist_data_plot_avg_responses \
        .hist_fx_self_response_year_avg_responses_physical_plot(year)

    return None

# -----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    year = '2008'

    # Basic folders
    hist_data_tools_avg_responses.hist_start_folders(year)

    # Run analysis
    # Analysis and plot
    hist_data_plot_generator(year)

    print('Ay vamos!!')

    return None

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
