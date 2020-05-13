'''HIST data main module.

The functions in the module run the complete extraction, analysis and plot of
the HIST data.

This script requires the following modules:
    * typing
    * hist_data_analysis_avg_responses
    * hist_data_plot_avg_responses
    * hist_data_tools_avg_responses

The module contains the following functions:
    * hist_data_plot_generator - generates all the analysis and plots from the
      HIST data.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from typing import List

import hist_data_analysis_avg_responses
import hist_data_plot_avg_responses
import hist_data_tools_avg_responses

# -----------------------------------------------------------------------------


def hist_data_plot_generator(years: List[str]) -> None:
    """Generates all the analysis and plots from the HIST data.

    :param years: List of the strings of the year to be analyzed
     (i.e ['2016', '2017']).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    year: str
    for year in years:

        fx_pairs: List[List[str]] = hist_data_analysis_avg_responses \
            .hist_fx_pair_spread_data(year)

        fx_idx: int
        fx_pair: List[str]
        for fx_idx, fx_pair in enumerate(fx_pairs):
            print(f'GROUP {fx_idx + 1}')
            fx_p: str
            for fx_p in fx_pair:
                print(fx_p)
            print(f'Number of tickers group {fx_idx + 1}: {len(fx_pair)}')
            print()

        hist_data_analysis_avg_responses \
            .hist_fx_self_response_year_avg_responses_trade_data(fx_pairs,
                                                                 year)

        hist_data_analysis_avg_responses \
            .hist_fx_self_response_year_avg_responses_physical_data(fx_pairs,
                                                                    year)

        hist_data_plot_avg_responses \
            .hist_fx_self_response_year_avg_responses_trade_plot(year)

        hist_data_plot_avg_responses \
            .hist_fx_self_response_year_avg_responses_physical_plot(year)

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    hist_data_tools_avg_responses.hist_initial_message()

    # Forex pairs and weeks to analyze
    # Response function analysis
    years: List[str] = ['2011', '2015', '2019']

    # Basic folders
    hist_data_tools_avg_responses.hist_start_folders(years)

    # Run analysis
    # Analysis and plot
    hist_data_plot_generator(years)

    print('Ay vamos!!!')

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
