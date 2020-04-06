'''HIST data analysis module.

The functions in the module extract the bid and ask from the Historic Rate Data
from HIST Capital in a year.

This script requires the following modules:
    * datetime
    * numpy
    * os
    * pandas
    * pickle
    * zipfile

The module contains the following functions:
    * hist_fx_data_extraction - extracts the bid and ask for a year.
    * hist_fx_midpoint_trade_data - extracts the midpoint price for
      a year
    * hist_fx_trade_signs_trade_data - extracts the midpoint price
      for a year
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

import datetime as dt
import numpy as np
import os
import pandas as pd
import pickle
import zipfile

import hist_data_tools_extraction

# -----------------------------------------------------------------------------


def hist_fx_data_extraction(fx_pair, year):
    """Extracts the bid and ask for a week.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name = hist_fx_data_extraction.__name__
    hist_data_tools_extraction \
        .hist_function_header_print_data(function_name, fx_pair, year, '')

    pair = fx_pair.split('_')
    cap_pair = pair[0].upper() + pair[1].upper()
    fx_data_col = ['DateTime', 'Ask', 'Bid']
    fx_data_type = {'DateTime': str, 'Ask': float, 'Bid': float}
    fx_data = pd.DataFrame(columns=fx_data_col)

    for m_num in range(1, 13):

        if (m_num < 10):
            m_num = f'0{m_num}'

        try:
            # Load data
            zf = zipfile.ZipFile(
                f'../../hist_data/original_data_{year}/{fx_pair}/hist'
                + f'_{fx_pair}_{year}{m_num}.zip')
            fx_data = fx_data.append(pd.read_csv(zf.open(
                f'DAT_ASCII_{cap_pair}_T_{year}{m_num}.csv'),
                usecols=(0, 1, 2), names=fx_data_col, dtype=fx_data_type),
                ignore_index=True)

        except FileNotFoundError as e:
            print('No data')
            print(e)
            print()

    # Convert 'DateTime' column to datetime type
    fx_data['DateTime'] = pd.to_datetime(fx_data['DateTime'],
                                         format='%Y%m%d %H%M%S%f')

    # Obtain the dates of every Sunday in the year
    weeks_str = hist_data_tools_extraction.hist_sundays(year)
    # Convert the Sundays dates in datetime type
    weeks = [dt.datetime.strptime(x, '%Y-%m-%d') for x in weeks_str]

    # Saving data
    if (not os.path.isdir(
            f'../../hist_data/extraction_data_{year}/{function_name}/')):

        try:
            os.mkdir(
                f'../../hist_data/extraction_data_{year}/{function_name}/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    if (not os.path.isdir(
            f'../../hist_data/extraction_data_{year}/{function_name}/'
            + f'{fx_pair}/')):

        try:
            os.mkdir(
                f'../../hist_data/extraction_data_{year}/{function_name}/'
                + f'{fx_pair}/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    for w_idx, week in enumerate(weeks):

        if (w_idx):
            week_ini = weeks[w_idx - 1].replace(hour=17, minute=10, second=0)
            # Five days from Sunday 17h10 to Friday 16h50
            t_secs = 432000 - 1200 + 1
            week_fin = week_ini + dt.timedelta(seconds=t_secs)
            w_df = fx_data[(fx_data['DateTime'] < week_fin)
                           & (fx_data['DateTime'] >= week_ini)]
        else:
            # First week of the year
            week_ini = fx_data['DateTime'].iloc[0].replace(
                hour=17, minute=10, second=0, microsecond=0)
            week_fin = weeks[0].replace(
                day=weeks[0].day - 2, hour=16, minute=51, second=0)
            w_df = fx_data[(fx_data['DateTime'] < week_fin)
                           & (fx_data['DateTime'] >= week_ini)]

        # Saving data
        if (w_idx + 1 < 10):
            w_idx = f'0{w_idx + 1}'
        else:
            w_idx += 1
        pickle.dump(w_df, open(f'../../hist_data/extraction_data_{year}/'
                    + f'{function_name}/{fx_pair}/{function_name}_{fx_pair}'
                    + f'_w{w_idx}.pickle', 'wb'))

    # Last days of the year
    week_ini = weeks[-1].replace(hour=17, minute=10, second=0)
    week_fin = fx_data['DateTime'].iloc[-1].replace(
        hour=16, minute=51, second=0, microsecond=0)
    w_df = fx_data[(fx_data['DateTime'] < week_fin)
                   & (fx_data['DateTime'] >= week_ini)]
    # Saving data
    pickle.dump(w_df, open(f'../../hist_data/extraction_data_{year}/'
                + f'{function_name}/{fx_pair}/{function_name}_{fx_pair}'
                + f'_w{w_idx + 1}.pickle', 'wb'))

    del w_df
    del fx_data

    return None

# -----------------------------------------------------------------------------


def hist_fx_midpoint_trade_data(fx_pair, year, week):
    """Extracts the midpoint price for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2019').
    :param week: string of the week to be analyzed (i.e. '01').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name = hist_fx_midpoint_trade_data.__name__
    hist_data_tools_extraction \
        .hist_function_header_print_data(function_name, fx_pair, year, week)

    try:
        # Load data
        fx_data = pickle.load(open(
                        f'../../hist_data/extraction_data_{year}/hist_fx_data'
                        + f'_extraction/{fx_pair}/hist_fx_data_extraction'
                        + f'_{fx_pair}_w{week}.pickle', 'rb'))

        fx_data['Midpoint'] = (fx_data['Ask'] + fx_data['Bid']) / 2
        fx_data['Spread'] = fx_data['Ask'] - fx_data['Bid']

        # Saving data
        hist_data_tools_extraction.hist_save_data(fx_data, fx_pair, year, week)

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
    hist_data_tools_extraction \
        .hist_function_header_print_data(function_name, fx_pair, year, week)

    try:
        # Load data
        fx_data = pickle.load(open(
                        f'../../hist_data/extraction_data_{year}/hist_fx_data'
                        + f'_extraction/{fx_pair}/hist_fx_data_extraction'
                        + f'_{fx_pair}_w{week}.pickle', 'rb'))

        midpoint = fx_data['Midpoint'].to_numpy()
        trade_signs = 0 * midpoint

        for m_idx, m_val in enumerate(midpoint):

            sign = np.sign(m_val - midpoint[m_idx - 1])

            if (sign):
                trade_signs[m_idx] = sign
            else:
                trade_signs[m_idx] = trade_signs[m_idx - 1]

        if (trade_signs[0] == 0):
            trade_signs[0] = trade_signs[1]
        assert np.sum(trade_signs == 0) == 0

        fx_data['Signs'] = trade_signs

        # Saving data
        hist_data_tools_extraction.hist_save_data(fx_data, fx_pair, year, week)

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

    pass

    return None

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
