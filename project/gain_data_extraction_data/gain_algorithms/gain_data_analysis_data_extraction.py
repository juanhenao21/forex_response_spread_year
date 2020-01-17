'''GAIN data analysis module.

The functions in the module extract the bid and ask from the Historic Rate Data
from GAIN Capital in a year.

This script requires the following modules:
    * numpy
    * pandas

The module contains the following functions:
    * fx_gain_year_extract_data - extracts the bid and ask for a year.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

import numpy as np
import pandas as pd

import gain_data_tools_data_extraction


# -----------------------------------------------------------------------------


def gain_fx_year_extract_data(fx_pair, year):
    """Extracts the bid and ask for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e. '2016').
    :return: pandas dataframe -- The function returns a pandas dataframe with
     the data.
    """

    function_name = gain_fx_year_extract_data.__name__
    gain_data_tools_data_extraction \
        .gain_function_header_print_data(function_name, fx_pair, year, '')

    fx_data_col = ['lTid', 'cDealable', 'CurrencyPair', 'RateDateTime',
                   'RateBid', 'RateAsk']
    fx_data = pd.DataFrame(columns=fx_data_col)

    for m_num in range(1,13):

        if (m_num < 10):
            m_num = f'0{m_num}'

        for w_num in range(1,6):

            try:
                fx_data = fx_data.append(pd.read_csv(
                    f'../../gain_data/original_data_{year}/{fx_pair}_{year}/'
                    + f'{fx_pair}_{year}{m_num}_w{w_num}.zip'))

            except FileNotFoundError as e:
                print('No data')
                print(e)
                print()

    fx_data.index = pd.to_datetime(fx_data['RateDateTime'])

    # Saving data
    gain_data_tools_data_extraction \
        .gain_save_data(function_name, fx_data, fx_pair, year, '')

    return fx_data

# -----------------------------------------------------------------------------


def main():

    pass

    return None

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()