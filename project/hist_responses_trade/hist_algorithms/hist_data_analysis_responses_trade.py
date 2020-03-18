'''HIST data analysis module.

The functions in the module compute the response function in trade time scale
from the Historic Rate Data from HIST Capital data in a year.

This script requires the following modules:
    * numpy
    * pandas
    * pickle

The module contains the following functions:
    * hist_fx_self_response_year_responses_trade - extracts the midpoint price
     for a year
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

import numpy as np
import pandas as pd
import pickle

import hist_data_tools_responses_trade

__tau__ = 1000

# -----------------------------------------------------------------------------


def hist_fx_self_response_year_responses_trade(fx_pair, year):
    """Computes the self-response of a year.

    Using the midpoint price and the trade signs of a ticker computes the
    self-response during different time lags (:math:`\\tau`) for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: tuple -- The function returns a tuple with numpy arrays.
    """

    function_name = hist_fx_self_response_year_responses_trade.__name__
    hist_data_tools_responses_trade \
        .hist_function_header_print_data(function_name, fx_pair, year, '')

    try:
        # Load data
        _, midpoint = pickle.load(open(
                        f'../../hist_data/extraction_data_{year}/hist_fx'
                        + f'_midpoint_year_data_extraction/hist_fx_midpoint'
                        + f'_year_data_extraction_{year}_{fx_pair}.pickle',
                        'rb'))
        _, trade_signs = pickle.load(open(
                        f'../../hist_data/extraction_data_{year}/hist_fx'
                        + f'_trade_signs_year_data_extraction/hist_fx_trade'
                        + f'_signs_year_data_extraction_{year}_{fx_pair}'
                        + f'.pickle', 'rb'))

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

        self_response = self_response_tau / num

        # Saving data
        hist_data_tools_responses_trade \
            .hist_save_data(function_name, self_response, fx_pair, year,
                            '')

        return self_response

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
