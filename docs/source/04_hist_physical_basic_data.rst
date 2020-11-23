.. _hist_physical_basic_data:

HIST Physical Basic Data
************************

This module obtains the information from the data extracted with the module
:ref:`hist_data_extraction`. We obtain the time, best ask, best bid, midpoint
price, spread and trade signs in physical time scale.

To run this part of the code is necessary to have the results from the module
:ref:`hist_data_extraction`.

Modules
=======
The code is divided in four parts:
    * `Tools`_: some functions for repetitive actions.
    * `Analysis`_: code to analyze the data.
    * `Plot`_: code to plot the data.
    * `Main`_: code to run the implementation.

Tools
-----
.. automodule:: hist_data_tools_physical_basic_data
   :members:

Analysis
--------
.. automodule:: hist_data_analysis_physical_basic_data
   :members:

Plot
----
.. automodule:: hist_data_plot_physical_basic_data
   :members:

Main
----
.. automodule:: hist_data_main_physical_basic_data
   :members:
