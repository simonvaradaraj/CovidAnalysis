# Visualizing the Growth in Covid 19 Cases in Texas, and it to the growth of Monkeypox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data gathered from https://dshs.texas.gov/coronavirus/AdditionalData.aspx 
# TEXAS DEPARTMENT OF STATE HEALTH SERVICES - Last Updated July 23rd 2022

vaccsheet = pd.read_excel("COV19-vaccine-data-by-county.xlsx", sheet_name="By Age, Day")

# data gathered from https://www.statista.com/statistics/912205/texas-population-share-age-group/
# Statistica Research Group

populframe = pd.DataFrame({
    'Age Groups': ['6mo-4yr', '5yr-12yr', '12yr-15yr', '16yr-49yr', '50yr-64yr', '65yr-79yr', '80yr+'],
    'Percents': [6.8, (6.9+3.75), (3.75+4.2), (3+6.8+14.6+13.7+6),(6.3+5.8+5.5), (7.8+2), (1.7+1.4)]
})

# creating subplots
fig, axes = plt.subplots(nrows=1, ncols=2)

# FORMATTING THE VACCINATION SHEET

# dropping useless info on the vaccination spreadsheet
del vaccsheet['Agegrp'], vaccsheet['Vaccination Date'], vaccsheet['Doses Administered']
vaccsheet = vaccsheet.drop(vaccsheet.index[7:])

# Plotting the pie chart for vaccination dataframe
vaccsheet.groupby(['Age Groups']).sum().plot(kind='pie', y='Vaccinations', ax = axes[0])
axes[0].set_title("Vaccinations Per Age Group")


# Plotting the pie chart for population dataframe
populframe.groupby(['Age Groups']).sum().plot(kind='pie', y='Percents', ax = axes[1])
axes[1].set_title("Population Per Age Group")


plt.show()