import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

esg_country = pd.read_csv(r"D:\Unified mentor Internship projects\1. Data governance & Security dashboard\Data Governance and Security Dashboard-20241104T085632Z-001\Data Governance and Security Dashboard\ESGCountry.csv")
esg_countryseries = pd.read_csv(r"D:\Unified mentor Internship projects\1. Data governance & Security dashboard\Data Governance and Security Dashboard-20241104T085632Z-001\Data Governance and Security Dashboard\ESGCountry-Series.csv")
esg_data = pd.read_csv(r"D:\Unified mentor Internship projects\1. Data governance & Security dashboard\Data Governance and Security Dashboard-20241104T085632Z-001\Data Governance and Security Dashboard\ESGData.csv")
esg_footnote = pd.read_csv(r"D:\Unified mentor Internship projects\1. Data governance & Security dashboard\Data Governance and Security Dashboard-20241104T085632Z-001\Data Governance and Security Dashboard\ESGFootNote.csv")
esg_series = pd.read_csv(r"D:\Unified mentor Internship projects\1. Data governance & Security dashboard\Data Governance and Security Dashboard-20241104T085632Z-001\Data Governance and Security Dashboard\ESGSeries.csv")
esg_seriestime = pd.read_csv(r"D:\Unified mentor Internship projects\1. Data governance & Security dashboard\Data Governance and Security Dashboard-20241104T085632Z-001\Data Governance and Security Dashboard\ESGSeries-Time.csv")

esg_data.head()

col = esg_data.columns

y = esg_data.loc[19]

esg_data.isnull().sum()

esg_data['1990'].fillna(esg_data['1990'].mean(), inplace = True)
esg_data['1991'].fillna(esg_data['1991'].mean(), inplace=True)
esg_data['1992'].fillna(esg_data['1992'].mean(), inplace=True)
esg_data['1993'].fillna(esg_data['1993'].mean(), inplace=True)
esg_data['1994'].fillna(esg_data['1994'].mean(), inplace=True)
esg_data['1995'].fillna(esg_data['1995'].mean(), inplace=True)
esg_data['1996'].fillna(esg_data['1996'].mean(), inplace=True)
esg_data['1997'].fillna(esg_data['1997'].mean(), inplace=True)
esg_data['1998'].fillna(esg_data['1998'].mean(), inplace=True)
esg_data['1999'].fillna(esg_data['1999'].mean(), inplace=True)
esg_data['2000'].fillna(esg_data['2000'].mean(), inplace=True)
esg_data['2001'].fillna(esg_data['2001'].mean(), inplace=True)
esg_data['2002'].fillna(esg_data['2002'].mean(), inplace=True)
esg_data['2003'].fillna(esg_data['2003'].mean(), inplace=True)
esg_data['2004'].fillna(esg_data['2004'].mean(), inplace=True)
esg_data['2005'].fillna(esg_data['2005'].mean(), inplace=True)
esg_data['2006'].fillna(esg_data['2006'].mean(), inplace=True)
esg_data['2007'].fillna(esg_data['2007'].mean(), inplace=True)
esg_data['2008'].fillna(esg_data['2008'].mean(), inplace=True)

esg_data['2009'].fillna(esg_data['2009'].mean(), inplace=True)
esg_data['2010'].fillna(esg_data['2010'].mean(), inplace=True)
esg_data['2011'].fillna(esg_data['2011'].mean(), inplace=True)
esg_data['2012'].fillna(esg_data['2012'].mean(), inplace=True)
esg_data['2013'].fillna(esg_data['2013'].mean(), inplace=True)
esg_data['2014'].fillna(esg_data['2014'].mean(), inplace=True)
esg_data['2015'].fillna(esg_data['2015'].mean(), inplace=True)
esg_data['2016'].fillna(esg_data['2016'].mean(), inplace=True)
esg_data['2017'].fillna(esg_data['2017'].mean(), inplace=True)
esg_data['2018'].fillna(esg_data['2018'].mean(), inplace=True)

X = esg_data[[ '1990', '1991', '1992', '1993' , '1994' , '1995' , '1996' ,'1997' , '1998' , '1999' , '2000' , '2001' , '2002' , '2003' , '2004', '2005' , '2006' , '2007', '2008' , '2009' , '2010' , '2011' , '2012' , '2013' , '2014' ,'2015', '2016' ,'2017' ,'2018']]


# deleting data("Year") that have less than 40% of the data that is valid.(Might prevent us from being able to understand various criterion)
list = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
       '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986','1987', '1988', '1989', '2019', '2020', '2050', 'Unnamed: 66']

updated = esg_data.drop(list, axis=1)
updated.head()

new = updated.columns
new_list = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977','1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986','1987', '1988', '1989', '2019', '2020', '2050', 'Unnamed: 66']

updated = esg_data.drop(new_list, axis = 1)
updated = updated.transpose()

# Top 3 ESG.
sweden = updated[[14216, 14221, 14225, 14239, 14253]].reset_index(drop = True)
sweden = sweden.rename({14216: 'CO2 emissions (metric tons per capita)',
                        14221: 'Electricity production from coal sources (% of total)',
                        14225: 'Fertility rate, total (births per woman)',
                        14239: 'Life expectancy at birth, total (years)',
                        14253: 'Population ages 65 and above (% of total population)'}, axis = 1)

finland = updated[[7047, 7052, 7056, 7070, 7084]].reset_index(drop = True)
finland = finland.rename({7047: 'CO2 emissions (metric tons per capita)',
                          7052: 'Electricity production from coal sources (% of total)',
                          7056: 'Fertility rate, total (births per woman)',
                          7070: 'Life expectancy at birth, total (years)',
                          7084: 'Population ages 65 and above (% of total population)'}, axis = 1)

norway = updated[[11737, 11742, 11746, 11760, 11774]].reset_index(drop = True)
norway = norway.rename({11737: 'CO2 emissions (metric tons per capita)',
                        11742: 'Electricity production from coal sources (% of total)',
                        11746: 'Fertility rate, total (births per woman)',
                        11760: 'Life expectancy at birth, total (years)',
                        11774: 'Population ages 65 and above (% of total population)'}, axis = 1)

# Bottom 3 ESG.
south_sudan = updated[[13680, 13685, 13689, 13703, 13717]].reset_index(drop = True)
south_sudan = south_sudan.rename({13680: 'CO2 emissions (metric tons per capita)',
                                  13685: 'Electricity production from coal sources (% of total)',
                                  13689: 'Fertility rate, total (births per woman)',
                                  13703: 'Life expectancy at birth, total (years)',
                                  13717: 'Population ages 65 and above (% of total population)'}, axis = 1)


car = updated[[5104, 5109, 5113, 5127, 5141]].reset_index(drop = True)
car = car.rename({5104: 'CO2 emissions (metric tons per capita)',
                  5109: 'Electricity production from coal sources (% of total)',
                  5113: 'Fertility rate, total (births per woman)',
                  5127: 'Life expectancy at birth, total (years)', 
                  5141: 'Population ages 65 and above (% of total population)'}, axis = 1)

yemen = updated[[15824, 15829, 15833, 15847, 15861]].reset_index(drop = True)
yemen = yemen.rename({15824: 'CO2 emissions (metric tons per capita)',
                      15829: 'Electricity production from coal sources (% of total)',
                      15833: 'Fertility rate, total (births per woman)', 
                      15847: 'Life expectancy at birth, total (years)', 
                      15861: 'Population ages 65 and above (% of total population)'}, axis = 1)

# Sweden Graphs.
plt.plot(sweden.index, sweden['CO2 emissions (metric tons per capita)'], color = 'red', linewidth = 2)
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(sweden.index, sweden['Electricity production from coal sources (% of total)'], color = 'red', linewidth = 2)
plt.ylabel('Electricity production from coal sources (% of total)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(sweden.index, sweden['Fertility rate, total (births per woman)'], color = 'red', linewidth = 2)
plt.ylabel('Fertility rate, total (births per woman)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(sweden.index, sweden['Life expectancy at birth, total (years)'], color = 'red', linewidth = 2)
plt.ylabel('Life expectancy at birth, total (years)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(sweden.index, sweden['Population ages 65 and above (% of total population)'], color = 'red', linewidth = 2)
plt.ylabel('Population ages 65 and above (% of total population)')
plt.xlabel('Years since 1990')
plt.show()

# Finland Graphs
plt.plot(finland.index, finland['CO2 emissions (metric tons per capita)'], color = 'red', linewidth = 2)
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(finland.index, finland['Electricity production from coal sources (% of total)'], color = 'red', linewidth = 2)
plt.ylabel('Electricity production from coal sources (% of total)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(finland.index, finland['Fertility rate, total (births per woman)'], color = 'red', linewidth = 2)
plt.ylabel('Fertility rate, total (births per woman)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(finland.index, finland['Life expectancy at birth, total (years)'], color = 'red', linewidth = 2)
plt.ylabel('Life expectancy at birth, total (years)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(finland.index, finland['Population ages 65 and above (% of total population)'], color = 'red', linewidth = 2)
plt.ylabel('Population ages 65 and above (% of total population)')
plt.xlabel('Years since 1990')
plt.show()


plt.plot(norway.index, norway['CO2 emissions (metric tons per capita)'], color = 'red', linewidth = 2)
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(norway.index, norway['Electricity production from coal sources (% of total)'], color = 'red', linewidth = 2)
plt.ylabel('Electricity production from coal sources (% of total)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(norway.index, norway['Fertility rate, total (births per woman)'], color = 'red', linewidth = 2)
plt.ylabel('Fertility rate, total (births per woman)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(norway.index, norway['Life expectancy at birth, total (years)'], color = 'red', linewidth = 2)
plt.ylabel('Life expectancy at birth, total (years)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(norway.index, norway['Population ages 65 and above (% of total population)'], color = 'red', linewidth = 2)
plt.ylabel('Population ages 65 and above (% of total population)')
plt.xlabel('Years since 1990')
plt.show()


plt.plot(south_sudan.index, south_sudan['CO2 emissions (metric tons per capita)'], color = 'red', linewidth = 2)
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(south_sudan.index, south_sudan['Electricity production from coal sources (% of total)'], color = 'red', linewidth = 2)
plt.ylabel('Electricity production from coal sources (% of total)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(south_sudan.index, south_sudan['Fertility rate, total (births per woman)'], color = 'red', linewidth = 2)
plt.ylabel('Fertility rate, total (births per woman)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(south_sudan.index, south_sudan['Life expectancy at birth, total (years)'], color = 'red', linewidth = 2)
plt.ylabel('Life expectancy at birth, total (years)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(south_sudan.index, south_sudan['Population ages 65 and above (% of total population)'], color = 'red', linewidth = 2)
plt.ylabel('Population ages 65 and above (% of total population)')
plt.xlabel('Years since 1990')
plt.show()


plt.plot(car.index, car['CO2 emissions (metric tons per capita)'], color = 'red', linewidth = 2)
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(car.index, car['Electricity production from coal sources (% of total)'], color = 'red', linewidth = 2)
plt.ylabel('Electricity production from coal sources (% of total)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(car.index, car['Fertility rate, total (births per woman)'], color = 'red', linewidth = 2)
plt.ylabel('Fertility rate, total (births per woman)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(car.index, car['Life expectancy at birth, total (years)'], color = 'red', linewidth = 2)
plt.ylabel('Life expectancy at birth, total (years)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(car.index, car['Population ages 65 and above (% of total population)'], color = 'red', linewidth = 2)
plt.ylabel('Population ages 65 and above (% of total population)')
plt.xlabel('Years since 1990')
plt.show()


plt.plot(yemen.index, yemen['CO2 emissions (metric tons per capita)'], color = 'red', linewidth = 2)
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(yemen.index, yemen['Electricity production from coal sources (% of total)'], color = 'red', linewidth = 2)
plt.ylabel('Electricity production from coal sources (% of total)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(yemen.index, yemen['Fertility rate, total (births per woman)'], color = 'red', linewidth = 2)
plt.ylabel('Fertility rate, total (births per woman)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(yemen.index, yemen['Life expectancy at birth, total (years)'], color = 'red', linewidth = 2)
plt.ylabel('Life expectancy at birth, total (years)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(yemen.index, yemen['Population ages 65 and above (% of total population)'], color = 'red', linewidth = 2)
plt.ylabel('Population ages 65 and above (% of total population)')
plt.xlabel('Years since 1990')
plt.show()

plt.plot(sweden.index, sweden['CO2 emissions (metric tons per capita)'], color = 'red', linewidth = 2, label = "Sweden")
plt.plot(finland.index, finland['CO2 emissions (metric tons per capita)'], color = 'blue', linewidth = 2, label = "Finland")
plt.plot(norway.index, norway['CO2 emissions (metric tons per capita)'], color = 'green', linewidth = 2, label = "Norway")
plt.plot(south_sudan.index, south_sudan['CO2 emissions (metric tons per capita)'], color = 'orange', linewidth = 2, label = "South_sudan")
plt.plot(car.index, car['CO2 emissions (metric tons per capita)'], color = 'black', linewidth = 2, label = "Central African Republic")
plt.plot(yemen.index, yemen['CO2 emissions (metric tons per capita)'], color = 'purple', linewidth = 2, label = "Yemen")
plt.ylabel("CO2 emissions (metric tons per capita)")
plt.xlabel("Years since 1990")
plt.legend(loc = "lower left", prop = {'size': 8})
plt.show()


plt.plot(sweden.index, sweden['Electricity production from coal sources (% of total)'], color = 'red', linewidth = 2, label = "Sweden")
plt.plot(finland.index, finland['Electricity production from coal sources (% of total)'], color = 'blue', linewidth = 2, label = "Finland")
plt.plot(norway.index, norway['Electricity production from coal sources (% of total)'], color = 'green', linewidth = 2, label = "Norway")
plt.plot(south_sudan.index, south_sudan['Electricity production from coal sources (% of total)'], color = 'orange', linewidth = 2, label = "South Sudan")
plt.plot(car.index, car['Electricity production from coal sources (% of total)'], color = 'black', linewidth = 2, label = "Central African Republic")
plt.plot(yemen.index, yemen['Electricity production from coal sources (% of total)'], color = 'purple', linewidth = 2, label = "Yemen")
plt.ylabel("Electricity production from coal sources (% of total)")
plt.xlabel("Years since 1990")
plt.legend(loc = "lower left", prop = {'size': 8})
plt.show()

plt.plot(sweden.index, sweden['Fertility rate, total (births per woman)'], color = 'red', linewidth = 2, label = "Sweden")
plt.plot(finland.index, finland['Fertility rate, total (births per woman)'], color = 'blue', linewidth = 2, label = "Finland")
plt.plot(norway.index, norway['Fertility rate, total (births per woman)'], color = 'green', linewidth = 2, label = "Norway")
plt.plot(south_sudan.index, south_sudan['Fertility rate, total (births per woman)'], color = 'orange', linewidth = 2, label = "South Sudan")
plt.plot(car.index, car['Fertility rate, total (births per woman)'], color = 'black', linewidth = 2, label = "Central African Republic")
plt.plot(yemen.index, yemen['Fertility rate, total (births per woman)'], color = 'purple', linewidth = 2, label = "Yemen")
plt.ylabel("Fertility rate, total (births per woman)")
plt.xlabel("Years since 1990")
plt.legend(loc = "lower left", prop = {'size': 8})
plt.show()

plt.plot(sweden.index, sweden['Life expectancy at birth, total (years)'], color = 'red', linewidth = 2, label = "Sweden")
plt.plot(finland.index, finland['Life expectancy at birth, total (years)'], color = 'blue', linewidth = 2, label = "finland")
plt.plot(norway.index, norway['Life expectancy at birth, total (years)'], color = 'green', linewidth = 2, label = "Norway")
plt.plot(south_sudan.index, south_sudan['Life expectancy at birth, total (years)'], color = 'orange', linewidth = 2, label = "South Sudan")
plt.plot(car.index, car['Life expectancy at birth, total (years)'], color = 'black', linewidth = 2, label = "Central African Republic")
plt.plot(yemen.index, yemen['Life expectancy at birth, total (years)'], color = 'purple', linewidth = 2, label = "Yemen")
plt.ylabel("Life expectancy at birth, total (years)")
plt.xlabel("Years since 1990")
plt.legend(loc = "lower left", prop = {'size': 8})
plt.show()

plt.plot(sweden.index, sweden['Population ages 65 and above (% of total population)'], color = 'red', linewidth = 2, label = "Sweden")
plt.plot(finland.index, finland['Population ages 65 and above (% of total population)'], color = 'blue', linewidth = 2, label = "Finland")
plt.plot(norway.index, norway['Population ages 65 and above (% of total population)'], color = 'green', linewidth = 2, label = "Norway")
plt.plot(south_sudan.index, south_sudan['Population ages 65 and above (% of total population)'], color = 'orange', linewidth = 2, label = "South Sudan")
plt.plot(car.index, car['Population ages 65 and above (% of total population)'], color = 'black', linewidth = 2, label = "Central African republic")
plt.plot(yemen.index, yemen['Population ages 65 and above (% of total population)'], color = 'purple', linewidth = 2, label = "Yemen")
plt.ylabel("Population ages 65 and above (% of total population)")
plt.xlabel("Years since 1990")
plt.legend(loc = "lower left", prop = {'size': 8})
plt.show()











