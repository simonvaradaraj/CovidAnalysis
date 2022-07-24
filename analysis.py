# Visulatizing the Growth in Covid 19 Cases in Texas, and it to the growth of Monkeypox

from turtle import color
from matplotlib import dates
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Data gathered from https://dshs.texas.gov/coronavirus/AdditionalData.aspx 
# TEXAS DEPARTMENT OF STATE HEALTH SERVICES - Last Updated July 23rd 2022

# vaccsheets is a dictionary that holds a dataframe interpretation of the excel sheets on the vaccine data spreadsheet
vaccsheets = pd.read_excel("COV19-vaccine-data-by-county.xlsx", sheet_name=None)
covidsheets = pd.read_excel("texasnewcases.xlsx", sheet_name=None)

fig, axes = plt.subplots(nrows=1, ncols=2)

# FORMATTING THE VACCINATION SHEET

# dropping useless info on the vaccination spreadsheet
del vaccsheets['By Vaccination Date']['People with at least One Booster Dose']

# formatting the dates in the excel sheet to pandas datetime values
print(vaccsheets['By Vaccination Date']['Vaccination Date'])

vaccsheets['By Vaccination Date']['Vaccination Date'] = pd.to_datetime(vaccsheets['By Vaccination Date']['Vaccination Date'], format='%Y-%m-%d %H:%M:%S.%f')
vaccsheets['By Vaccination Date']['Doses Administered'] /= 1000

# FORMATTING THE COVID CASE SHEET

# creating a list of all the covid cases in 2020-2022
cases2020 = np.array(covidsheets['New Cases by County 2020'].iloc[257][-18:-2])
# syncing up the dates on the vaccination sheet (since that only starts at December 14, 2020)
dates2020 = np.array(covidsheets['New Cases by County 2020'].iloc[1][-18:-2])

cases2021 = np.array(covidsheets['New Cases by County 2021'].iloc[257][1:])
dates2021 = np.array(covidsheets['New Cases by County 2021'].iloc[1][1:])

cases2022 = np.array(covidsheets['New Cases by County 2022'].iloc[257][1:])
# for some reason, this is not being comprehended as the correct datetime unit
dates2022 = (np.array(covidsheets['New Cases by County 2022'].iloc[1][1:]))

properdates = []
# converting to the proper datetime unit
for date in dates2022:
    properdates.append(datetime.strptime(date, '%m/%d/%Y'))

dates2022 = np.asarray(properdates)

allcases = np.concatenate((cases2020, cases2021, cases2022), axis = None) / 1000
alldates = np.concatenate((dates2020, dates2021, dates2022), axis = None)

print(alldates)

# creating a dataframe of the dates and cases
covidframe = pd.DataFrame({'Dates':alldates, 'Cases':allcases})
covidframe.plot(x = 'Dates', y = ["Cases"], ax= axes[0], color = "#FFAAA6")
axes[0].set_ylabel("Cases in thousands")
axes[0].set_xlabel("Contraction Date")

# plotting Vaccine doses over time
vaccsheets['By Vaccination Date'].plot(x = "Vaccination Date", y = ["Doses Administered"], ax=axes[1])
axes[1].set_ylabel("Doses Administered in thousands")
axes[1].set_xlabel("Vaccination Date")


axes[0].set_xlim([datetime.date(2020, 12, 14), datetime.date(2022, 7, 22)])
axes[1].set_xlim([datetime.date(2020, 12, 14), datetime.date(2022, 7, 22)])

plt.show()
