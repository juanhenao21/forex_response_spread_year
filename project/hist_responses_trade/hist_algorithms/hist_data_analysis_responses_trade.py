'''HIST data analysis module.

The functions in the module compute the response function in trade time scale
from the Historic Rate Data from HIST Capital data in a year.

This script requires the following modules:
    * itertools
    * multiprocessing
    * numpy
    * os
    * pandas
    * pickle

The module contains the following functions:
    * hist_fx_self_response_week_responses_trade - extracts the midpoint price
      for a week.
    * hist_fx_self_response_year_responses_trade - extracts the midpoint price
      for a year.
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

from itertools import product as iprod
import multiprocessing as mp
import numpy as np
import os
import pandas as pd
import pickle

import hist_data_tools_responses_trade

__tau__ = 1000

# -----------------------------------------------------------------------------


def hist_fx_self_response_week_responses_trade_data(fx_pair, year, week):
    """Computes the self-response of a year.

    Using the midpoint price and the trade signs of a ticker computes the
    self-response during different time lags (:math:`\\tau`) for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: tuple -- The function returns a tuple with numpy arrays.
    """

    try:
        # Load data
        fx_data = pickle.load(open(
                        f'../../hist_data/extraction_data_{year}/hist_fx'
                        + f'_data_extraction/{fx_pair}/hist_fx_data_extraction'
                        + f'_{fx_pair}_w{week}.pickle', 'rb'))

        midpoint = fx_data['Midpoint'].to_numpy()
        trade_signs = fx_data['Signs'].to_numpy()

        # Relate the return of the previous second with the current trade sign
        midpoint = midpoint[:-1]
        trade_signs = trade_signs[1:]

        assert len(midpoint) == len(trade_signs)

        # Array of the average of each tau
        self_response_tau = np.zeros(__tau__)
        num = np.zeros(__tau__)

        # Calculating the midpoint price return and the self-response function
        # Depending on the tau value
        for tau_idx in range(__tau__):

            trade_sign_tau = trade_signs[:-tau_idx - 1]
            trade_sign_no_0_len = len(trade_sign_tau[trade_sign_tau != 0])
            num[tau_idx] = trade_sign_no_0_len
            # Obtain the midpoint price return. Displace the numerator tau
            # values to the right and compute the return

            # Midpoint price returns
            log_return_sec = (midpoint[tau_idx + 1:]
                              - midpoint[:-tau_idx - 1]) \
                / midpoint[:-tau_idx - 1]

            # Obtain the self response value
            if (trade_sign_no_0_len != 0):
                product = log_return_sec * trade_sign_tau
                self_response_tau[tau_idx] = np.sum(product)

        del fx_data

        return (self_response_tau, num)

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        zeros = np.zeros(__tau__)
        return (zeros, zeros)

# ----------------------------------------------------------------------------


def hist_fx_self_response_year_responses_trade_data(fx_pair, year):
    """Computes the self-response of a year.

    Using the hist_self_response_year_responses_trade_data function computes
    the self-response function for a year.

    :param ticker: string of the abbreviation of stock to be analyzed
     (i.e. 'AAPL').
    :param year: string of the year to be analyzed (i.e '2016').
    :return: tuple -- The function returns a tuple with numpy arrays.
    """

    function_name = hist_fx_self_response_year_responses_trade_data.__name__
    hist_data_tools_responses_trade \
        .hist_function_header_print_data(function_name, fx_pair, year, '')

    weeks = hist_data_tools_responses_trade.hist_weeks()

    self_values = []
    args_prod = iprod([fx_pair], [year], weeks)

    # Parallel computation of the self-responses. Every result is appended to
    # a list
    with mp.Pool(processes=mp.cpu_count()) as pool:
        self_values.append(pool.starmap(
            hist_fx_self_response_week_responses_trade_data, args_prod))

    # To obtain the total self-response, I sum over all the self-response
    # values and all the amount of trades (averaging values)
    self_v_final = np.sum(self_values[0], axis=0)

    self_response_val = self_v_final[0] / self_v_final[1]
    self_response_avg = self_v_final[1]

    # Saving data
    if (not os.path.isdir(
            f'../../hist_data/responses_trade_{year}/{function_name}/')):

        try:
            os.mkdir(
                f'../../hist_data/responses_trade_{year}/{function_name}/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    if (not os.path.isdir(
            f'../../hist_data/responses_trade_{year}/{function_name}/'
            + f'{fx_pair}/')):

        try:
            os.mkdir(
                f'../../hist_data/responses_trade_{year}/{function_name}/'
                + f'{fx_pair}/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    hist_data_tools_responses_trade \
        .hist_save_data(self_response_val, fx_pair, year)

    return (self_response_val, self_response_avg)

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
