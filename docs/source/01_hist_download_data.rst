.. _hist_download_data:

HIST Download Data
******************

The objective of this part of the code is to download the data to analyze.

The data is obtained from `HistData.com <www.histdata.com>`_. I used tick data
in generic ASCII format. For the response function analysis are used the majors
(EUR/USD, GBP/USD, USD/JPY, USD/CHF, USD/CAD, AUS/USD and NZD/USD) and for the
spread impact analysis are used 66 forex pairs available in the website
(EUR/USD, EUR/CHF, EUR/GBP, EUR/JPY, EUR/AUD, USD/CAD, USD/CHF, USD/JPY,
USD/MXN, GBP/CHF, GBP/JPY, GBP/USD, AUD/JPY, AUD/USD, CHF/JPY, NZD/JPY,
NZD/USD, XAU/USD, EUR/CAD, AUD/CAD, CAD/JPY, EUR/NZD, GRX/EUR, NZD/CAD,
SGD/JPY, USD/HKD, USD/NOK, USD/TRY, XAU/AUD, AUD/CHF, AUX/AUD, EUR/HUF,
EUR/PLN, FRX/EUR, HKX/HKD, NZD/CHF, SPX/USD, USD/HUF, USD/PLN, USD/ZAR,
XAU/CHF, ZAR/JPY, BCO/USD, ETX/EUR, EUR/CZK, EUR/SEK, GBP/AUD, GBP/NZD,
JPX/JPY, UDX/USD, USD/CZK, USD/SEK, WTI/USD, XAU/EUR, AUD/NZD, CAD/CHF,
EUR/DKK, EUR/NOK, EUR/TRY, GBP/CAD, NSX/USD, UKX/GBP, USD/DKK, USD/SGD,
XAG/USD, XAU/GBP)

Modules
=======
The code is divided in two parts:
    * `Tools`_: some functions for repetitive actions.
    * `Main`_: code to run the implementation.

Tools
-----
.. automodule:: hist_data_tools_download
   :members:

Main
----
.. automodule:: hist_data_main_download
   :members:
