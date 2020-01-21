'''GAIN data analysis module.

The functions in the module compute the response function in trade time scale
from the Historic Rate Data from GAIN Capital data in a year.

This script requires the following modules:
    * numpy
    * pandas

The module contains the following functions:
    * gain_fx_self_response_year_responses_trade - extracts the midpoint price
     for a year
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

import numpy as np
import pandas as pd
import pickle

import gain_data_tools_responses_trade

__tau__ = 1000

# -----------------------------------------------------------------------------


def gain_fx_self_response_year_responses_second(fx_pair, year):
    """Extracts the trade signs price for a year.

    The trade signs are obtained from the midpoint price as
    $\epsilon(t) = sign(m(t) - m(t - 1))$, where +1 indicates the trade was
    triggered by a market order to buy, and -1 indicates the trade was
    triggered by a market order to sell.

    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e. '2016').
    :return: tuple -- The function returns a tuple with numpy arrays.
    """

    function_name = gain_fx_self_response_year_responses_second.__name__
    gain_data_tools_responses_trade \
        .gain_function_header_print_data(function_name, fx_pair, year, '')

    try:
        # Load data
        _, midpoint = pickle.load(open(
                        f'../../gain_data/data_extraction_{year}/gain_fx'
                        + f'_midpoint_year_data_extraction/gain_fx_midpoint'
                        + f'_year_data_extraction_{year}_{fx_pair}.pickle',
                        'rb'))
        _, trade_signs = pickle.load(open(
                        f'../../gain_data/data_extraction_{year}/gain_fx'
                        + f'_trade_signs_year_data_extraction/gain_fx_trade'
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
        gain_data_tools_responses_trade \
            .gain_save_data(function_name, self_response, fx_pair, year,
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

    gain_fx_self_response_year_responses_second('eur_usd', '2016')

    return None

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()