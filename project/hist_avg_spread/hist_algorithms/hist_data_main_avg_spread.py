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

    # Run analysis
    # Analysis and plot
    hist_data_generator(fx_pairs, years)

    print('Ay vamos!!')

    return None

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
