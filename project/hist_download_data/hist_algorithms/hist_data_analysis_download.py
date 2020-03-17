'''Hist data analysis module.

The functions in the module download tick data quotes from www.histdata.com for
a year.

This script requires the following modules:
    * os
    * selenium

The module contains the following functions:
    * gain_fx_year_data_extraction - extracts the bid and ask for a year.
    * gain_fx_midpoint_year_data_extraction - extracts the midpoint price for a
     year
    * gain_fx_trade_signs_year_data_extraction - extracts the midpoint price
     for a year
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

import os
import pyvirtualdisplay
from selenium import webdriver

import hist_data_tools_download

# -----------------------------------------------------------------------------


def hist_download_data(fx_pair, year):
    """Downloads the hist data for a year for a forex pair.

    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e. '2016').
    :return: None -- The function saves the data and does not return a value.
    """

    fx_pair_sep = fx_pair.split('_')
    pair = fx_pair_sep[0] + fx_pair_sep[1]

    if (not os.path.isdir(f'../../hist_data/original_data_{year}/{fx_pair}/')):

        try:
            os.mkdir(f'../../hist_data/original_data_{year}/{fx_pair}/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    for month in range(1, 2):

        url = f'http://www.histdata.com/download-free-forex-historical' \
            + f'-data/?/ascii/tick-data-quotes/{pair}/{year}/{month}'
        print(url)

        # To prevent downloading the dialog
        # profile = webdriver.FirefoxProfile(executable_path=r'/home/tp/jchenaol/bin/geckodriver')
        profile = webdriver.FirefoxProfile()
        # Custom location
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.download.manager.showWhenStarting',
                               False)
        profile.set_preference('browser.download.dir', f'/scratch/jchenaol/forex/project/hist_data/original_data_{year}/{fx_pair}')
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                               'application/x-gzip')

        browser = webdriver.Firefox(profile)
        browser.get(url)

        browser.find_element_by_id('a_file').click()

        # browser.quit()


    return None


# -----------------------------------------------------------------------------


def gain_fx_year_data_extraction(fx_pair, year):
    """Extracts the bid and ask for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e. '2016').
    :return: pandas dataframe -- The function returns a pandas dataframe with
     the data.
    """

    function_name = gain_fx_year_data_extraction.__name__
    gain_data_tools_data_extraction \
        .gain_function_header_print_data(function_name, fx_pair, year, '')

    fx_data_col = ['lTid', 'cDealable', 'CurrencyPair', 'RateDateTime',
                   'RateBid', 'RateAsk']
    fx_data = pd.DataFrame(columns=fx_data_col)

    for m_num in range(1,13):

        if (m_num < 10):
            m_num = f'0{m_num}'

        for w_num in range(1,6):

            try:
                fx_data = fx_data.append(pd.read_csv(
                    f'../../gain_data/original_data_{year}/{fx_pair}_{year}/'
                    + f'{fx_pair}_{year}{m_num}_w{w_num}.zip'))

            except FileNotFoundError as e:
                print('No data')
                print(e)
                print()

    fx_data.index = pd.to_datetime(fx_data['RateDateTime'])

    # Saving data
    gain_data_tools_data_extraction \
        .gain_save_data(function_name, fx_data, fx_pair, year, '')

    return fx_data

# -----------------------------------------------------------------------------


def gain_fx_midpoint_year_data_extraction(fx_pair, year):
    """Extracts the midpoint price for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e. '2016').
    :return: tuple -- The function returns a tuple with numpy arrays.
    """

    function_name = gain_fx_midpoint_year_data_extraction.__name__
    gain_data_tools_data_extraction \
        .gain_function_header_print_data(function_name, fx_pair, year, '')

    try:
        # Load data
        fx_data = pickle.load(open(
                        f'../../gain_data/data_extraction_{year}/gain_fx_year'
                        + f'_data_extraction/gain_fx_year_data_extraction'
                        + f'_{year}_{fx_pair}.pickle', 'rb'))

        time = fx_data['RateDateTime'].to_numpy()
        ask = fx_data['RateAsk'].to_numpy()
        bid = fx_data['RateBid'].to_numpy()

        midpoint = (ask + bid) / 2

        # Saving data
        gain_data_tools_data_extraction \
            .gain_save_data(function_name, (time, midpoint), fx_pair, year, '')

        return (time, midpoint)

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        return None

# -----------------------------------------------------------------------------


def gain_fx_trade_signs_year_data_extraction(fx_pair, year):
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

    function_name = gain_fx_trade_signs_year_data_extraction.__name__
    gain_data_tools_data_extraction \
        .gain_function_header_print_data(function_name, fx_pair, year, '')

    try:
        # Load data
        time, midpoint = pickle.load(open(
                        f'../../gain_data/data_extraction_{year}/gain_fx'
                        + f'_midpoint_year_data_extraction/gain_fx_midpoint'
                        + f'_year_data_extraction_{year}_{fx_pair}.pickle',
                        'rb'))

        trade_signs = 0 * midpoint

        for m_idx, m_val in enumerate(midpoint):

            sign = np.sign(m_val - midpoint[m_idx - 1])
            if (sign):
                trade_signs[m_idx] = sign
            else:
                trade_signs[m_idx] = trade_signs[m_idx - 1]

        assert np.sum(trade_signs == 0) == 0

        # Saving data
        gain_data_tools_data_extraction \
            .gain_save_data(function_name, (time, trade_signs), fx_pair, year,
                            '')

        return (time, trade_signs)

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

    hist_download_data('gbp_usd', '2016')

    return None

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()