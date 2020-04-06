'''HIST data analysis module.

The functions in the module obtain the midpoint price and the trade signs in
physical time scale for HIST Capital in a year.

This script requires the following modules:
    * datetime
    * numpy
    * os
    * pandas
    * pickle

The module contains the following functions:
    * hist_fx_physical_data - extracts the midpoint price for a year
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

import hist_data_tools_physical_basic_data

# -----------------------------------------------------------------------------


def hist_fx_physical_data(fx_pair, year, week):
    """Extracts the midpoint price for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2019').
    :param week: string of the week to be analyzed (i.e. '01').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name = hist_fx_physical_data.__name__
    hist_data_tools_physical_basic_data \
        .hist_function_header_print_data(function_name, fx_pair, year, week)

    try:
        # Load data
        fx_data = pickle.load(open(
                        f'../../hist_data/extraction_data_{year}/hist_fx_data'
                        + f'_extraction/{fx_pair}/hist_fx_data_extraction'
                        + f'_{fx_pair}_w{week}.pickle', 'rb'))

        # DataFrame physical time
        physical_col = ['DateTime', 'Midpoint', 'Signs']
        physical_data = pd.DataFrame(columns=physical_col)
        # Days in the week
        dates = sorted(set(fx_data['DateTime'].dt.date))
        date = dates[0]

        # First day of the week to be analyzed
        t_init = dt.datetime(date.year, date.month, date.day, 17, 10, 0, 0)

        # The total number of seconds in the week. The time starts 10 min after
        # the opening of the market and ends 10 min before it closes
        t_secs = range(0, 86400 * (len(dates) - 1) - 1200 + 2)
        # Create DateTime object with all the seconds in all the days of the
        # week
        dates_seconds = list(map(lambda x: t_init + dt.timedelta(seconds=x),
                                 t_secs))
        physical_data['DateTime'] = dates_seconds[:-1]

        # Initial numpy arrays
        midpoint = np.zeros(len(dates_seconds[:-1]))
        trade_signs = np.zeros(len(dates_seconds[:-1]))

        # Trade data to numpy array
        datetime_fx_data = list(sorted(set(
            map(lambda x: x.replace(microsecond=0), fx_data['DateTime']))))
        midpoint_fx_data = fx_data['Midpoint'].to_numpy()
        trade_signs_fx_data = fx_data['Signs'].to_numpy()
        # Select the last midpoint price of every second. If there is no
        # midpoint price in a second, takes the value of the previous second
        for t_val in datetime_fx_data:
            condition = (fx_data['DateTime'] >= t_val) \
                & (fx_data['DateTime'] < t_val + dt.timedelta(seconds=1))
            trades_same_t_exp = trade_signs_fx_data[condition]
            sign_exp = int(np.sign(np.sum(trades_same_t_exp)))
            pos = np.where(t_val == physical_data['DateTime'])
            trade_signs[pos] = sign_exp
            midpoint[pos] = midpoint_fx_data[condition][-1]

        # Some values in the midpoint array are 0. To fix it find the zero
        # values positions and replace with the first value different to
        # zero
        no_zero_pos = np.where(midpoint != 0)[0]

        for z_idx, z_pos in enumerate(no_zero_pos):
            if (not z_idx):
                midpoint[:z_pos] = midpoint[z_pos]
                midpoint[z_pos:no_zero_pos[z_idx + 1]] = midpoint[z_pos]
            if (z_pos ==no_zero_pos[-1]):
                midpoint[z_pos:] = midpoint[z_pos]
            else:
                midpoint[z_pos:no_zero_pos[z_idx + 1]] = midpoint[z_pos]

        assert not np.sum(midpoint == 0)

        physical_data['Midpoint'] = midpoint
        physical_data['Signs'] = trade_signs

        # Saving data
        hist_data_tools_physical_basic_data \
            .hist_save_data(physical_data, fx_pair, year, week)

        del fx_data
        del physical_data

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

    hist_fx_physical_data('eur_usd', '2019', '02')

    return None

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
