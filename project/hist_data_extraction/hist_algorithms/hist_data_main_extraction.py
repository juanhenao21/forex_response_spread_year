'''HIST data main module.

The functions in the module extract and plot the Historic Rate data from HIST
Capital in a year.

This script requires the following modules:
    * itertools
    * multiprocessing
    * typing
    * hist_data_analysis_extraction
    * hist_data_plot_extraction
    * hist_data_tools_extraction

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
from typing import List, Tuple

import hist_data_analysis_extraction
import hist_data_plot_extraction
import hist_data_tools_extraction

# -----------------------------------------------------------------------------


def hist_data_plot_generator(fx_pairs: List[str], years: List[str],
                             weeks: Tuple[str, ...]) -> None:
    """Generates all the analysis and plots from the HIST data.

    :param fx_pairs: list of the string abbreviation of the forex pairs to be
     analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param years: list of the strings of the year to be analyzed
     (i.e. ['2016', '2017']).
    :param weeks: tuple of the strings of the weeks to be analyzed
     (i.e. ('01', '02')).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    fx_pair: str
    year: str
    for fx_pair in fx_pairs:
        for year in years:
            # Data extraction
            hist_data_analysis_extraction \
                .hist_fx_data_extraction_week(fx_pair, year)

    # Parallel computing
    with mp.Pool(processes=mp.cpu_count()) as pool:
        # Basic functions
        pool.starmap(hist_data_analysis_extraction
                     .hist_fx_midpoint_trade_data,
                     iprod(fx_pairs, years, weeks))

    # Parallel computing
    with mp.Pool(processes=mp.cpu_count()) as pool:
        # Basic functions
        pool.starmap(hist_data_analysis_extraction
                     .hist_fx_trade_signs_trade_data,
                     iprod(fx_pairs, years, weeks))

    for fx_pair in fx_pairs:
        for year in years:
            # Plot
            hist_data_plot_extraction \
                .hist_fx_quotes_year_plot(fx_pair, year, weeks)
            hist_data_plot_extraction \
                .hist_fx_midpoint_year_plot(fx_pair, year, weeks)
            hist_data_plot_extraction \
                .hist_fx_spread_year_plot(fx_pair, year, weeks)

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    hist_data_tools_extraction.hist_initial_message()

    # Forex pairs and weeks to analyze
    # Response function analysis
    # The other year will be extracted with the spread data
    years_1: List[str] = ['2008', '2014']
    weeks_1: Tuple[str, ...] = hist_data_tools_extraction.hist_weeks()
    fx_pairs_1: List[str] = ['eur_usd', 'gbp_usd', 'usd_jpy', 'aud_usd',
                             'usd_chf', 'usd_cad', 'nzd_usd']

    # Basic folders
    hist_data_tools_extraction.hist_start_folders(years_1)

    # Run analysis
    # Analysis and plot
    hist_data_plot_generator(fx_pairs_1, years_1, weeks_1)

    # Spread impact analysis
    years_2: List[str] = ['2011', '2015', '2019']
    weeks_2: Tuple[str, ...] = hist_data_tools_extraction.hist_weeks()
    fx_pairs_2: List[str] = ['aud_cad', 'aud_chf', 'aud_jpy', 'aud_nzd',
                             'aud_usd', 'cad_chf', 'cad_jpy', 'chf_jpy',
                             'eur_aud', 'eur_cad', 'eur_chf', 'eur_czk',
                             'eur_dkk', 'eur_gbp', 'eur_huf', 'eur_jpy',
                             'eur_nok', 'eur_nzd', 'eur_pln', 'eur_sek',
                             'eur_try', 'eur_usd', 'gbp_aud', 'gbp_cad',
                             'gbp_chf', 'gbp_jpy', 'gbp_nzd', 'gbp_usd',
                             'nzd_cad', 'nzd_chf', 'nzd_jpy', 'nzd_usd',
                             'sgd_jpy', 'usd_cad', 'usd_chf', 'usd_czk',
                             'usd_dkk', 'usd_hkd', 'usd_huf', 'usd_jpy',
                             'usd_mxn', 'usd_nok', 'usd_pln', 'usd_sek',
                             'usd_sgd', 'usd_try', 'usd_zar']

    # Basic folders
    hist_data_tools_extraction.hist_start_folders(years_2)

    # Run analysis
    # Analysis and plot
    hist_data_plot_generator(fx_pairs_2, years_2, weeks_2)

    print('Ay vamos!!!')

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
