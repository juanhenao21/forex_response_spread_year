'''HIST data plot module.

The functions in the module plot the data obtained in the
hist_data_analysis_responses_physical module.

This script requires the following modules:
    * gc
    * pickle
    * typing
    * matplotlib
    * hist_data_tools_data_extract

The module contains the following functions:
    * hist_fx_self_response_year_avg_responses_physical_plot - plots the
      self-response average for a year.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# ----------------------------------------------------------------------------
# Modules

import gc
import pickle

from matplotlib import pyplot as plt  # type: ignore
import numpy as np  # type: ignore

import hist_data_tools_responses_physical

# ----------------------------------------------------------------------------


def hist_fx_self_response_year_avg_responses_physical_plot(
        fx_pair: str, year: str) -> None:
    """Plots the self-response average for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        function_name: str = \
            hist_fx_self_response_year_avg_responses_physical_plot.__name__
        hist_data_tools_responses_physical \
            .hist_function_header_print_plot(function_name, fx_pair, year, '')

        fx_pair_upper: str = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()

        figure: plt.Figure = plt.figure(figsize=(16, 9))

        # Load data
        self_response: np.ndarray = pickle.load(open(
                        f'../../hist_data/responses_physical_{year}/hist_fx'
                        + f'_self_response_year_responses_physical_data/'
                        + f'{fx_pair}/hist_fx_self_response_year_responses'
                        + f'_physical_data_{fx_pair}_{year}.pickle', 'rb'))

        plt.semilogx(self_response, linewidth=5, label=f'{fx_pair_upper}')
        plt.legend(loc='best', fontsize=25)
        plt.title(f'HIST data self-response', fontsize=40)
        plt.xlabel(r'$\tau \, [trades]$', fontsize=35)
        plt.ylabel(r'$R_{ii}(\tau)$', fontsize=35)
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)
        plt.xlim(1, 1000)
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        plt.grid(True)
        plt.tight_layout()

        # Plotting
        hist_data_tools_responses_physical \
            .hist_save_plot(function_name, figure, fx_pair, year, '')

        plt.close()
        del self_response
        del figure
        gc.collect()

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
