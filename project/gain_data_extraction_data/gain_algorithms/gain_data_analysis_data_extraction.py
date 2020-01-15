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

    :param fx_pair: string of the abbreviation of the forex pair to be analized
     (i.e. 'eur_usd').
    :param year: string of the year to be analized (i.e. '2016').
    :param month: string of the month to be analized (i.e. '01').
    :return: pandas dataframe -- The function returns a pandas dataframe with
     the data.
    """

    fx_files_ = sorted(os.listdir(f'../data/eur_usd_{year}_{month}/'))
    fx_files = list(map(lambda each:each.strip('.zip'), fx_files_))
    fx_pair_upper = fx_pair.upper()

    fx_data = pd.read_csv(f'../data/{fx_pair}_{year}_{month}/{fx_pair_upper}_Week1.zip')

    for m_num in range(1,13):
        for w_num in range(2,6):

            try:
                fx_data = fx_data.append(pd.read_csv(f'../data/{fx_pair}_{year}_{month}/{fx_pair_upper}_Week{w_num}.zip'))
            except FileNotFoundError as e:
                print('No data')
                print(e)
                print()

    fx_data.index = pd.to_datetime(fx_data['RateDateTime'])

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