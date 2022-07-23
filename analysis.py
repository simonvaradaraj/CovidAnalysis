# Visulatizing the Growth in Covid 19 Cases in Texas, and it to the growth of Monkeypox

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data gathered from https://dshs.texas.gov/coronavirus/AdditionalData.aspx 
# TEXAS DEPARTMENT OF STATE HEALTH SERVICES - Last Updated July 23rd 2022

# vaccsheets is a dictionary that holds a dataframe interpretation of the excel sheets on the vaccine data spreadsheet
vaccsheets = pd.read_excel("COV19-vaccine-data-by-county.xlsx", sheet_name=None)
covidsheets = pd.read_excel("texasnewcases.xlsx", sheet_name=None)

# FORMATTING THE VACCINATION SHEET

# dropping useless info on the vaccination spreadsheet
del vaccsheets['By Vaccination Date']['People with at least One Booster Dose']

# formatting the dates in the excel sheet to pandas datetime values
vaccsheets['By Vaccination Date']['Vaccination Date'] = pd.to_datetime(vaccsheets['By Vaccination Date']['Vaccination Date'], format='%Y-%m-%d %H:%M:%S.%f')
vaccsheets['By Vaccination Date']['Doses Administered'] /= 1000

# plotting Vaccine doses over time
vaccsheets['By Vaccination Date'].plot(x = "Vaccination Date", y = ["Doses Administered"])
plt.ylabel("Doses Administered in thousands")

plt.show()