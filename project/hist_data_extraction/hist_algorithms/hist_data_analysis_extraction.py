'''HIST data analysis module.

The functions in the module extract the bid and ask from the Historic Rate Data
from HIST Capital in a year.

This script requires the following modules:
    * os
    * pickle
    * typing
    * zipfile
    * datetime
    * numpy
    * pandas
    * hist_data_tools_extraction

The module contains the following functions:
    * hist_fx_data_extraction_year - extracts the bid and ask for a year.
    * hist_fx_data_extraction_week - extracts the bid and ask for a week.
    * hist_fx_week_start - extracts data that starts in a week day.
    * hist_fx_weekend_start - extracts data that starts in a weekend day.
    * hist_fx_midpoint_trade_data - extracts the midpoint price for
      a year
    * hist_fx_trade_signs_trade_data - extracts the midpoint price
      for a year
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

import os
import pickle
from typing import Any, Dict, List, Tuple
import zipfile

import datetime as dt
import numpy as np  # type: ignore
import pandas as pd  # type: ignore

import hist_data_tools_extraction

# -----------------------------------------------------------------------------


def hist_fx_data_extraction_year(fx_pair: str, year: str) -> pd.DataFrame:
    """Extracts the bid and ask for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    pair: List[str] = fx_pair.split('_')
    cap_pair: str = pair[0].upper() + pair[1].upper()
    if year == '2008':
        fx_data_col: List[str] = ['DateTime', 'Ask', 'Bid']
        fx_data_type: Dict[str, Any] = {'DateTime': str, 'Ask': float,
                                        'Bid': float}
    else:
        fx_data_col: List[str] = ['DateTime', 'Bid', 'Ask']
        fx_data_type: Dict[str, Any] = {'DateTime': str, 'Bid': float,
                                        'Ask': float}
    fx_data: pd.DataFrame = pd.DataFrame(columns=fx_data_col)

    m_num: int
    for m_num in range(1, 13):

        m_num_str: str
        if m_num < 10:
            m_num_str = f'0{m_num}'
        else:
            m_num_str = f'{m_num}'

        try:
            # Load data
            zip_f: zipfile.ZipFile = zipfile.ZipFile(
                f'../../hist_data/original_data_{year}/{fx_pair}/hist'
                + f'_{fx_pair}_{year}{m_num_str}.zip')
            fx_data = fx_data.append(
                pd.read_csv(zip_f.open(
                    f'DAT_ASCII_{cap_pair}_T_{year}{m_num_str}.csv'),
                            usecols=(0, 1, 2), names=fx_data_col,
                            dtype=fx_data_type), ignore_index=True)

        except FileNotFoundError as error:
            print('No data')
            print(error)
            print()

    # Convert 'DateTime' column to datetime type
    fx_data['DateTime'] = pd.to_datetime(fx_data['DateTime'],
                                         format='%Y%m%d %H%M%S%f')

    return fx_data

# -----------------------------------------------------------------------------


def hist_fx_data_extraction_week(fx_pair: str, year: str) -> None:
    """Extracts the bid and ask for a week.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = hist_fx_data_extraction_week.__name__
    hist_data_tools_extraction \
        .hist_function_header_print_data(function_name, fx_pair, year, '')

    # Year data
    fx_data: pd.DataFrame = hist_fx_data_extraction_year(fx_pair, year)

    # Obtain the dates of every Sunday in the year
    weeks_tup: Tuple[str, ...] = hist_data_tools_extraction.hist_sundays(year)
    # Convert the Sundays dates in datetime type
    weeks: List[dt.datetime] = \
        [dt.datetime.strptime(x, '%Y-%m-%d') for x in weeks_tup]

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

    # Year that not starts with a Saturday or Sunday
    if (weeks[0].day != 1 and weeks[0].day != 2):

        hist_fx_week_start(fx_pair, function_name, year, fx_data, weeks)

    # Year that starts with a Saturday or Sunday
    else:

        hist_fx_weekend_start(fx_pair, function_name, year, fx_data, weeks)

    del fx_data

# -----------------------------------------------------------------------------


def hist_fx_week_start(fx_pair: str, function_name: str, year: str,
                       fx_data: pd.DataFrame,
                       weeks: List[dt.datetime]) -> None:
    """Extracts the bid and ask for a week that starts in a week day.

    :param fx_data: pd.DataFrame with the data.
    :param weeks: List with the dates of the sundays in a year.
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    w_idx: int
    week: dt.datetime
    for w_idx, week in enumerate(weeks):
        if w_idx:
            week_ini: dt.datetime = weeks[w_idx - 1] \
                .replace(hour=17, minute=10, second=0)
            # Five days from Sunday 17h10 to Friday 16h50
            t_secs: int = 432000 - 1200 + 1
            week_fin: dt.datetime = week_ini + dt.timedelta(seconds=t_secs)
            w_df: pd.DataFrame = \
                fx_data[(fx_data['DateTime'] < week_fin)
                        & (fx_data['DateTime'] >= week_ini)]

        else:
            # First week of the year
            week_ini = fx_data['DateTime'].iloc[0].replace(
                hour=17, minute=10, second=0, microsecond=0)
            week_fin = week.replace(
                day=week.day - 2, hour=16, minute=51, second=0)
            w_df = fx_data[(fx_data['DateTime'] < week_fin)
                           & (fx_data['DateTime'] >= week_ini)]

        # Saving data
        w_idx_str: str
        if w_idx + 1 < 10:
            w_idx_str = f'0{w_idx + 1}'
        else:
            w_idx_str = f'{w_idx + 1}'

        pickle.dump(w_df,
                    open(f'../../hist_data/extraction_data_{year}/'
                         + f'{function_name}/{fx_pair}/{function_name}'
                         + f'_{fx_pair}_w{w_idx_str}.pickle', 'wb'))

    # Last days of the year
    week_ini = weeks[-1].replace(hour=17, minute=10, second=0)
    week_fin = fx_data['DateTime'].iloc[-1] \
        .replace(hour=16, minute=51, second=0, microsecond=0)
    w_df = fx_data[(fx_data['DateTime'] < week_fin)
                   & (fx_data['DateTime'] >= week_ini)]
    # Saving data
    pickle.dump(w_df,
                open(f'../../hist_data/extraction_data_{year}/{function_name}/'
                     + f'{fx_pair}/{function_name}_{fx_pair}_w{w_idx + 2}'
                     + f'.pickle', 'wb'))

    del w_df

# -----------------------------------------------------------------------------


def hist_fx_weekend_start(fx_pair: str, function_name: str, year: str,
                          fx_data: pd.DataFrame,
                          weeks: List[dt.datetime]) -> None:
    """Extracts the bid and ask for a weekend that starts in a week day.

    :param fx_data: pd.DataFrame with the data.
    :param weeks: List with the dates of the sundays in a year.
    :return: None -- The function saves the data in a file and does not return
     a value.
    """
    w_idx: int
    for w_idx, _ in enumerate(weeks):
        if w_idx:

            week_ini = weeks[w_idx - 1].replace(hour=17, minute=10,
                                                second=0)
            # Five days from Sunday 17h10 to Friday 16h50
            t_secs = 432000 - 1200 + 1
            week_fin = week_ini + dt.timedelta(seconds=t_secs)
            w_df = fx_data[(fx_data['DateTime'] < week_fin)
                           & (fx_data['DateTime'] >= week_ini)]

            # Saving data
            if w_idx < 10:
                w_idx_str = f'0{w_idx}'
            else:
                w_idx_str = f'{w_idx}'

            pickle.dump(w_df,
                        open(f'../../hist_data/extraction_data_{year}/'
                             + f'{function_name}/{fx_pair}/{function_name}'
                             + f'_{fx_pair}_w{w_idx_str}.pickle', 'wb'))

    # Last days of the year
    week_ini = weeks[-1].replace(hour=17, minute=10, second=0)
    week_fin = fx_data['DateTime'].iloc[-1] \
        .replace(hour=16, minute=51, second=0, microsecond=0)
    w_df = fx_data[(fx_data['DateTime'] < week_fin)
                   & (fx_data['DateTime'] >= week_ini)]
    # Saving data
    pickle.dump(w_df,
                open(f'../../hist_data/extraction_data_{year}/{function_name}/'
                     + f'{fx_pair}/{function_name}_{fx_pair}_w{w_idx + 1}'
                     + f'.pickle', 'wb'))

    del w_df

# -----------------------------------------------------------------------------


def hist_fx_midpoint_trade_data(fx_pair: str, year: str, week: str) -> None:
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

        fx_data['Midpoint'] = (fx_data['Ask'] + fx_data['Bid']) / 2
        fx_data['Spread'] = fx_data['Ask'] - fx_data['Bid']

        # Saving data
        hist_data_tools_extraction.hist_save_data(fx_data, fx_pair, year, week)

        del fx_data

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def hist_fx_trade_signs_trade_data(fx_pair: str, year: str, week: str) -> None:
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

    try:
        # Load data
        fx_data: pd.DataFrame = pickle.load(open(
                        f'../../hist_data/extraction_data_{year}/hist_fx_data'
                        + f'_extraction_week/{fx_pair}/hist_fx_data_extraction'
                        + f'_week_{fx_pair}_w{week}.pickle', 'rb'))

        trade_signs_bef: pd.Series = np.sign(fx_data['Midpoint'].diff())
        trade_signs_bef[trade_signs_bef == 0] =\
            trade_signs_bef[trade_signs_bef == 0] * np.nan
        trade_signs_bef.iloc[0] = 1
        trade_signs: pd.Series = trade_signs_bef.fillna(method='ffill')

        fx_data['Signs'] = trade_signs
        fx_data.set_index('DateTime', inplace=True)

        # Saving data
        hist_data_tools_extraction.hist_save_data(fx_data, fx_pair, year, week)

        del fx_data

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
