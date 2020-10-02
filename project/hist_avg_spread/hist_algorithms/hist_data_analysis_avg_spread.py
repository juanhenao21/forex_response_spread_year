'''HIST data analysis module.

The functions in the module analyze the statistics from the NASDAQ stock
market and compute the average spread of the stocks.

This script requires the following modules:
    * itertools.product
    * multiprocessing
    * numpy
    * pandas
    * pickle
    * hist_data_tools_avg_spread

The module contains the following functions:
    * hist_quotes_trades_day_avg_spread_data - statistics of quotes and trades
      for a day.
    * hist_quotes_trades_year_avg_spread_data - statistics of quotes and trades
      for a year.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# ----------------------------------------------------------------------------
# Modules

from itertools import product as iprod
import multiprocessing as mp
import pickle
from typing import Any, Iterator, List, Tuple

import numpy as np  # type: ignore
import pandas as pd  # type: ignore

import hist_data_tools_avg_spread

# ----------------------------------------------------------------------------


def hist_quotes_trades_day_avg_spread_data(
        fx_pair: str, year: str, week: str) -> Tuple[Any, Any]:
    """Obtain the quotes and trades statistics for a week.

    Using the quotes files, obtain the statistics of the average spread, number
    of quotes and number of trades for a day.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e '2016').
    :param week: string of the week to be analyzed (i.e. '16').
    :return: tuple -- The function returns a tuple with float values.
    """

    try:
        # Load data
        fx_data: pd.DataFrame = pickle.load(open(
                        f'../../hist_data/extraction_data_{year}/hist_fx'
                        + f'_data_extraction/{fx_pair}/hist_fx_data_extraction'
                        + f'_{fx_pair}_w{week}.pickle', 'rb'))

        if ('JPY' in fx_pair or
            'CZK' in fx_pair or
            'HUF' in fx_pair or
            'MXN' in fx_pair or
            'ZAR' in fx_pair):
            spread: np.ndarray = fx_data['Spread'].to_numpy() * 100
            print(fx_pair)
        else:
            spread: np.ndarray = fx_data['Spread'].to_numpy() * 1000

        num_quotes: int = len(spread)
        avg_spread: float = np.mean(spread)

        return (num_quotes, avg_spread)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()
        return (np.NaN, np.NaN)

# ----------------------------------------------------------------------------


def hist_quotes_trades_year_avg_spread_data(fx_pairs: List[str],
                                            year: str) -> None:
    """Obtain the quotes and trades statistics for a year.

    Using the hist_quotes_trades_day_avg_spread_data function computes the
    statistics of the average spread, number of quotes and number of trades
    for a year.

    :param fx_pairs: list of the string abbreviation of the fx pairs to be
     analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param year: String of the years to be analyzed (i.e '2016').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = hist_quotes_trades_year_avg_spread_data.__name__

    # Pandas DataFrame to store the data
    spread_stats: pd.DataFrame = pd.DataFrame(
        columns=['FxPair', 'Avg_Quotes', 'Avg_Spread'])

    weeks: Tuple[str, ...] = hist_data_tools_avg_spread.hist_weeks()

    idx: int
    fx_pair: str
    for idx, fx_pair in enumerate(fx_pairs):

        hist_data_tools_avg_spread \
            .hist_function_header_print_data(function_name, fx_pair, year, '')

        stat: List[Any] = []
        args_prod: Iterator[Tuple[str, ...]] = iprod([fx_pair], [year], weeks)

        # Parallel computation of the statistics. Every result is appended to
        # a list
        with mp.Pool(processes=mp.cpu_count()) as pool:
            stat.append(pool.starmap(hist_quotes_trades_day_avg_spread_data,
                                     args_prod))

        # To obtain the average of the year, I average all the results of the
        # corresponding values (number quotes, trades and avg spread)
        stat_year: List[str] = list(np.nanmean(stat[0], axis=0))
        spread_stats.loc[idx] = [fx_pair] + stat_year

    spread_stats.sort_values(by='Avg_Spread', inplace=True)
    spread_stats.to_csv(f'../hist_avg_spread_{year}.csv')
    print(spread_stats)

# ----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

# ----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
