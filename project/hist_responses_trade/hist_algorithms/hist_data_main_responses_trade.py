'''HIST data main module.

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


def hist_data_plot_generator(fx_pairs, years):
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

    # Specific functions
    for fx_pair in fx_pairs:
        for year in years:
            # Self-response
            hist_data_analysis_responses_trade \
                .hist_fx_self_response_year_responses_trade_data(fx_pair, year)

    # Parallel computing
    with mp.Pool(processes=mp.cpu_count()) as pool:
        # Plot
        pool.starmap(hist_data_plot_responses_trade
                     .hist_fx_self_response_year_avg_responses_trade_plot,
                     iprod(fx_pairs, years))

    return None

# -----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    # Forex pairs and weeks to analyze
    # Response function analysis
    # The other years will be analyzed with the spread data
    years = ['2008', '2014']
    fx_pairs = ['eur_usd', 'gbp_usd', 'usd_jpy', 'aud_usd',
                'usd_chf', 'usd_cad', 'nzd_usd']

    # Basic folders
    hist_data_tools_responses_trade.hist_start_folders(years)

    # Run analysis
    # Analysis and plot
    hist_data_plot_generator(fx_pairs, years)

    # Spread impact analysis
    years = ['2011', '2015', '2019']
    fx_pairs = ['aud_cad', 'aud_chf', 'aud_jpy', 'aud_nzd', 'aud_usd',
                'aux_aud', 'bco_usd', 'cad_chf', 'cad_jpy', 'chf_jpy',
                'eur_aud', 'eur_cad', 'eur_chf', 'eur_czk', 'eur_dkk',
                'eur_gbp', 'eur_huf', 'eur_jpy', 'eur_nok', 'eur_nzd',
                'eur_pln', 'eur_sek', 'eur_try', 'eur_usd', 'gbp_aud',
                'gbp_cad', 'gbp_chf', 'gbp_jpy', 'gbp_nzd', 'gbp_usd',
                'jpx_jpy', 'nsx_usd', 'nzd_cad', 'nzd_chf', 'nzd_jpy',
                'nzd_usd', 'sgd_jpy', 'spx_usd', 'udx_usd', 'usd_cad',
                'usd_chf', 'usd_czk', 'usd_dkk', 'usd_hkd', 'usd_huf',
                'usd_jpy', 'usd_mxn', 'usd_nok', 'usd_pln', 'usd_sek',
                'usd_sgd', 'usd_try', 'usd_zar', 'wti_usd', 'xag_usd',
                'xau_usd', 'zar_jpy']

    # Basic folders
    hist_data_tools_responses_trade.hist_start_folders(years)

    # Run analysis
    # Analysis and plot
    hist_data_plot_generator(fx_pairs, years)

    print('Ay vamos!!')

    return None

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
