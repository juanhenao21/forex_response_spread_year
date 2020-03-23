'''HIST data main module.

The functions in the module extract and plot the Historic Rate data from HIST
Capital in a year.

This script requires the following modules:
    * histdata
    * itertools.product
    * multiprocessing
    * os
    * hist_data_tools_download

The module contains the following functions:
    * hist_download_data - downloads the HIST data.
    * hist_download_all_data - downloads all the HIST data.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from histdata import download_hist_data as dl
from histdata.api import Platform as P, TimeFrame as TF
from itertools import product as iprod
import multiprocessing as mp
import os

import hist_data_tools_download

# -----------------------------------------------------------------------------


def hist_download_data(fx_pair, year):
    """Downloads the HIST data.

    :param fx_pair: string abbreviation of the forex pairs to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name = hist_download_data.__name__
    hist_data_tools_download.hist_function_header_print_data(
        function_name, fx_pair, year, '')

    pair_split = fx_pair.split('_')
    p = pair_split[0] + pair_split[1]
    p_cap = pair_split[0].upper() + pair_split[1].upper()

    # Absolute path file
    abs_path = os.path.abspath(__file__).split('/')
    # Take the path from the start to the project folder
    root_path = '/'.join(abs_path[:abs_path.index('project') + 1])
    os.chdir(root_path + f'/hist_data/original_data_{year}/{fx_pair}/')

    for m in range(1, 13):

        dl(year=f'{year}', month=f'{m}', pair=f'{p}', platform=P.GENERIC_ASCII,
           time_frame=TF.TICK_DATA)
        if (m < 10):
            m = f'0{m}'
        os.rename(f'DAT_ASCII_{p_cap}_T_{year}{m}.zip',
                  f'hist_{fx_pair}_{year}{m}.zip')

    return None

# -----------------------------------------------------------------------------


def hist_download_all_data(fx_pairs, years):
    """Downloads all the HIST data.

    :param fx_pairs: list of the string abbreviation of the forex pairs to be
     analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    with mp.Pool(processes=mp.cpu_count()) as pool:

        pool.starmap(hist_download_data, iprod(fx_pairs, years))

    return None
# -----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    # Tickers and days to analyze
    hist_data_tools_download.hist_initial_data()
    years = ['2008', '2014', '2019']
    fx_pairs = ['eur_usd', 'gbp_usd', 'usd_jpy', 'aud_usd',
                'usd_chf', 'usd_cad', 'nzd_usd']


    # Basic folders
    hist_data_tools_download.hist_start_folders(fx_pairs, years)

    # Run analysis
    # Download data
    hist_download_all_data(fx_pairs, years)

    print('Ay vamos!!')

    return None

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
