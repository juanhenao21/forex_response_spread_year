.. _hist_download_data:

HIST Download Data
******************

The objective of this part of the code is to download the data to analyze. The
data is obtained from `HistData.com <www.histdata.com>`_. The code use tick
data in generic ASCII format. For the price response function analysis are used
the majors foreign exchange pairs and for the spread impact analysis are used
a combination of majors, crosses and exotic pairs (46 in total).

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
