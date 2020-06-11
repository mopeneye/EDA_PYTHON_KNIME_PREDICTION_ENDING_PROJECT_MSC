# EDA_PYTHON_KNIME_PREDICTION_ENDING_PROJECT_MSC
I'm very proud to share my ending project of MSc in business analytics. Project is consist of two stages.  First stage covers a comprehensive data analysis and visualisation of data obtained from kaggle. Second stage covers some preprocessing tasks performed and then usage of several machine learning models in order to predict severity levels of accidents happened in USA.  For both stage, python has been used as programming language. In second stage of the project, Knime analytics platform has been used and integrated with python.  

First stage:

Data download link is below:
https://drive.google.com/open?id=1Jv7yHBumRavNIOLootzvvkKQ_WqoA8OT

All codes for EDA stage is available in data_analysis_visualization_318631062.ipynb file.

In order to analyze 1M rows of data code is available in bitirme_318631062.py file

Note: path should be updated with the location of csv file in your computer where ever you downloaded to.

Second stage:

Note 1: You must add python extension to your knime analytics platform to use python in knime.
Note 2: Complete workflow is available in  Bitirme_projesi_v2_Mert_Acikgoz.knwf file

To provide running knime analytics platform as quick as possible, we're importing 500K lines of data to a dataframe in python.
Code is available in bitirme_318631062.py file.

Since excel has boundaries, we're dividing data to 10 xls files that include 50K rows.

Code is available in bitirme_318631062.py file.

You should update configuration of Excel Reader nodes in Knime workflows with xls files locations where ever you've created in your
computer.
                   

