'''Gain data main module.

The functions in the module extract and plot the Historic Rate data from GAIN
Capital in a year.

This script requires the following modules:
    * itertools.product
    * multiprocessing
    * gain_data_analysis_data_extraction
    * gain_data_plot_data_extraction
    * gain_data_tools_data_extraction

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

import gain_data_analysis_data_extraction
import gain_data_plot_data_extraction
import gain_data_tools_data_extraction

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

        # Basic functions
        pool.starmap(gain_data_analysis_data_extraction
                     .gain_fx_year_extract_data,
                     iprod(fx_pairs, [year]))

        # Plot
        pool.starmap(gain_data_plot_data_extraction
                     .gain_fx_quotes_year_plot,
                     iprod(fx_pairs, [year]))
        pool.starmap(gain_data_plot_data_extraction
                     .gain_fx_midpoint_year_plot,
                     iprod(fx_pairs, [year]))
        pool.starmap(gain_data_plot_data_extraction
                     .gain_fx_spread_year_plot,
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
