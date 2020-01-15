'''ITCH data main module.

The functions in the module extract and plot of the ITCH data.

This script requires the following modules:
    * itertools.product
    * multiprocessing
    * itch_data_analysis_data_extraction
    * itch_data_plot_data_extraction
    * itch_data_tools_data_extraction

The module contains the following functions:
    * itch_data_plot_generator - generates all the analysis and plots from the
      ITCH data.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from itertools import product as iprod
import multiprocessing as mp

import itch_data_analysis_data_extraction
import itch_data_plot_data_extraction
import itch_data_tools_data_extraction

# -----------------------------------------------------------------------------


def itch_data_plot_generator(tickers, dates):
    """Generates all the analysis and plots from the ITCH data.

    :param tickers: list of the string abbreviation of the stocks to be
     analized (i.e. ['AAPL', 'MSFT']).
    :param dates: list of strings with the date of the data to be extracted
     (i.e. ['2008-01-02', '2008-01-03]).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    # Parallel computing
    with mp.Pool(processes=mp.cpu_count()) as pool:

        # Basic functions
        pool.starmap(itch_data_analysis_data_extraction
                     .itch_midpoint_second_data,
                     iprod(tickers, dates))
        pool.starmap(itch_data_analysis_data_extraction
                     .itch_trade_signs_second_data,
                     iprod(tickers, dates))

        # Plot
        pool.starmap(itch_data_plot_data_extraction
                     .itch_midpoint_second_plot,
                     iprod(tickers, [dates]))

    return None

# -----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    # Tickers and days to analyze
    tickers = ['AAPL']
    dates_2008 = ['2008-01-07', '2008-01-08', '2008-01-09', '2008-01-10',
                  '2008-01-11']
    dates_2016 = ['2016-03-07', '2016-03-08', '2016-03-09', '2016-03-10',
                  '2016-03-11']

    # Run analysis
    itch_data_plot_generator(tickers, dates_2008)
    itch_data_plot_generator(tickers, dates_2016)

    print('Ay vamos!!')

    return None

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
