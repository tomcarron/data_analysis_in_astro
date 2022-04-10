import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

"""
Data Analysis in Astronomy and Physics (SoSe22)
Exercise 1: Tom Carron.
"""
"""
SAMPLING
a) Take a sample of 30000 from this dataset and export it to an ASCII file. Make sure that your
method allows to draw more than one sample from the population.
"""
print("Creating random sample of 30,000 rows")
filename = "cdbrfss1999.csv"
n = sum(1 for line in open(filename)) - 1 #number of records in file (excludes header)
s = 30000 #desired sample size
skip = sorted(random.sample(range(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
df = pd.read_csv(filename, skiprows=skip)
df.to_csv("random_sample.csv")

"""
the above code generates a random sample of 30000 cases everytime the script runs.
b. Discuss your method to do so. Is your sampling a “good sample” in the sense that it is
representative for the larger “population”?
"""

"""
a. Locate the columns corresponding to the variables genhlth, exerany, htf, hti, smoke100,
weight, wtdesire, age, and sex.
b. Reduce your sample to include only these variables and export it to an ASCII file. [5 points]
"""
print("Selecting the columns of interst from the random sample")
df.to_csv("columns_of_interst.csv",columns=["GENHLTH", "EXERANY", "HTF", "HTI", "SMOKE100",
"WEIGHT", "WTDESIRE", "AGE", "SEX"])

df=pd.read_csv("columns_of_interst.csv")
"""
c. How many cases and how many variables are there in your sample?
30,000 cases and 9 variables.

d. What type of variable is genhlth?
Categorical,ordinal

e. What type of variable is weight?
numerical continuous.

f. What type of variable is smoke100?
categorical
"""

"""
One Bar chart
Take all genhlth entries from your sample and draw a bar chart to visualize how the cases are
distributed across the possible categories.
"""
categories=["Excellent", "Very Good", "Good", "Fair", "Poor", "Don't know/\nNot sure", "Refused"]
#value=[1,2,3,4,5,7,9]
h=[df["GENHLTH"].value_counts()[1],df["GENHLTH"].value_counts()[2],df["GENHLTH"].value_counts()[3],df["GENHLTH"].value_counts()[4],df["GENHLTH"].value_counts()[5],df["GENHLTH"].value_counts()[7],df["GENHLTH"].value_counts()[9]]



plt.figure(0)
plt.bar(categories,h,width=0.8)
plt.xticks(rotation=-45)
plt.savefig("plots/bar1.png",dpi=400,bbox_inches="tight")

"""
Two Bar Charts
Combine the smoke100 with the genhlth entries from your sample and draw two bar charts, one
showing the health of the smokers and a second one showing the health of the non-smokers.
Dont know/Not sure and refused entries for smoke100 will be exluded
"""

smoker_df=df.loc[df["SMOKE100"]==1]
non_smoker_df=df.loc[df["SMOKE100"]==2]

h_smoker=[smoker_df["GENHLTH"].value_counts()[1],smoker_df["GENHLTH"].value_counts()[2],smoker_df["GENHLTH"].value_counts()[3],smoker_df["GENHLTH"].value_counts()[4],smoker_df["GENHLTH"].value_counts()[5],smoker_df["GENHLTH"].value_counts()[7],smoker_df["GENHLTH"].value_counts()[9]]

h_non_smoker=[non_smoker_df["GENHLTH"].value_counts()[1],non_smoker_df["GENHLTH"].value_counts()[2],non_smoker_df["GENHLTH"].value_counts()[3],non_smoker_df["GENHLTH"].value_counts()[4],non_smoker_df["GENHLTH"].value_counts()[5],non_smoker_df["GENHLTH"].value_counts()[7],non_smoker_df["GENHLTH"].value_counts()[9]]

plt.figure(1)
plt.bar(categories,h_smoker,width=0.8)
plt.xticks(rotation=-45)
plt.savefig("plots/bar_smoker.png",dpi=400,bbox_inches="tight")

plt.figure(2)
plt.bar(categories,h_non_smoker,width=0.8)
plt.xticks(rotation=-45)
plt.savefig("plots/bar_non_smoker.png",dpi=400,bbox_inches="tight")


"""
Next let’s consider a new variable bmi that doesn’t show up directly in this data set: Body Mass
Index (BMI).
"""
#Function to calculate BMI given height in inches and weight in pounds. Returns bmi.
def bmi(weight,height):
    y=(weight/height**2) * 703
    return y


htf=(df["HTF"].to_numpy())*12 #getting height in feet and converting to inches
hti=df["HTI"].to_numpy()      #inches component of height
heights=(htf+hti)  #total height in inches
weights=(df["WEIGHT"]).to_numpy()   #weight in pounds
#print("Weight",weights)
#print("height",heights)
bmis=bmi(weights,heights)      #calculating bmi


df=df.assign(BMI=bmis)  #adding bmi column to df

#replacing bmi where weight or height were answered as refusal or dont know/not sure.
df.loc[df["WEIGHT"] >=777, "BMI"] = np.NaN
df.loc[df["WEIGHT"] <50, "BMI"] = np.NaN
df.loc[df["HTI"] >=12, "BMI"] = np.NaN
df.loc[df["HTF"] >=7, "BMI"] = np.NaN
df.loc[df["HTF"] <2, "BMI"] = np.NaN
df.loc[df["BMI"] == np.inf, "BMI"] = np.NaN

df.to_csv("with_BMI.csv")
df=pd.read_csv("with_BMI.csv")

#visualize bmi as histogram
plt.figure(3)
plt.hist(df["BMI"].to_numpy(),bins=50)
plt.xlabel("BMI")
plt.savefig("plots/bmi.png",dpi=400,bbox_inches="tight")
plt.show()
