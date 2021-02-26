'''HIST spread impact figures

Plots the figures of the spread impact responses for the paper

This script requires the following modules:
    * matplotlib
    * pickle
    * typing
    * numpy

The module contains the following functions:
    * hist_response_year_avg_responses_plot - plots the spread impact
      responses for a year.
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

def hist_response_year_avg_responses_plot(years: List[str]) -> None:
    """Plots the response average for different years.

    :param year: list of strings of the years to be analyzed
     (i.e. ['2016', '2019']).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        figure, axs = plt.subplots(2, 3, sharex=True, figsize=(16, 9))

        markers: List = ['-o', '-^', '-s']

        year: str
        for idx, year in enumerate(years):

            # Load data
            resp_g1_t, resp_g2_t, resp_g3_t = pickle.load(open(
                f'../../project/hist_data/avg_responses_data_{year}/hist_fx_self_response'
                + f'_year_avg_responses_trade_data/hist_fx_self_response_year_avg'
                + f'_responses_trade_data_{year}_.pickle', 'rb'))
            resp_g1_p, resp_g2_p, resp_g3_p = pickle.load(open(
                f'../../project/hist_data/avg_responses_data_{year}/hist_fx_self_response'
                + f'_year_avg_responses_physical_data/hist_fx_self_response_year'
                + f'_avg_responses_physical_data_{year}_.pickle', 'rb'))

            axs[0, idx].semilogx(resp_g1_t, markers[0], ms=10,
                                 label=f'Group 1')
            axs[0, idx].semilogx(resp_g2_t, markers[1], ms=10,
                                 label=f'Group 2')
            axs[0, idx].semilogx(resp_g3_t, markers[2], ms=10,
                                 label=f'Group 3')

            # axs[idx, 0].legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3,
            #         fontsize=30)
            axs[0, idx].set_title(f'{year}', fontsize=15)
            axs[0, idx].set_xlabel(r'$\tau \, [trades]$', fontsize=13)
            axs[0, idx].set_ylabel(r'$R^{\left(t\right)}_{ii}(\tau)$', fontsize=15)
            axs[0, idx].tick_params(axis='x', labelsize=10)
            axs[0, idx].tick_params(axis='y', labelsize=10)
            axs[0, idx].set_xlim(1, __tau__)
            # axs[0, idx].ylim(19.5 * 10 ** -5, 32.5 * 10 ** -5)
            axs[0, idx].ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
            axs[0, idx].yaxis.offsetText.set_fontsize(10)
            axs[0, idx].grid(True)

            axs[1, idx].semilogx(resp_g1_p, markers[0], ms=10,
                                 label=f'Group 1')
            axs[1, idx].semilogx(resp_g2_p, markers[1], ms=10,
                                 label=f'Group 2')
            axs[1, idx].semilogx(resp_g3_p, markers[2], ms=10,
                                 label=f'Group 3')

            # axs[1, idx].legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3,
            #                    fontsize=15)
            # axs[1, idx].set_title(f'{year}', fontsize=15)
            axs[1, idx].set_xlabel(r'$\tau \, [s]$', fontsize=13)
            axs[1, idx].set_ylabel(r'$R^{\left(p\right)}_{ii}(\tau)$', fontsize=15)
            axs[1, idx].tick_params(axis='x', labelsize=10)
            axs[1, idx].tick_params(axis='y', labelsize=10)
            axs[1, idx].set_xlim(1, __tau__)
            # axs[0, idx].ylim(19.5 * 10 ** -5, 32.5 * 10 ** -5)
            axs[1, idx].ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
            axs[1, idx].yaxis.offsetText.set_fontsize(10)
            axs[1, idx].grid(True)

        axs[1, 1].legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3,
                           fontsize=12)

        plt.tight_layout()

        # Save Plot
        figure.savefig(f'../plot/05_spread_impact.png')

        return None

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        return None

# ----------------------------------------------------------------------------


def main():

    years: List[str] = ['2011', '2015', '2019']

    hist_response_year_avg_responses_plot(years)

    return None

# ----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
