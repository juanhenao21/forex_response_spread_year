'''HIST data analysis module.

The functions in the module obtain the midpoint price and the trade signs in
physical time scale for HIST Capital in a year.

This script requires the following modules:
    * os
    * pickle
    * typing
    * datetime
    * numpy
    * pandas
    * hist_data_tools_physical_basic_data

The module contains the following functions:
    * hist_fx_physical_data - extracts the midpoint price for a year
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

import pickle
from typing import List

import datetime as dt
import numpy as np  # type: ignore
import pandas as pd  # type: ignore

import hist_data_tools_physical_basic_data

# -----------------------------------------------------------------------------


def hist_fx_physical_data(fx_pair: str, year: str, week: str) -> None:
    """Extracts the midpoint price for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2019').
    :param week: string of the week to be analyzed (i.e. '01').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    try:
        # Load data
        fx_data: pd.DataFrame = pickle.load(open(
                        f'../../hist_data/extraction_data_{year}/hist_fx_data'
                        + f'_extraction_week/{fx_pair}/hist_fx_data_extraction'
                        + f'_week_{fx_pair}_w{week}.pickle', 'rb'))

        fx_data_p = fx_data[['Midpoint', 'Signs']]

        # Days in the week
        dates: List[dt.date] = sorted(set(fx_data.index))
        date_init: dt.date = dates[0]
        date_end: dt.date = dates[-1]

        # First day of the week to be analyzed
        t_init: dt.datetime = dt.datetime(date_init.year, date_init.month,
                                          date_init.day, 17, 10, 0, 0)
        t_init_dict = {'DateTime': t_init, 'Midpoint': np.nan, 'Signs': np.nan}
        t_init_df = pd.DataFrame(t_init_dict, index=[t_init])
        t_init_df.set_index('DateTime', inplace=True)
        fx_data_p = pd.concat([t_init_df, fx_data_p])

        # Last day of the week to be analyzed
        t_end: dt.datetime = dt.datetime(date_end.year, date_end.month,
                                          date_end.day, 16, 50, 1, 0)
        t_end_dict = {'DateTime': t_end, 'Midpoint': np.nan, 'Signs': np.nan}
        t_end_df = pd.DataFrame(t_end_dict, index=[t_end])
        t_end_df.set_index('DateTime', inplace=True)
        fx_data_p = pd.concat([fx_data_p, t_end_df])

        fx_data_p = fx_data_p.asfreq(freq='S', method='ffill')
        fx_data_p = fx_data_p.fillna(method='ffill')
        fx_data_p = fx_data_p.fillna(method='bfill')

        # Saving data
        hist_data_tools_physical_basic_data \
            .hist_save_data(fx_data_p, fx_pair, year, week)

        del fx_data
        del fx_data_p

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
