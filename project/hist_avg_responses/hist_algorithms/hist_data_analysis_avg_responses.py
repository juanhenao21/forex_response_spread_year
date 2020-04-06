'''HIST data analysis module.

The functions in the module analyze the data from the NASDAQ stock market,
computing the self- and cross-response functions and the trade sign self- and
cross-correlator functions. This module reproduces the sections 3.1 and 3.2 of
the `paper
<https://link.springer.com/content/pdf/10.1140/epjb/e2016-60818-y.pdf>`_.


This script requires the following modules:
    * numpy
    * pandas
    * pickle
    * hist_data_tools_avg_responses_physical

The module contains the following functions:
    * hist_tickers_spread_data - obtains the tickers and the spread for the
      classification.
    * hist_self_response_year_avg_responses_trade_data - computes the average
      self response for groups of tickers in a year in trade time scale.
    * hist_self_response_year_avg_responses_physical_data - computes the average
      self response for groups of tickers in a year in physical time scale.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# ----------------------------------------------------------------------------
# Modules

import numpy as np
import pandas as pd
import pickle

import hist_data_tools_avg_responses

__tau__ = 10000

# ----------------------------------------------------------------------------


def hist_fx_pair_spread_data(year):
    """Obtains the tickers and the spread range for the classification.

    :param year: string of the year to be analyzed (i.e. '2016').
    :return: tuple -- The function returns a tuple with a numpy array and a
     list.
    """

    function_name = hist_fx_pair_spread_data.__name__
    hist_data_tools_avg_responses \
        .hist_function_header_print_data(function_name, '', year, '')

    try:
        # load data
        spread_data = pd.read_csv(
            f'../../hist_avg_spread/hist_avg_spread_{year}.csv',
            usecols=['FxPair', 'Avg_Spread'])

        tickers = []

        g1 = spread_data[spread_data['Avg_Spread'] < 0.03]
        tickers_g1 = g1['Ticker'].tolist()
        g2 = spread_data[(spread_data['Avg_Spread'] <= 0.03)
                         & spread_data['Avg_Spread'] < 0.06]
        tickers_g2 = g2['Ticker'].tolist()
        g3 = spread_data[(spread_data['Avg_Spread'] <= 0.06)
                         & spread_data['Avg_Spread'] < 0.09]
        tickers_g3 = g3['Ticker'].tolist()
        g4 = spread_data[(spread_data['Avg_Spread'] <= 0.09)
                         & spread_data['Avg_Spread'] < 0.15]
        tickers_g4 = g4['Ticker'].tolist()
        g5 = spread_data[(spread_data['Avg_Spread'] <= 0.15)
                         & spread_data['Avg_Spread'] < 0.4]
        tickers_g5 = g5['Ticker'].tolist()

        tickers.append(tickers_g1)
        tickers.append(tickers_g2)
        tickers.append(tickers_g3)
        tickers.append(tickers_g4)
        tickers.append(tickers_g5)

        return tickers

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        raise Exception('Check the CSV file')

# ----------------------------------------------------------------------------


def hist_fx_self_response_year_avg_responses_trade_data(fx_pairs, year):
    """Computes the avg self-response for groups of tickers in a year.

    :param fx_pairs: list of strings of the abbreviation of the forex pairs to
     be analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param year: string of the year to be analyzed (i.e '2016').
    :return: tuple -- The function returns a tuple with numpy arrays.
    """

    function_name = hist_self_response_year_avg_responses_trade_data.__name__
    hist_data_tools_avg_responses \
        .hist_function_header_print_data(function_name, '', year, '')

    results_avg = []

    for fx_pair in fx_pairs:
        response = np.zeros(__tau__)
        for fx_p in fx_pair:
            # Load data
            response += pickle.load(open(
                f'../../hist_data/responses_trade_{year}/hist_fx_self_response'
                + f'_year_responses_trade_data/{fx_p}/hist_fx_self_response'
                + f'_year_responses_trade_data_{fx_p}_{year}.pickle', 'rb'))

        avg_response = response / len(ticker)
        results_avg.append(avg_response)

    results_avg = tuple(results_avg)

    # Saving data
    hist_data_tools_avg_responses \
        .hist_save_data(function_name, results_avg, '', year, '')

    return results_avg

# ----------------------------------------------------------------------------


def hist_fx_self_response_year_avg_responses_physical_data(fx_pairs, year):
    """Computes the avg self-response for groups of tickers in a year.

    :param fx_pairs: list of strings of the abbreviation of the forex pairs to
     be analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param year: string of the year to be analyzed (i.e '2016').
    :return: tuple -- The function returns a tuple with numpy arrays.
    """

    function_name = hist_self_response_year_avg_responses_physical_data.__name__
    hist_data_tools_avg_responses
        .hist_function_header_print_data(function_name, '', year, '')

    results_avg = []

    for fx_pair in fx_pairs:
        response = np.zeros(__tau__)
        for fx_p in fx_pair:
            # Load data
            response += pickle.load(open(
                f'../../hist_data/responses_physical_{year}/hist_fx_self'
                + f'_response_year_responses_physical_data/{fx_p}/hist_fx_self'
                + f'_response_year_responses_physical_data_{fx_p}_{year}'
                + f'.pickle', 'rb'))

        avg_response = response / len(ticker)
        results_avg.append(avg_response)

    results_avg = tuple(results_avg)

    # Saving data
    hist_data_tools_avg_responses \
        .hist_save_data(function_name, results_avg, '', year, '')

    return results_avg

# ----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

    pass

    return None

# ----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
