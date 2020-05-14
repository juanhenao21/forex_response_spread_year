.. Price response functions and spread impact in foreign exchange markets
   documentation master file, created by sphinx-quickstart on Wed Apr 1
   12:06:23 2020. You can adapt this file completely to your liking, but it
   should at least contain the root `toctree` directive.

Price response functions and spread impact in foreign exchange markets
======================================================================

In this study, we analyzed tick data from the foreign exchange market.

The data contains the best bid price and the best ask price. With this
information we compute the midpoint price and the trade signs. Finally we
obtain the price response functions.

In order to avoid overnight effects and any artifact due to the opening and
closing of the market, we systematically discarded the first ten and the last
ten minutes of a trading in a given week. Therefore, we only consider trades of
the same week from Sunday 17:10:00 to Friday 16:50:00 New York local time. We
will refer to this interval of time as the "market time".

The main objective of this work is to analyze the price response functions. In
general we define the self-response functions in a foreign exchange market as

.. math::  R^{scale}_{ii}\left(\tau\right)=\left\langle r^{scale}_{i}\left(t-1,
    \tau\right) \cdot\varepsilon^{scale}_{i} \left(t\right)\right\rangle
    _{scale}

In the following can be seen the documentation of all the code used in the
project.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   01_hist_download_data

   02_hist_data_extraction

   03_hist_responses_trade

   04_hist_physical_basic_data

   05_hist_responses_physical

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
