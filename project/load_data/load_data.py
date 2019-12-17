'''Load and test data script

The functions in the script load and plot the Historic Rate Data from GAIN
Capital for january 2016.

This script requires the following modules
    * numpy
    * pandas
    * 

The script contains the following functions
    * fx_gain_load - loads the data of the month.
    * fx_gain_plot - plots the data of the month.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd


# -----------------------------------------------------------------------------


def fx_gain_load(fx_pair, year, month):
    """Loads the forex data.

    :param fx_pair: string of the forex pair to be loaded (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e. '2016').
    :param month: string of the month to be analized (i.e. '01').
    :return: pandas dataframe -- The function returns a pandas dataframe with
     the data.
    """

    fx_files_ = sorted(os.listdir('../data/eur_usd_2016_01/'))
    fx_files = list(map(lambda each:each.strip('.zip'), fx_files_))

    fx_data = pd.read_csv('../data/eur_usd_2016_01/EUR_USD_Week1.zip')
    fx_data.index = pd.to_datetime(fx_data['RateDateTime'])
    print(fx_data.head())
    return fx_data

# -----------------------------------------------------------------------------


def fx_gain_plot(fx_data):
    """Plot the forex data.

    :param fx_data: pandas dataframe with the forex data for a forex pair.
    :return: None -- The function save the plot in a file and does not return
     a value.
    """

    figure = plt.figure(figsize=(16,9))
    plt.plot(fx_data['RateBid'])
    plt.plot(fx_data['RateAsk'])
    # plt.plot(fx_data['RateDateTime'], fx_data['RateBid'])
    # plt.plot(fx_data['RateDateTime'], fx_data['RateAsk'])
    plt.grid(True)
    plt.show()

    return None
# -----------------------------------------------------------------------------


def main():

    fx_pair = 'eur_usd'
    year = '2016'
    month = '01'

    fx_data = fx_gain_load(fx_pair, year, month)
    fx_gain_plot(fx_data)

# -----------------------------------------------------------------------------



if __name__ == "__main__":
    main()