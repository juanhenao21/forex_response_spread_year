'''HIST data analysis module.

The functions in the module compute the average response function in trade and
physical time scale from the Historic Rate Data from HIST Capital data in a
year.

This script requires the following modules:
    * pickle
    * typing
    * numpy
    * pandas
    * hist_data_tools_avg_responses_physical

The module contains the following functions:
    * hist_tickers_spread_data - obtains the tickers and the spread for the
      classification.
    * hist_self_response_year_avg_responses_trade_data - computes the average
      self response for groups of tickers in a year in trade time scale.
    * hist_self_response_year_avg_responses_physical_data - computes the
      average self response for groups of tickers in a year in physical time
      scale.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# ----------------------------------------------------------------------------
# Modules

import pickle
from typing import List, Tuple

import numpy as np  # type: ignore
import pandas as pd  # type: ignore

import hist_data_tools_avg_responses

__tau__ = 10000

# ----------------------------------------------------------------------------


def hist_fx_pair_spread_data(year: str) -> List[List[str]]:
    """Obtains the tickers and the spread range for the classification.

    :param year: string of the year to be analyzed (i.e. '2016').
    :return: list -- The function returns a list of lists with forex pairs.
    """

    function_name: str = hist_fx_pair_spread_data.__name__
    hist_data_tools_avg_responses \
        .hist_function_header_print_data(function_name, '', year, '')

    try:
        # load data
        spread_data: pd.DataFrame = pd.read_csv(
            f'../../hist_avg_spread/hist_avg_spread_{year}.csv',
            usecols=['FxPair', 'Avg_Spread'])

        fx_pairs: List[List[str]] = []

        group_1: pd.DataFrame = \
            spread_data[spread_data['Avg_Spread'] < 0.6]
        tickers_g1: List[str] = group_1['FxPair'].tolist()
        group_2: pd.DataFrame = \
            spread_data[(spread_data['Avg_Spread'] >= 0.6)
                        & (spread_data['Avg_Spread'] < 7)]
        tickers_g2: List[str] = group_2['FxPair'].tolist()
        group_3: pd.DataFrame = \
            spread_data[(spread_data['Avg_Spread'] >= 7)
                        & (spread_data['Avg_Spread'] < 1000)]
        tickers_g3: List[str] = group_3['FxPair'].tolist()

        fx_pairs.append(tickers_g1)
        fx_pairs.append(tickers_g2)
        fx_pairs.append(tickers_g3)

        return fx_pairs

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()
        raise Exception('Check the CSV file')

# ----------------------------------------------------------------------------


def hist_fx_self_response_year_avg_responses_trade_data(
        fx_pairs: List[List[str]], year: str) -> Tuple[np.ndarray, ...]:
    """Computes the avg self-response for groups of tickers in a year.

    :param fx_pairs: list of lists of strings of the abbreviation of the forex
     pairs to be analyzed
     (i.e. [['eur_usd', 'gbp_usd'], ['aud_usd', 'usd_cad']).
    :param year: string of the year to be analyzed (i.e '2016').
    :return: tuple -- The function returns a tuple with numpy arrays.
    """

    function_name: str = hist_fx_self_response_year_avg_responses_trade_data \
        .__name__
    hist_data_tools_avg_responses \
        .hist_function_header_print_data(function_name, '', year, '')

    results_avg: List[np.ndarray] = []

    fx_pair: List[str]
    fx_p: str
    for fx_pair in fx_pairs:
        response: np.ndarray = np.zeros(__tau__)
        for fx_p in fx_pair:
            # Load data
            response += pickle.load(open(
                f'../../hist_data/responses_trade_{year}/hist_fx_self_response'
                + f'_year_responses_trade_data/{fx_p}/hist_fx_self_response'
                + f'_year_responses_trade_data_{fx_p}_{year}.pickle', 'rb'))

        avg_response: np.ndarray = response / len(fx_pair)
        results_avg.append(avg_response)

    results_avg_tup: Tuple[np.ndarray, ...] = tuple(results_avg)

    # Saving data
    hist_data_tools_avg_responses \
        .hist_save_data(function_name, results_avg_tup, '', year, '')

    return results_avg_tup

# ----------------------------------------------------------------------------


def hist_fx_self_response_year_avg_responses_physical_data(
        fx_pairs: List[List[str]], year: str) -> Tuple[np.ndarray, ...]:
    """Computes the avg self-response for groups of tickers in a year.

    :param fx_pairs: list of lists of strings of the abbreviation of the forex
     pairs to be analyzed
     (i.e. [['eur_usd', 'gbp_usd'], ['aud_usd', 'usd_cad']).
    :param year: string of the year to be analyzed (i.e '2016').
    :return: tuple -- The function returns a tuple with numpy arrays.
    """

    function_name: str = \
        hist_fx_self_response_year_avg_responses_physical_data.__name__
    hist_data_tools_avg_responses \
        .hist_function_header_print_data(function_name, '', year, '')

    results_avg: List[np.ndarray] = []

    fx_pair: List[str]
    fx_p: str
    for fx_pair in fx_pairs:
        response: np.ndarray = np.zeros(__tau__)
        for fx_p in fx_pair:
            # Load data
            response += pickle.load(open(
                f'../../hist_data/responses_physical_{year}/hist_fx_self'
                + f'_response_year_responses_physical_data/{fx_p}/hist_fx_self'
                + f'_response_year_responses_physical_data_{fx_p}_{year}'
                + f'.pickle', 'rb'))

        avg_response: np.ndarray = response / len(fx_pair)
        results_avg.append(avg_response)

    results_avg_tup: Tuple[np.ndarray, ...] = tuple(results_avg)

    # Saving data
    hist_data_tools_avg_responses \
        .hist_save_data(function_name, results_avg_tup, '', year, '')

    return results_avg_tup

# ----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

# ----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
