# Covid Analysis
This is an excercise in data retreival and visalization using *pandas*, *matplotlib*, and *numpy*. The gata that is to be analysed is the 
offical vaccination and transmission data of COVID-19 in Texas starting from March 6th 2020 to July 23rd 2022. 

All data used in the creation of this project comes directly from the Texas Department of State Health Services, and can be directly accessed <a href = "https://dshs.texas.gov/coronavirus/AdditionalData.aspx" style="color: red"> here. </a>

---

The main logic behind the project is using `pd.read_excel("example_sheetname.xlsx", sheet_name = None)` to create a dictionary of all the sheets in a given excel file. For example, <span style = 'color: green'>texasnewcases.xlsx</span> has *three* separate sheets dividing the covid cases by year, so in order to easily find and collect all the sheet data, this method worked quite well.

After using `pd.read_excel()`, I would use various pandas methods to crop and snip away at unwanted data and plotted all the neccessary data as line graphs over time using Matplotlib.