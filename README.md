# Price response function and spread impact analysis in foreign exchange markets

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://forex-response-spread-year.readthedocs.io/en/latest/)

In this repository, I analyze the price response functions of the foreign
exchange market data for different years,

I use the same methodology from my work in the project
[Price response function and spread impact analysis in correlated financial markets](https://github.com/juanhenao21/financial_response_spread_year) to compute all the
analysis. From the data I obtain the midpoint prices, trade signs and
self-responses for different forex pairs.

Based on these values, I analyze responses functions in trade time scale
([hist_responses_trade](https://github.com/juanhenao21/forex_response_spread_year/tree/master/project/hist_responses_trade/hist_algorithms)),
physical time scale
([hist_responses_physical](https://github.com/juanhenao21/forex_response_spread_year/tree/master/project/hist_responses_physical/hist_algorithms))
and the impact of the spread
([hist_avg_responses](https://github.com/juanhenao21/forex_response_spread_year/tree/master/project/hist_avg_responses/hist_algorithms))
in the strength of the response functions in trade and physical time scale.

All the results and figures obtained using the modules in the repository will
be saved in the folders
`forex_response_spread_year/project/hist_data` and
`forex_response_spread_year/project/hist_plot`.

You can find
[here](https://forex-response-spread-year.readthedocs.io/en/latest/)
a detailed documentation of the code.

## Getting Started

The main code is implemented in `Python`. We use tick data in generic ASCII
format from
[HistData.com](http://www.histdata.com/download-free-forex-data/?/ascii/tick-data-quotes)

### Prerequisites

For `Python`, all the packages needed to run the analysis are in the
`requirements.txt` file.

## Running the code

The first step is to clone the repository

```bash
$ git clone https://github.com/juanhenao21/forex_response_spread_year.git
```

To install all the needed `Python` packages I recommend to create a virtual
environment and install them from the `requirements.txt` file. To install the
packages from terminal, you can use

```bash
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Download forex data

To download the forex data, you need to move (cd) to the folder
`forex_response_spread_year/project/hist_download_data/hist_algorithms/`.

If you want to get my results, you just need to run the module
`hist_data_main_download.py`. If you want to select other years or forex pairs
you have to change all the contents of the main function and add the following

```Python
hist_data_tools_download.hist_initial_message()
# Years you want to analyze
years: List[str] = ['2018', '2019']
# Forex pairs you want to analyze
fx_pairs: List[str] = ['eur_usd', 'gbp_usd']
# Basic folders
hist_data_tools_download.hist_start_folders(fx_pairs, years)
# Run analysis
# Download data
hist_download_all_data(fx_pairs, years)
```

In any case, you need to run the module. In Linux, using the terminal the
command looks like

```bash
$ python3 hist_data_main_download.py
```

The program will download the data from the corresponding forex pairs.

### Forex price responses functions

The forex price response functions can be obtained in two time scales: trade
and physical time scale. In the following sections I describe in detail how
to run both.

#### Trade time scale

##### Data extraction

To extract the midpoint price and the trade signs from the data, you need to
move (cd) to the folder
`forex_response_spread_year/project/hist_data_extraction/hist_algorithms/`.

If you want to get my results, you just need to run the module
`hist_data_main_extraction`. If you want to select other years or forex pairs
you have to change all the contents of the main function and add the following

```Python
hist_data_tools_extraction.hist_initial_message()
# Years you want to analyze
years: List[str] = ['2018', '2019']
# Forex pairs you want to analyze
fx_pairs: List[str] = ['eur_usd', 'gbp_usd']
# Basic folders
hist_data_tools_extraction.hist_start_folders(fx_pairs, years)
# Run analysis
# Download data
hist_data_plot_generator(fx_pairs, years)
```

In any case, you need to run the module. In Linux, using the terminal the
command looks like

```bash
$ python3 hist_data_main_extraction.py
```

The program will compute the values from the corresponding forex pairs.

##### Price response functions - trade time scale

To compute the price response functions from the data, you need to move (cd) to
the folder
`forex_response_spread_year/project/hist_responses_trade/hist_algorithms/`.

If you want to get my results, you just need to run the module
`hist_data_main_responses_trade`. If you want to select other years or forex
pairs you have to change all the contents of the main function and add the
following

```Python
hist_data_tools_responses_trade.hist_initial_message()
# Years you want to analyze
years: List[str] = ['2018', '2019']
# Forex pairs you want to analyze
fx_pairs: List[str] = ['eur_usd', 'gbp_usd']
# Basic folders
hist_data_tools_responses_trade.hist_start_folders(fx_pairs, years)
# Run analysis
# Download data
hist_data_plot_generator(fx_pairs, years)
```

In any case, you need to run the module. In Linux, using the terminal the
command looks like

```bash
$ python3 hist_data_main_responses_trade.py
```

The program will compute and plot the values from the corresponding forex
pairs.

#### Physical time scale

##### Physical basic data

To run the physical time scale part, you need to have the results from the
trade time scale part.

To compute the midpoint price and the trade signs in physical time scale, you
need to move (cd) to the folder
`forex_response_spread_year/project/hist_physical_basic_data/hist_algorithms/`.

If you want to get my results, you just need to run the module
`hist_data_main_physical_basic_data`. If you want to select other years or
forex pairs you have to change all the contents of the main function and add
the following

```Python
hist_data_tools_physical_basic_data.hist_initial_message()
# Years you want to analyze
years: List[str] = ['2018', '2019']
# Forex pairs you want to analyze
fx_pairs: List[str] = ['eur_usd', 'gbp_usd']
# Basic folders
hist_data_tools_physical_basic_data.hist_start_folders(fx_pairs, years)
# Run analysis
# Download data
hist_data_plot_generator(fx_pairs, years)
```

In any case, you need to run the module. In Linux, using the terminal the
command looks like

```bash
$ python3 hist_data_main_physical_basic_data.py
```

The program will compute the values from the corresponding forex pairs.

##### Price response functions - physical time scale

To compute the price response functions from the data, you need to move (cd) to
the folder
`forex_response_spread_year/project/hist_responses_physical/hist_algorithms/`.

If you want to get my results, you just need to run the module
`hist_data_main_responses_physical`. If you want to select other years or forex
pairs you have to change all the contents of the main function and add the
following

```Python
hist_data_tools_responses_physical.hist_initial_message()
# Years you want to analyze
years: List[str] = ['2018', '2019']
# Forex pairs you want to analyze
fx_pairs: List[str] = ['eur_usd', 'gbp_usd']
# Basic folders
hist_data_tools_responses_physical.hist_start_folders(fx_pairs, years)
# Run analysis
# Download data
hist_data_plot_generator(fx_pairs, years)
```

In any case, you need to run the module. In Linux, using the terminal the
command looks like

```bash
$ python3 hist_data_main_responses_physical.py
```

The program will compute and plot the values from the corresponding forex
pairs.

# VOY AQUI EDITANDO

### TAQ Spread Impact

To run this part of the code, you need to move (cd) to the folder
`financial_response_spread_year/project/taq_avg_spread/taq_algorithms/`
and run the module `taq_data_main_avg_spread.py`. In Linux,
using the terminal the command looks like

```bash
$ python3 taq_data_main_avg_spread.py
```

This analysis is recommended to be done with several stocks. The key point is
that all the stocks used have to have already the self-response function
analysis of the first part (TAQ Responses Physical).

After run the `taq_data_main_avg_spread.py` module, you can move (cd) to the
folder
`financial_response_spread_year/project/taq_avg_responses_physical/taq_algorithms/`
and run the module `taq_data_main_avg_responses_physical.py`. In Linux, using
the terminal the command looks like

```bash
$ python3 taq_data_main_avg_responses_physical.py
```

## Expected results

For the response functions, an increase to a maximum followed by a slowly
decrease is expected.

![Response functions](paper/financial_response_spread_year_paper/figures/03_responses_physical_scale_2008.png)

In the time shift analysis, a change in the relative position between returns
and trade signs can vanish the response function signal.

![Time shift](paper/financial_response_spread_year_paper/figures/04_shift_responses_physical.png)

Dividing the time lag used in the returns, we obtain a short and long
response function, where the short component has a large impact compared with
the long component.

![Short long](paper/financial_response_spread_year_paper/figures/05_short_long_GOOG_MA.png)

Finally, the spread directly impact the strength of the price response
functions. Liquid stocks have smaller price responses.

![Spread impact](paper/financial_response_spread_year_paper/figures/06_spread_impact_2008.png)

## Authors

* **Juan Camilo Henao Londono** - *Initial work* - [Website](https://juanhenao21.github.io)

## Acknowledgments

* Research Group Guhr [Website](http://www.theo.physik.uni-duisburg-essen.de/tp/ags/guhr_dir/index.html)
* DAAD Research Grants - Doctoral Programmes in Germany
