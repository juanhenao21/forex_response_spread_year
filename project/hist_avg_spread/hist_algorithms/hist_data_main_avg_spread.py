'''HIST data main module.

The functions in the module run the complete analysis of the HIST data.

This script requires the following modules:
    * itertools.product
    * multiprocessing
    * hist_data_analysis_avg_spread
    * hist_data_tools_avg_spread

The module contains the following functions:
    * hist_data_generator - generates all the analysis of the HIST data.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from itertools import product as iprod
import multiprocessing as mp

import hist_data_analysis_avg_spread
import hist_data_tools_avg_spread

# -----------------------------------------------------------------------------


def hist_data_generator(fx_pairs, years):
    """Generates all the analysis of the HIST data.

    :param fx_pairs: list of the string abbreviation of the forex pairs to be
     analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param years: list of the string of the years to be analyzed
     (i.e ['2016', '2019']).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    for year in years:
        # Statistics of the quotes and trades
        hist_data_analysis_avg_spread \
            .hist_quotes_trades_year_avg_spread_data(fx_pairs, year)

    return None

# -----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    # Fx pairs and days to analyze
    # Spread impact analysis
    fx_pairs = ['eur_usd']
    years = ['2019']
    # years = ['2008', '2014', '2019']
    # fx_pairs = ['eur_usd', 'eur_chf', 'eur_gbp', 'eur_jpy', 'eur_aud',
    #             'usd_cad', 'usd_chf', 'usd_jpy', 'usd_mxn', 'gbp_chf',
    #             'gbp_jpy', 'gbp_usd', 'aud_jpy', 'aud_usd', 'chf_jpy',
    #             'nzd_jpy', 'nzd_usd', 'xau_usd', 'eur_cad', 'aud_cad',
    #             'cad_jpy', 'eur_nzd', 'grx_eur', 'nzd_cad', 'sgd_jpy',
    #             'usd_hkd', 'usd_nok', 'usd_try', 'xau_aud', 'aud_chf',
    #             'aux_aud', 'eur_huf', 'eur_pln', 'frx_eur', 'hkx_hkd',
    #             'nzd_chf', 'spx_usd', 'usd_huf', 'usd_pln', 'usd_zar',
    #             'xau_chf', 'zar_jpy', 'bco_usd', 'etx_eur', 'eur_czk',
    #             'eur_sek', 'gbp_aud', 'gbp_nzd', 'jpx_jpy', 'udx_usd',
    #             'usd_czk', 'usd_sek', 'wti_usd', 'xau_eur', 'aud_nzd',
    #             'cad_chf', 'eur_dkk', 'eur_nok', 'eur_try', 'gbp_cad',
    #             'nsx_usd', 'ukx_gbp', 'usd_dkk', 'usd_sgd', 'xag_usd',
    #             'xau_gbp']

    # Run analysis
    # Analysis and plot
    hist_data_generator(fx_pairs, years)

    print('Ay vamos!!')

    return None

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
