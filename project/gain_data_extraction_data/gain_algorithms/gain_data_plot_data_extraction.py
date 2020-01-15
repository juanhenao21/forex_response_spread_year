'''ITCH data plot module.

The functions in the module plot the data obtained in the
itch_data_analysis_data_extraction module.

This script requires the following modules:
    * matplotlib
    * pickle
    * itch_data_tools_data_extract

The module contains the following functions:
    * itch_midpoint_second_plot - plots the midpoint price in second scale for
     a day.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# ----------------------------------------------------------------------------
# Modules

from matplotlib import pyplot as plt
import pickle

import itch_data_tools_data_extraction

# ----------------------------------------------------------------------------


def itch_midpoint_second_plot(ticker, dates):
    """Plots the midpoint price in second scale for a day.

    :param ticker: string of the abbreviation of the stock to be analized
     (i.e. 'AAPL').
    :param dates: list of strings with the date of the data to be extracted
     (i.e. ['2008-01-02', '2008-01-03]).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    year_ = dates[0].split('-')[0]

    try:
        function_name = itch_midpoint_second_plot.__name__
        itch_data_tools_data_extraction \
            .itch_function_header_print_plot(function_name, ticker, ticker,
                                             year_, '', '')

        figure = plt.figure(figsize=(16, 9))

        for date in dates:

            date_sep = date.split('-')
            year = date_sep[0]
            month = date_sep[1]
            day = date_sep[2]

            # Load data
            time, midpoint = pickle.load(open(
                            f'../../itch_data/data_extraction_{year}/itch_'
                            + f'midpoint_second_data/itch_midpoint_second_data'
                            + f'_{year}{month}{day}_{ticker}.pickle', 'rb'))

            plt.plot(time, midpoint, linewidth=5, label=f'{date}')
            plt.legend(loc='best', fontsize=25)
            plt.title(f'ITCH Midpoint price - {ticker}', fontsize=40)
            plt.xlabel(r'Time $[s]$', fontsize=35)
            plt.ylabel(r'$m(t)$', fontsize=35)
            plt.xticks(fontsize=25)
            plt.yticks(fontsize=25)

        plt.grid(True)
        plt.tight_layout()

        # Plotting
        itch_data_tools_data_extraction \
            .itch_save_plot(function_name, figure, ticker, ticker, year, '')

        return None

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

    pass

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
