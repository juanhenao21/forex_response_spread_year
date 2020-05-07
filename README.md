# Price response function and spread impact analysis in foreign exchange markets

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://forex-response-spread-year.readthedocs.io/en/latest/)

In this repository, I analyze the price response functions of the foreign
exchange market data for different years,

I use the same methodology from my work in the project
[Price response function and spread impact analysis in correlated financial markets](https://github.com/juanhenao21/financial_response_spread_year) to compute all the
analysis. From the data I obtain the midpoint prices, trade signs and
self-responses for different forex pairs.

(MODIFY)
Based on these values, I analyze responses functions in trade time scale
([taq_responses_trade](https://github.com/juanhenao21/financial_response_spread_year/tree/master/project/taq_responses_trade/taq_algorithms))
and the influence of the number of trades in a second in the response functions
([taq_responses_activity](https://github.com/juanhenao21/financial_response_spread_year/tree/master/project/taq_responses_activity/taq_algorithms)).
I also analyze the influence of the time shift between trade signs and midpoint
prices
([taq_physical_shift](https://github.com/juanhenao21/financial_response_spread_year/tree/master/project/taq_physical_shift/taq_algorithms),
[taq_responses_physical_shift](https://github.com/juanhenao21/financial_response_spread_year/tree/master/project/taq_responses_physical_shift/taq_algorithms),
[taq_trade_shift](https://github.com/juanhenao21/financial_response_spread_year/tree/master/project/taq_trade_shift/taq_algorithms)
and
[taq_responses_trade_shift](https://github.com/juanhenao21/financial_response_spread_year/tree/master/project/taq_responses_trade_shift/taq_algorithms)),
the influence of the time lag
([taq_responses_physical_short_long](https://github.com/juanhenao21/financial_response_spread_year/tree/master/project/taq_responses_physical_short_long/taq_algorithms))
in the response functions and the impact of the spread
([taq_avg_responses_physical](https://github.com/juanhenao21/financial_response_spread_year/tree/master/project/taq_avg_responses_physical/taq_algorithms))
in the strength of the response functions.

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

### Forex responses

#### Physical time scale

# VOY AQUI EDITANDO

To run the code from the scratch and reproduce the results in section 2.3 and
2.4 of the
[paper](https://link.springer.com/content/pdf/10.1140/epjb/e2016-60818-y.pdf),
you need to copy the folder `decompress_original_data_2008` to the folder
`financial_response_spread_year/project/taq_data`.
Then you need to create a folder with the name `original_year_data_2008` inside
`financial_response_spread_year/project/taq_data` and move the `.quotes` and
`.trades` files of the tickers you want to analyze. Make sure you move a copy
of the files and not the originals, because when you run the code, it will
delete these files to free space.

Then, you need to move (cd) to the folder
`financial_response_spread_year/project/taq_responses_physical/taq_algorithms/`
and in the `main()` function of the module
`taq_data_main_responses_physical.py`, edit the tickers list with the stocks
you want to analyze (in this case the symbols of the files of the tickers you
copy in the previous step).

```Python
tickers = ['AAPL', 'MSFT']
```

Finally, you need to run the module. In Linux, using the terminal the command
looks like

```bash
$ python3 taq_data_main_responses_physical.py
```

The program will obtain and plot the data for the corresponding stocks.

#### For the users with the year CSV data files

If you have the CSV data files, you need to create a folder with the name
`csv_year_data_2008` inside `financial_response_spread_year/project/taq_data`,
and move the CSV files inside.  Make sure you move a copy of the files and not
the originals, because when you run the code, it will delete these files to
free space. Then go to the
`financial_response_spread_year/project/taq_responses_physical/taq_algorithms/taq_data_main_responses_physical.py`
file and comment the line in the `main` function

```Python
# taq_build_from_scratch(tickers, year)
```

Edit the tickers list with the stocks you want to analyze (in this case the
symbols of the files of the tickers you copy in the previous step).

```Python
tickers = ['AAPL', 'MSFT']
```

Finally, you need to run the module. In Linux, using the terminal, the command
looks like

```bash
$ python3 taq_data_main_responses_physical.py
```

The program will obtain and plot the data for the corresponding stocks.

All the following analysis depend directly from the results of this section. If
you want to run them, you need to run this section first.

### TAQ Responses Trade

To run this part of the code, you need to move (cd) to the folder
`financial_response_spread_year/project/taq_responses_trade/taq_algorithms/` and run
the module `taq_data_main_responses_trade.py`. In Linux, using the terminal the
command looks like

```bash
$ python3 taq_data_main_responses_trade.py
```

This part of the code is the slowest. I do not recommend to analyze several
stocks in this time scale.

### TAQ Responses Activity

To run this part of the code, you need to move (cd) to the folder
`financial_response_spread_year/project/taq_responses_activity/taq_algorithms/`
and run the module `taq_data_main_responses_activity.py`. In Linux, using the
terminal the command looks like

```bash
$ python3 taq_data_main_responses_trade.py
```

### TAQ Time Shift

The TAQ time shift analysis is divided in two time scales and in two modules.
The modules have to be executed in the order shown.

#### Physical time scale

To run this part of the code, you need to move (cd) to the folder
`financial_response_spread_year/project/taq_physical_shift/taq_algorithms/` and
run the module `taq_data_main_physical_shift.py`. In Linux, using the terminal
the command looks like

```bash
$ python3 taq_data_main_physical_shift.py
```

After run the `taq_data_main_physical_shift.py` module, you can move (cd) to
the folder
`financial_response_spread_year/project/taq_responses_physical_shift/taq_algorithms/`
and run the module `taq_data_main_responses_physical_shift.py`. In Linux, using
the terminal the command looks like

```bash
$ python3 taq_data_main_responses_physical_shift.py
```

#### Trade time scale

To run this part of the code, you need to move (cd) to the folder
`financial_response_spread_year/project/taq_trade_shift/taq_algorithms/` and
run the module `taq_data_main_trade_shift.py`. In Linux, using the terminal the
command looks like

```bash
$ python3 taq_data_main_trade_shift.py
```

After run the `taq_data_main_trade_shift.py` module, you can move (cd) to the
folder
`financial_response_spread_year/project/taq_responses_trade_shift/taq_algorithms/`
and run the module `taq_data_main_responses_trade_shift.py`. In Linux, using
the terminal the command looks like

```bash
$ python3 taq_data_main_responses_trade_shift.py
```

### TAQ Responses Short Long

To run this part of the code, you need to move (cd) to the folder
`financial_response_spread_year/project/taq_responses_physical_short_long/taq_algorithms/`
and run the module `taq_data_main_responses_physical_short_long.py`. In Linux,
using the terminal the command looks like

```bash
$ python3 taq_data_main_responses_physical_short_long.py
```

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
