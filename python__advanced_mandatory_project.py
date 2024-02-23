# -*- coding: utf-8 -*-
"""Python _Advanced_Mandatory_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19Ggi0ZISKSVumd1iwM0hyWGsgaw9Wn6e

**California_Housing_Dataset**

Introduction:-This dataset gives brief description about california housing data.The main aim of this dataset is to predict the median house prices for california.This dataset consists of the following features are as follows:

1.longitude:A measure of distance of the house horizontally from west to east and it is of numerical datatype i.e., continous data.

2.latitude:A measure of distance of the house vertically from north to south and it is of numerical datatype i.e., continous data.

3.housing_median_age:it is median age of the house of quantitative datatype i.e., continous data.

4.total_rooms:Total number of rooms within a block is of quantitative data type,i.e.,discrete data.

5.total_bedrooms:Total number of bedrooms within a block is of quantitative data type,i.e.,discrete data.

6.population:Total number of people residing within a block is of quantitative data type,i.e.,discrete data.

7.households:Total number of households,a group of people residing within a homeunit is of quantitative  data type,i.e.,discrete data.

8.median_income:Median income of households within a block of houses.(measured in tens of thousands of US Dollars)is of continuous data.

9.median_house_value:Median house value for households within a block(measured in US Dollars).It comes under continuous data.

10.ocean_proximity:Location of the house with respect to ocean and it is of categorical data i.e.,it is of nominal data type.
"""

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read datafile
df=pd.read_excel("housing+(1).xlsx")
df

#print first 5 rows of data
df.head()

#print last 5 rows of data
df.tail()

#To get information about Dataframe
df.info()

"""From the above it is to be noted that Datatype longitude,latitude,total_bedrooms,median_income are float.

and housing_median_age,total_rooms,population,households,median_house_value as Integer while ocean_proximity is an object.
"""

#to check total number of rows and columns
print(df.shape)

"""1. What is the average median income of the data set and check the distribution of data using appropriate plots. Please explain the distribution of the plot."""

#To find the average of median_income
df['median_income'].mean()

#Histogram is used to see the distribution of numerical values
df.hist(bins = 50, figsize = (15,15))
plt.show()

"""From the above plot,we can observe that housing_median_age and median_house_value has outliers.while total_rooms,total_bedrooms,households,population,median_income are right skewed.while longitude and latitude are assymmetrical i.e., Highly Skewed

2. Draw an appropriate plot to see the distribution of housing_median_age and explain your observations.
"""

#Histogram for distribution of numerical values
plt.hist(df['housing_median_age'],bins=50,facecolor='cyan',edgecolor='black')
# name the x-axis
plt.xlabel("Housing_median_age")
# name the y-axis
plt.ylabel("Frequencies")
# name the title
plt.title("Housing_median_age_Histogram_plot")
plt.show()

"""from the above hist we can observe that it is distributed symmetrically.
we can find the skewness by this formula :   skewed=3*(mean-median)/std()
"""

# to find mean of housing_median_age
mean=df["housing_median_age"].mean()
mean

# to find median of housing_median_age
median=df["housing_median_age"].median()
median

# to find standard deviation of housing_median_age
std=df["housing_median_age"].std()
std

skewed=3*(mean-median)/std
skewed

"""skewness is -0.08 which lies between -0.5 to -0.1 so the housing_median_age is perfectly symmetrical.

3. Show with the help of visualization, how median_income and median_house_values are related?
"""

#scatter plot shows the relationship between two attributes
plt.scatter(df["median_house_value"],df['median_income'],edgecolor='black',facecolor='purple',marker='o')
#name the x_axis
plt.xlabel("median_house_value")
#name the y-axis
plt.ylabel("median_income")
#give the title for plot
plt.title("Relationship between median_house_value and median_income")
plt.show()

"""conclusion:-From the above visualization,we can clearly observe that as median_house_value increases median_income increases and there are outliers in median_house_value.so we can say that median_house_value is directly proportional to median_income.

4. Create a data set by deleting the corresponding examples from the data set for which total_bedrooms are not available.
"""

#Detects missing values
df.isnull()

#gives number of missing values in dataset
df.isnull().sum()

#Dataset Before deleting missing values
df

#To drop the rows and columns with null values
df2=df.dropna()
#Dataset after deleting missing values
df2

"""We have dropped the missing values from dataset using dropna() method

5. Create a data set by filling the missing data with the mean value of the total_bedrooms in the original data set.
"""

#To find mean value of total_bedrooms
total_bedroom_mean=df["total_bedrooms"].mean()
total_bedroom_mean

#filling the missing value with mean_value of total_bedrooms
null_mean=df.fillna(df["total_bedrooms"].mean())
null_mean

#Checking whether the missing value is replaced by mean_value of total_bedrooms
null_mean.loc[289:290,"total_bedrooms"]

"""In the above code,a null_mean dataset had been created where the missing values in the 'total_bedrooms'which are denoted by NaN are replaced with the mean value of the 'total_bedrooms'.

For eg:row no.290,341,538 and other rows with the missing values are replaced with the mean value of 'total_bedrooms' i.e.,537.870553 respectively.

6. Write a programming construct (create a user defined function) to calculate the median value of the data set wherever required.
"""

# To find out median of all columns
median=lambda x:x.median()

df.iloc[:,0:9].apply(median)

# Another approach to find median values
df.median(numeric_only=True)

"""The median value for longitude is -118.4900
The median value for latitude is 34.2600
The median value for housing_median_age is 29.0000
The median value for total_rooms is 2127.0000
The median value for total_bedrooms is 435.0000
The median value for population is 1166.0000
The median value for households is 409.0000
The median value for median_income is 3.5348
The median value for median_house_value is 179700.0000

7. Plot latitude versus longitude and explain your observations.
"""

#To show the relationship between latitude and longitude
plt.scatter(x="latitude",y="longitude",data=df,facecolor='gold',edgecolor='brown')
#name the x-axis
plt.xlabel("latitude")
#name the y-axis
plt.ylabel("longitude")
#name the title
plt.title("Relationship between latitude and longitude")
plt.show()

"""From above scatter plot,we can clearly observe that as longitude decreases latitude is increased.so we can clearly say that longitude and latitude are independent of each other and longitude is inversely proportional to latitude.
From the plot we can note that  longitude vs latitude has a negative correlation as y-axis increases x-axis decreases i.e., Moving in opposite direction.

8. Create a data set for which the ocean_proximity is ‘Near ocean’.
"""

#filtering of data
df_near_ocean=df[df['ocean_proximity']=='NEAR OCEAN']
df_near_ocean

#query method allows you to filter the dataframe
df_nearocean=df.query('ocean_proximity=="NEAR OCEAN"')
df_nearocean

"""9. Find the mean and median of the median income for the data set created in question 8."""

#mean gives average of data
df_near_ocean["median_income"].mean()

#median gives the 50th percentile of set of all observations
df_near_ocean["median_income"].median()

"""The mean and median value in df_near_ocean dataset are : 4.005784 and 3.64705

10. Please create a new column named total_bedroom_size. If the total bedrooms is 10 or less, it should be quoted as small. If the total bedrooms is 11 or more but less than 1000, it should be medium, otherwise it should be considered large.
"""

#conditions for new column
conditions=[(df['total_bedrooms']<=10),(df['total_bedrooms']>11) &(df['total_bedrooms']<=1000),(df['total_bedrooms']>1000)]
#choices for new column
choices=["small",'medium','large']
# return an array drawn from elements in choicelist, depending on conditions.
df["total_bedrooms_size"] = np.select(conditions, choices)
df

"""In the above dataset a new column has been added as total_bedroom_size.Where the total_bedroom_size had been compared to the total_bedrooms while mentioning about the sizes of the total_bedroom_size,where:
If the total_bedrooms <=10 it is indicated as "small"
If the total_bedrooms >=11 or <=1000 it is indicated as "medium"
If the total_bedrooms >1000 it is indicated as "large"

CONCLUSION: 1.From the given dataset it is to be noted that the outliers are present for housing_median_age and median_house_value.

2.From the above it is to be noted that Datatype longitude,latitude,total_bedrooms,median_income,median_house_value are float.

and housing_median_age,total_rooms,population,households as Integer while ocean_proximity is an object.

3.housing_median_age is of fairly symmetric as the skewness value (-0.5 to -0.1).

4.plot between median_income vs median_house_values is directly proportional to each other as it has positive correlation.

5.plot between latitude and longitude is inversely proportional to each other as within increase in latitude,there is decrease in longitude.Therefore ,it has a negative correlation.
"""