import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Data analysis exercise set 2 - Global CO2 emissions
Author: Tom Carron
"""

"""
Open the data in co2-data.csv to answer the following questions. It contains historical CO2
emissions of each country per capita.
"""

df=pd.read_csv("co2-data.csv")

"""
a. Compute the mean CO2 per capita emission in 2017. What is the standard deviation and
median? 20 points
"""
#new df with just 2017 entries.
df_2017=df.loc[df["year"]==2017]
df_2017.to_csv("co2-data-2017.csv")
#Select the CO2 emission per capita column
#There are some entries which are NaN. We should remove these before calculating the median and standard deviation.
df_2017_co2=df_2017["co2_per_capita"].loc[df_2017["co2_per_capita"].notnull()]
print(df_2017_co2)
#Data is prepped now calculate the standard deviation and median. Data needs to be sorted before calculating the median but np.median does this.
std=np.std(df_2017_co2)
print("Standard deviation is : ", std)
median=np.median(df_2017_co2)
print("Median is : ", median)

"""
b. This compares the data of countries in numerous stages of development. Try separating the data
by continent, then calculate the mean, standard deviation, and median in 2017. Show this data in a
convenient plot (maybe in a box plot). What are the limitations to this data reduction? 30 points
"""
#Africa
df_2017_co2_africa=df_2017_co2.loc[df_2017["continent"]=="Africa"]
std_africa=np.std(df_2017_co2_africa)
median_africa=np.median(df_2017_co2_africa)
#Europe
df_2017_co2_europe=df_2017_co2.loc[df_2017["continent"]=="Europe"]
std_europe=np.std(df_2017_co2_europe)
median_europe=np.median(df_2017_co2_europe)
#Asia
df_2017_co2_asia=df_2017_co2.loc[df_2017["continent"]=="Asia"]
std_asia=np.std(df_2017_co2_asia)
median_asia=np.median(df_2017_co2_asia)
#North America
df_2017_co2_NA=df_2017_co2.loc[df_2017["continent"]=="North America"]
std_NA=np.std(df_2017_co2_NA)
median_NA=np.median(df_2017_co2_NA)
#South America
df_2017_co2_SA=df_2017_co2.loc[df_2017["continent"]=="South America"]
std_SA=np.std(df_2017_co2_SA)
median_SA=np.median(df_2017_co2_SA)
#Oceania
df_2017_co2_oceania=df_2017_co2.loc[df_2017["continent"]=="Oceania"]
std_oceania=np.std(df_2017_co2_oceania)
median_oceania=np.median(df_2017_co2_oceania)

data=[df_2017_co2_africa,df_2017_co2_europe,df_2017_co2_asia,df_2017_co2_NA,df_2017_co2_SA,df_2017_co2_oceania,df_2017_co2]
labels=["Africa","Europe","Asia","North\nAmerica","South\nAmerica","Oceania","Global"]
#Box plot to represent this data
fig, ax = plt.subplots(1)
bp=ax.boxplot(data,labels=labels,patch_artist = True, vert = 0, showfliers=0)
colors = ['red','green','lightblue','lime','purple','yellow','blue']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
ax.set_xlabel("$CO_2$ [tonnes/yr]",labelpad=4).set_rotation(0)
#ax.set_xticklabels(labels,rotation=0)
ax.set_title("$CO_2$ emissions per capita, 2017")
plt.savefig("plots/boxplot.png",dpi=400,bbox_inches="tight")

print("What are the limitations to this data reduction?")

"""
c. To fully assess the contribution of each country to global emissions, we should look at the
cumulative emission. What are the mean, standard deviation, and median of the dataset? Show
this information for both the world and separated by continent. 20 points
"""
#world co2
df_2017_cum=df_2017["co2"].loc[df_2017["co2"].notnull()]
std_cum=np.std(df_2017_cum)
median_cum=np.median(df_2017_cum)
print("Standard deviation is : ", std_cum)
print("Median is : ", median_cum)

#Africa
df_2017_cum_africa=df_2017_cum.loc[df_2017["continent"]=="Africa"]
std_africa_cum=np.std(df_2017_cum_africa)
median_africa_cum=np.median(df_2017_cum_africa)
#Europe
df_2017_cum_europe=df_2017_cum.loc[df_2017["continent"]=="Europe"]
std_europe_cum=np.std(df_2017_cum_europe)
median_europe_cum=np.median(df_2017_cum_europe)
#Asia
df_2017_cum_asia=df_2017_cum.loc[df_2017["continent"]=="Asia"]
std_asia_cum=np.std(df_2017_cum_asia)
median_asia_cum=np.median(df_2017_cum_asia)
#North America
df_2017_cum_NA=df_2017_cum.loc[df_2017["continent"]=="North America"]
std_NA_cum=np.std(df_2017_cum_NA)
median_NA_cum=np.median(df_2017_cum_NA)
#South America
df_2017_cum_SA=df_2017_cum.loc[df_2017["continent"]=="South America"]
std_SA_cum=np.std(df_2017_cum_SA)
median_SA_cum=np.median(df_2017_cum_SA)
#Oceania
df_2017_cum_oceania=df_2017_cum.loc[df_2017["continent"]=="Oceania"]
std_oceania_cum=np.std(df_2017_cum_oceania)
median_oceania_cum=np.median(df_2017_cum_oceania)

data_cum=[df_2017_cum_africa,df_2017_cum_europe,df_2017_cum_asia,df_2017_cum_NA,df_2017_cum_SA,df_2017_cum_oceania,df_2017_cum]
labels=["Africa","Europe","Asia","North\nAmerica","South\nAmerica","Oceania","Global"]
#Box plot to represent this data
fig1, ax1 = plt.subplots(1)
bp1=ax1.boxplot(data_cum,labels=labels,patch_artist = True, vert = 0, showfliers=0)
#colors = ['red','green','lightblue','lime','purple','yellow','pink']

for patch, color in zip(bp1['boxes'], colors):
    patch.set_facecolor(color)
ax1.set_xlabel("$CO_2$ [tonnes/yr]",labelpad=4).set_rotation(0)
#ax.set_xticklabels(labels,rotation=0)
ax1.set_title("$CO_2$ emissions (cumulative), 2017")
plt.savefig("plots/boxplot_cumulative.png",dpi=400,bbox_inches="tight")

"""
d. We can also look at this history of CO2 emissions by each country. Calculate the mean and
standard deviation of the annual emission for the U.S., U.K., Germany, and China. Is this metric
useful? In which year was the peak emission from these countries? Are they starting to gain control
of their emissions? 30 points
"""
df2=df.loc[(df["country"]=="United States") | (df["country"]=="United Kingdom") | (df["country"]=="Germany") | (df["country"]=="China")]
#get max and min years
print("years min=",np.min(df2["year"].to_numpy()),"years max=",np.max(df2["year"].to_numpy()))
#creating an array of all the years.
years=[]
k=np.min(df2["year"].to_numpy())
while k < (np.max(df2["year"].to_numpy())+1):
    years.append(k)
    k+=1

print(years)
countries=["United States","United Kingdom","Germany","China"]
means=[]
stds=[]
for i in range(len(years)):
    year=years[i]
    year_total=[]
    year_total=df2["co2"].loc[df2["year"]==year]
    means.append(np.mean(year_total))
    stds.append(np.std(year_total))

"""
NEED TO GET RID OF YEARS WHERE DATA IS NOT AVAILABLE FOR ALL 4 COUNTRIES
"""
for i in range(len(years)):
    print("year=",years[i],"mean=",means[i],"std=",stds[i])


fig2, ax2=plt.subplots(1)
ax2.plot(years,means)
ax2.set_ylabel("$CO_2$ (mean) [tonnes/yr]",labelpad=4).set_rotation(90)
ax2.set_xlabel("year")
ax2.set_title("mean $CO_2$ emissions of Germany,US,UK and China")
plt.savefig("plots/means_yearly.png",dpi=400,bbox_inches="tight")

fig3, ax3=plt.subplots(1)
ax3.plot(years,stds)
ax3.set_ylabel("$CO_2$ (std) [tonnes/yr]",labelpad=4).set_rotation(90)
ax3.set_xlabel("year")
ax3.set_title("std $CO_2$ emissions of Germany,US,UK and China")
plt.savefig("plots/std_yearly.png",dpi=400,bbox_inches="tight")
plt.show()
