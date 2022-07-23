# Visulatizing the Growth in Covid 19 Cases in Texas, and it to the growth of Monkeypox

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data gathered from https://dshs.texas.gov/coronavirus/AdditionalData.aspx - TEXAS DEPARTMENT OF STATE HEALTH SERVICES


# covidsheets is a dictionary that holds a dataframe interpretation of the excel sheets on the vaccine data spreadsheet
covidsheets = pd.read_excel("COV19-vaccine-data-by-county.xlsx", sheet_name=None)


covidsheets['By Vaccination Date'].name = "Vaccinations in Texas Over Time (not cumulative)"

# dropping useless info on the vaccination spreadsheet
del covidsheets['By Vaccination Date']['People with at least One Booster Dose']

# formatting the dates in the excel sheet to pandas datetime values
covidsheets['By Vaccination Date']['Vaccination Date'] = pd.to_datetime(covidsheets['By Vaccination Date']['Vaccination Date'], format='%Y-%m-%d %H:%M:%S.%f')
covidsheets['By Vaccination Date']['Doses Administered'] /= 1000

# plotting Vaccine doses over time
covidsheets['By Vaccination Date'].plot(x = "Vaccination Date", y = ["Doses Administered"])
plt.ylabel("Doses Administered in thousands")

plt.show()