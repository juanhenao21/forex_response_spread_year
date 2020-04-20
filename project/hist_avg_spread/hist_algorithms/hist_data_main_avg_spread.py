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

    # Run analysis
    # Analysis and plot
    hist_data_generator(fx_pairs, years)

    print('Ay vamos!!')

    return None

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
