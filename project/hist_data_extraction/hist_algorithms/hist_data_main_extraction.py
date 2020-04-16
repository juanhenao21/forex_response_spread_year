'''HIST data main module.

The functions in the module extract and plot the Historic Rate data from HIST
Capital in a year.

This script requires the following modules:
    * itertools.product
    * multiprocessing
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

import hist_data_analysis_extraction
import hist_data_plot_extraction
import hist_data_tools_extraction

# -----------------------------------------------------------------------------


def hist_data_plot_generator(fx_pairs, years, weeks):
    """Generates all the analysis and plots from the HIST data.

    :param fx_pairs: list of the string abbreviation of the forex pairs to be
     analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param years: list of the string of the year to be analyzed
     (i.e. ['2016', '2017']).
    :param weeks: list of the string of the weeks to be analyzed
     (i.e. ['01', '02']).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    for fx_pair in fx_pairs:
        for year in years:
            # Data extraction
            hist_data_analysis_extraction \
                .hist_fx_data_extraction(fx_pair, year)

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
            hist_data_plot_extraction.hist_fx_quotes_year_plot(fx_pair, year,
                                                               weeks)
            hist_data_plot_extraction.hist_fx_midpoint_year_plot(fx_pair, year,
                                                                 weeks)
            hist_data_plot_extraction.hist_fx_spread_year_plot(fx_pair, year,
                                                               weeks)

    return None

# -----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    # Forex pairs and weeks to analyze
    # Response function analysis
    # The other year will be extracted with the spread data
    years = ['2008', '2014']
    weeks = hist_data_tools_extraction.hist_weeks()
    fx_pairs = ['eur_usd', 'gbp_usd', 'usd_jpy', 'aud_usd',
                'usd_chf', 'usd_cad', 'nzd_usd']

    # Basic folders
    hist_data_tools_extraction.hist_start_folders(years)

    # Run analysis
    # Analysis and plot
    hist_data_plot_generator(fx_pairs, years, weeks)

    # Spread impact analysis
    years = ['2011', '2015', '2019']
    weeks = hist_data_tools_extraction.hist_weeks()
    fx_pairs = ['eur_usd', 'eur_chf', 'eur_gbp', 'eur_jpy', 'eur_aud',
                'usd_cad', 'usd_chf', 'usd_jpy', 'usd_mxn', 'gbp_chf',
                'gbp_jpy', 'gbp_usd', 'aud_jpy', 'aud_usd', 'chf_jpy',
                'nzd_jpy', 'nzd_usd', 'xau_usd', 'eur_cad', 'aud_cad',
                'cad_jpy', 'eur_nzd', 'nzd_cad', 'sgd_jpy', 'usd_hkd',
                'usd_try', 'aud_chf', 'usd_dkk', 'aux_aud', 'eur_huf',
                'eur_pln', 'usd_nok', 'eur_nok', 'eur_try', 'gbp_cad',
                'nzd_chf', 'spx_usd', 'usd_huf', 'usd_pln', 'usd_zar',
                'zar_jpy', 'bco_usd', 'eur_czk', 'usd_sgd', 'xag_usd',
                'eur_sek', 'gbp_aud', 'gbp_nzd', 'jpx_jpy', 'udx_usd',
                'usd_czk', 'usd_sek', 'wti_usd', 'aud_nzd', 'nsx_usd',
                'cad_chf', 'eur_dkk']

    # Basic folders
    hist_data_tools_extraction.hist_start_folders(years)

    # Run analysis
    # Analysis and plot
    hist_data_plot_generator(fx_pairs, years, weeks)

    print('Ay vamos!!')

    return None

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
