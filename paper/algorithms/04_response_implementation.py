'''HIST data response implementation.

Plots the figures of the response implementation for the paper.

This script requires the following modules:
    * matplotlib
    * pickle
    * typing
    * numpy

The module contains the following functions:
    * hist_trade_scale_response_year_avg_plot - plots the average response for
      a year in trade time scale.
    * hist_physical_scale_response_year_avg_plot - plots the average response
      for a year in physical time scale.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# ----------------------------------------------------------------------------
# Modules

import pickle
from typing import List

from matplotlib import pyplot as plt  #type: ignore
import numpy as np  #type: ignore

__tau__ = 1000

# ----------------------------------------------------------------------------


def hist_trade_scale_response_year_avg_plot(
        fx_pairs: List[str], symbols: List[str], years: List[str]) -> None:
    """Plots the avg response for a year in trade time scale.

    :param fx_pairs: list of strings of the abbreviation of the forex pairs to
     be analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param years: list of strings of the years to be analyzed
     (i.e. ['2016', '2019']).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        figure: plt.Figure = plt.figure(figsize=(6, 16))
        ax1: plt.subplot = plt.subplot(3, 1, 1)
        ax2: plt.subplot = plt.subplot(3, 1, 2)
        ax3: plt.subplot = plt.subplot(3, 1, 3)

        ax_plot: List[plt.subplot] = [ax1, ax2, ax3]

        fx_pair: str
        year: str

        for idx, year in enumerate(years):
            for fx_idx, fx_pair in enumerate(fx_pairs):

                # Load data
                resp: np.ndarray = pickle.load(
                    open(f'../../project/hist_data/responses_trade_{year}/hist'
                         + f'_fx_self_response_year_responses_trade_data/'
                         + f'{fx_pair}/hist_fx_self_response_year_responses'
                         + f'_trade_data_{fx_pair}_{year}.pickle', 'rb'))

                ax_plot[idx].semilogx(resp, linewidth=5,
                                      label=f'{symbols[fx_idx]}')

        ax1.set_title(f'{years[0]}', fontsize=15)
        ax1.set_xlabel(r'$\tau \, [trades]$', fontsize=15)
        ax1.set_ylabel(r'$R^{\left(t\right)}_{ii}(\tau)$', fontsize=15)
        ax1.tick_params(axis='x', labelsize=10)
        ax1.tick_params(axis='y', labelsize=10)
        ax1.set_xlim(1, __tau__)
        # plt.ylim(13 * 10 ** -5, 16 * 10 ** -5)
        ax1.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        ax1.yaxis.offsetText.set_fontsize(10)
        ax1.grid(True)

        ax2.set_title(f'{years[1]}', fontsize=15)
        ax2.set_xlabel(r'$\tau \, [trades]$', fontsize=15)
        ax2.set_ylabel(r'$R^{\left(t\right)}_{ii}(\tau)$', fontsize=15)
        ax2.tick_params(axis='x', labelsize=10)
        ax2.tick_params(axis='y', labelsize=10)
        ax2.set_xlim(1, __tau__)
        # plt.ylim(13 * 10 ** -5, 16 * 10 ** -5)
        ax2.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        ax2.yaxis.offsetText.set_fontsize(10)
        ax2.grid(True)

        ax3.set_title(f'{years[2]}', fontsize=15)
        ax3.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3,
                   fontsize=13)
        ax3.set_xlabel(r'$\tau \, [trades]$', fontsize=15)
        ax3.set_ylabel(r'$R^{\left(t\right)}_{ii}(\tau)$', fontsize=15)
        ax3.tick_params(axis='x', labelsize=10)
        ax3.tick_params(axis='y', labelsize=10)
        ax3.set_xlim(1, __tau__)
        # plt.ylim(13 * 10 ** -5, 16 * 10 ** -5)
        ax3.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        ax3.yaxis.offsetText.set_fontsize(10)
        ax3.grid(True)

        plt.tight_layout()

        # Save Plot
        figure.savefig(f'../plot/04_responses_trade_scale.png')

        return None

    except FileNotFoundError as error:
        print('No data')
        print(error)
        return None

# ----------------------------------------------------------------------------


def hist_physical_scale_response_year_avg_plot(
        fx_pairs: List[str], symbols: List[str], years: List[str]) -> None:
    """Plots the avg response for a year in physical time scale.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. ['eur_usd', 'gbp_usd']).
    :param year: string of the year to be analyzed (i.e. ['2016', '2019']).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        figure: plt.Figure = plt.figure(figsize=(6, 16))
        ax1: plt.subplot = plt.subplot(3, 1, 1)
        ax2: plt.subplot = plt.subplot(3, 1, 2)
        ax3: plt.subplot = plt.subplot(3, 1, 3)

        ax_plot: List[plt.subplot] = [ax1, ax2, ax3]

        fx_pair: str
        year: str

        for idx, year in enumerate(years):
            for fx_idx, fx_pair in enumerate(fx_pairs):

                # Load data
                resp: np.ndarray = pickle.load(
                    open(f'../../project/hist_data/responses_physical_{year}/'
                         + f'hist_fx_self_response_year_responses_physical'
                         + f'_data/{fx_pair}/hist_fx_self_response_year'
                         + f'_responses_physical_data_{fx_pair}_{year}.pickle',
                         'rb'))

                ax_plot[idx].semilogx(resp, linewidth=5,
                                      label=f'{symbols[fx_idx]}')

        ax1.set_title(f'{years[0]}', fontsize=15)
        ax1.set_xlabel(r'$\tau \, [s]$', fontsize=15)
        ax1.set_ylabel(r'$R^{\left(p\right)}_{ii}(\tau)$', fontsize=15)
        ax1.tick_params(axis='x', labelsize=10)
        ax1.tick_params(axis='y', labelsize=10)
        ax1.set_xlim(1, __tau__)
        # plt.ylim(13 * 10 ** -5, 16 * 10 ** -5)
        ax1.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        ax1.yaxis.offsetText.set_fontsize(10)
        ax1.grid(True)

        ax2.set_title(f'{years[1]}', fontsize=15)
        ax2.set_xlabel(r'$\tau \, [s]$', fontsize=15)
        ax2.set_ylabel(r'$R^{\left(p\right)}_{ii}(\tau)$', fontsize=15)
        ax2.tick_params(axis='x', labelsize=10)
        ax2.tick_params(axis='y', labelsize=10)
        ax2.set_xlim(1, __tau__)
        # plt.ylim(13 * 10 ** -5, 16 * 10 ** -5)
        ax2.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        ax2.yaxis.offsetText.set_fontsize(10)
        ax2.grid(True)

        ax3.set_title(f'{years[2]}', fontsize=15)
        ax3.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3,
                   fontsize=13)
        ax3.set_xlabel(r'$\tau \, [s]$', fontsize=15)
        ax3.set_ylabel(r'$R^{\left(p\right)}_{ii}(\tau)$', fontsize=15)
        ax3.tick_params(axis='x', labelsize=10)
        ax3.tick_params(axis='y', labelsize=10)
        ax3.set_xlim(1, __tau__)
        # plt.ylim(13 * 10 ** -5, 16 * 10 ** -5)
        ax3.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        ax3.yaxis.offsetText.set_fontsize(10)
        ax3.grid(True)

        plt.tight_layout()

        # Save Plot
        figure.savefig(f'../plot/04_responses_physical_scale.png')

    except FileNotFoundError as error:
        print('No data')
        print(error)

# ----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

    fx_pairs: List[str] = ['eur_usd', 'gbp_usd', 'usd_jpy', 'aud_usd',
                           'usd_chf', 'usd_cad', 'nzd_usd']
    symbols: List[str] = ['EUR/USD', 'GBP/USD', 'USD/JPY', 'AUD/USD',
                          'USD/CHF', 'USD/CAD', 'NZD/USD']
    years: List[str] = ['2008', '2014', '2019']

    hist_trade_scale_response_year_avg_plot(fx_pairs, symbols, years)
    hist_physical_scale_response_year_avg_plot(fx_pairs, symbols, years)

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
