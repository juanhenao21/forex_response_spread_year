'''HIST data analysis module.

The functions in the module obtain the midpoint price and the trade signs in
physical time scale for HIST Capital in a year.

This script requires the following modules:
    * numpy
    * os
    * pandas
    * pickle
    * zipfile

The module contains the following functions:
    * hist_fx_midpoint_physical_data - extracts the midpoint price for
      a year
    * hist_fx_trade_signs_physical_data - extracts the midpoint price
     for a year
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

import numpy as np
import os
import pandas as pd
import pickle
import zipfile

import hist_data_tools_physical_basic_data

# -----------------------------------------------------------------------------


def hist_fx_midpoint_physical_data(fx_pair, year, week):
    """Extracts the midpoint price for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2019').
    :param week: string of the week to be analyzed (i.e. '01').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name = hist_fx_midpoint_physical_data.__name__
    hist_data_tools_physical_basic_data \
        .hist_function_header_print_data(function_name, fx_pair, year, week)

    try:
        # Load data
        fx_data = pickle.load(open(
                        f'../../hist_data/extraction_data_{year}/hist_fx_data'
                        + f'_extraction/{fx_pair}/hist_fx_data_extraction'
                        + f'_{fx_pair}_w{week}.pickle', 'rb'))

        # Combine Date and Time columns
        fx_data['Time'] = pd.to_datetime(fx_data['Time'],
                                         format='%H%M%S%f').dt.time
        fx_data.insert(0, 'DateTime', pd.to_datetime(
            fx_data['Date'].dt.strftime('%Y-%m-%d')
            + ' ' + fx_data['Time'].astype(str), format='%Y%m%d %H:%M:%S.%f'))
        fx_data = fx_data.drop(columns=['Date', 'Time'])
        print(fx_data.head())
        print(fx_data.tail())

        print(pd.Interval(fx_data['DateTime'].iloc[0], fx_data['DateTime'].iloc[-1]))

        # Saving data
        hist_data_tools_physical_basic_data.hist_save_data(fx_data, fx_pair,
                                                           year, week)

        del fx_data

        return None

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        return None

# -----------------------------------------------------------------------------


def hist_fx_trade_signs_trade_data(fx_pair, year, week):
    """Extracts the trade signs price for a year.

    The trade signs are obtained from the midpoint price as
    :math:`\\epsilon(t) = sign(m(t) - m(t - 1))`, where +1 indicates the trade
    was triggered by a market order to buy, and -1 indicates the trade was
    triggered by a market order to sell.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name = hist_fx_trade_signs_trade_data.__name__
    hist_data_tools_physical_basic_data \
        .hist_function_header_print_data(function_name, fx_pair, year, week)

    try:
        # Load data
        fx_data = pickle.load(open(
                        f'../../hist_data/extraction_data_{year}/hist_fx_data'
                        + f'_extraction/{fx_pair}/hist_fx_data_extraction'
                        + f'_{fx_pair}_w{week}.pickle', 'rb'))

        midpoint = fx_data['Midpoint'].to_numpy()
        trade_signs = 0 * midpoint

        for m_idx, m_val in enumerate(fx_data['Midpoint']):

            sign = np.sign(m_val - midpoint[m_idx - 1])

            if (sign):
                trade_signs[m_idx] = sign
            else:
                trade_signs[m_idx] = trade_signs[m_idx - 1]

        assert np.sum(trade_signs == 0) == 0

        fx_data['Signs'] = trade_signs

        # Saving data
        hist_data_tools_physical_basic_data.hist_save_data(fx_data, fx_pair, year, week)

        del fx_data

        return None

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        return None

# -----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

    hist_fx_midpoint_physical_data('eur_usd', '2019', '01')

    return None

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
