'''HIST data main module.

The functions in the module extract and plot the Historic Rate data from HIST
Capital in a year.

This script requires the following modules:
    * itertools
    * multiprocessing
    * os
    * typing
    * histdata
    * hist_data_tools_download

The module contains the following functions:
    * hist_download_data - downloads the HIST data.
    * hist_download_all_data - downloads all the HIST data.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from itertools import product as iprod
import multiprocessing as mp
import os
from typing import List

from histdata import download_hist_data as dl  # type: ignore
from histdata.api import Platform as P, TimeFrame as TF  # type: ignore

import hist_data_tools_download

# -----------------------------------------------------------------------------


def hist_download_data(fx_pair: str, year: str) -> None:
    """Downloads the HIST data.

    :param fx_pair: string abbreviation of the forex pairs to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    try:
        function_name: str = hist_download_data.__name__
        hist_data_tools_download.hist_function_header_print_data(
            function_name, fx_pair, year, '')

        pair_split: List[str] = fx_pair.split('_')
        p_low: str = pair_split[0] + pair_split[1]
        p_cap: str = pair_split[0].upper() + pair_split[1].upper()

        # Absolute path file
        abs_path: List[str] = os.path.abspath(__file__).split('/')
        # Take the path from the start to the project folder
        root_path: str = '/'.join(abs_path[:abs_path.index('project') + 1])
        os.chdir(root_path + f'/hist_data/original_data_{year}/{fx_pair}/')

        # Download forex pair for a year
        m_val: int
        for m_val in range(1, 13):

            dl(year=f'{year}', month=f'{m_val}', pair=f'{p_low}',
               platform=P.GENERIC_ASCII, time_frame=TF.TICK_DATA)
            if m_val < 10:
                m_val_str = f'0{m_val}'
                os.rename(f'DAT_ASCII_{p_cap}_T_{year}{m_val_str}.zip',
                          f'hist_{fx_pair}_{year}{m_val_str}.zip')
            else:
                os.rename(f'DAT_ASCII_{p_cap}_T_{year}{m_val}.zip',
                          f'hist_{fx_pair}_{year}{m_val}.zip')

    except AssertionError as error:
        print('No data')
        print(error)

# -----------------------------------------------------------------------------


def hist_download_all_data(fx_pairs: List[str], years: List[str]) -> None:
    """Downloads all the HIST data.

    :param fx_pairs: list of the string abbreviation of the forex pairs to be
     analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    with mp.Pool(processes=mp.cpu_count()) as pool:

        pool.starmap(hist_download_data, iprod(fx_pairs, years))

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    hist_data_tools_download.hist_initial_message()

    # Forex pairs and weeks to analyze
    # Response function analysis
    # The other years will be downloaded with the spread data
    years_1: List[str] = ['2008', '2014']
    fx_pairs_1: List[str] = ['eur_usd', 'gbp_usd', 'usd_jpy', 'aud_usd',
                             'usd_chf', 'usd_cad', 'nzd_usd']

    # Basic folders
    hist_data_tools_download.hist_start_folders(fx_pairs_1, years_1)

    # Run analysis
    # Download data
    hist_download_all_data(fx_pairs_1, years_1)

    # Spread impact analysis
    years_2: List[str] = ['2011', '2015', '2019']
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
    hist_data_tools_download.hist_start_folders(fx_pairs_2, years_2)

    # Run analysis
    # Download data
    hist_download_all_data(fx_pairs_2, years_2)

    print('Ay vamos!!!')

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
