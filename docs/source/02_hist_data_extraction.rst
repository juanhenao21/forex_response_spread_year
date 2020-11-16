.. _hist_data_extraction:

HIST Data Extraction
********************

This module extracts the information from the data downloaded with the module
:ref:`hist_download_data`. We obtain the time, best ask, best bid, midpoint
price, spread and trade signs in trade time scale.

To run this part of the code is necessary to have the results from the module
:ref:`hist_download_data`.

Modules
=======
The code is divided in four parts:
    * `Tools`_: some functions for repetitive actions.
    * `Analysis`_: code to analyze the data.
    * `Plot`_: code to plot the data.
    * `Main`_: code to run the implementation.

Tools
-----
.. automodule:: hist_data_tools_extraction
   :members:

Analysis
--------
.. automodule:: hist_data_analysis_extraction
   :members:

Plot
----
.. automodule:: hist_data_plot_extraction
   :members:

Main
----
.. automodule:: hist_data_main_extraction
   :members:
