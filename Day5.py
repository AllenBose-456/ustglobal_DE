#pandas - used for data analysis strong and flexible for python package which helps with data cleaning and wrangling tasks
#advantage
"""1.creates structured data similar to ms excel spreadsheet
2.Read data from various sources like csv ,TXT ,XLSX, SQL Databases
S.Selects rows and column from data sets
4.Arrange data in ASC and DESC order
5.Filtering data
^.Summerizing data
7.Transpose data into wide and long format
8.Merging and concatinating """
import pandas as pd
import numpy as np
df = pd.read_csv("customers-100.csv")
# print(df.iloc[:,:2]) #get first two columns
# print(df.columns) #index valiues-df.keys()
# print(df["Index"]) #column name
# print(df.dtypes)#datatype of columns
# print(df['Index'].dtypes)#-datatype of column
# print(df.Index.astype(float))#-convert to float
# print(df.shape)#-total number of rows and columns
# print(df.shape[1])#-rows
# print(df.shape[0])#-cols
# print(df.head(10))#shows first 5 rows
# print(df.tail(10))#shows last 10 rows
# print(df[0:5])
# print(df.Index.unique())
# print(len(df.Index.unique()))
#
# #bivarate frequency distribution
# print(pd.crosstab(df.Index,df.City))
# print(df.Index.value_counts(ascending=False))
# print(df.sample(n=10))#-any 10 dats random
# print(df.sample(frac=0.05)) #-5% percent random values from dataset
# print(df[["Index","City"]])#show details of theswe columns
# print(df[["Index","City"]])#show details of theswe columns
# print(df.loc[:,["Index","City"]])#-column datas we can use slice also to filter datas
# # Selecting Consecutive columns
# print(df.loc[:,"Index":"City"])
# print(df.iloc[:,0:4])
# sampledta=pd.DataFrame({'variable1':np.arange(3,10,2)},index=[9,8,7,2])
# print(sampledta)
#
# Zodiac_data=pd.DataFrame({"A":["John","Mary","Julia"],"B":["Libra","leo","virgo"]})
# print(Zodiac_data)
# print(Zodiac_data.columns)
# Zodiac_data.columns=["name","Zodiac_signs"]
# print(Zodiac_data)
# Zodiac_data.rename(columns={"name":"Customer"},inplace=True)#-to hapen in data set-inplace-true
# print(Zodiac_data)
# df.columns=df.columns.str.replace('Index',"Signs")
# print(df.columns)
# print(df.head)
# df.set_index("Signs",inplace=True)#making this as the first index value rather than python index
# print(df.head())
# print(df.columns)
# df.reset_index(inplace=True)
# print(df.head())
# print(df.columns)

#Removing Columns and Rows

# df.drop("Index",axis=1,inplace=True)
# print(df.columns)
# df.drop(0,axis=0,inplace=True)
# print(df.head(),["Index"])
# df.drop(1,axis="index",inplace=True)
# print(df.head(),["Index"])
# df.drop([0,1,2,3,4,5,6,7],axis=0,inplace=True)
# print(df.head())
# df.sort_values("Index",ascending=False,inplace=True)
# print(df.head())
# df.sort_values((["Index","City"]))
# print(df.loc[:,"Index":"City"])
# df["difference"]=df.Index-df.index
# print(df.head())
# df["difference"]=df.eval("Index-index")
# print(df.head())
# data=df.assign(ratio=(df.index/df.Index))
# print(data.head())
# print(df.describe())#onmy for numerical values
# print(df.describe(include=['object']))
# print(df.mean())
# print(df.median())
# print(df.agg(["mean","median"]))
# index_mean=df.Index.mean()
# print(index_mean)
# print(df.Index.max())
# print(df.Index.min())
# print(df.loc[:,["Index","City"]].max())
# print(df.groupby("Index")["City"].min())
# dt=df.groupby("Index").agg({"City":["min","max"],"Index":"mean"})
# dt.columns=["min-City","max-City","mean"]
# # print(dt)
# # print(df.groupby(["Index","City"]).agg({"City":["min","max"],"Index":"mean"}))
#
# #Filtering
# print(df["City"])
# print(df[df.City=="East Leonard"])
# print(df.loc[df.City=="East Leonard",:])
# print(df.loc[df.City=="East Leonard",:].City)
# #2 condition filtering

# data=df.loc[(df.Index==1) and (df.City=="East Leonard")]
# print(data)
# #Filter the rows with index A and income data for 2002=1500000
# data=df.loc[(df.index=="A") and (df.Y2002==1500000)]
#
# data2=df.loc[(df.index=="A" | df.index=="W"),:]#all columns
# data3=df.loc[df.Index.isin(["A","W"]),:]
# df.query("Y2002>120000 & Y2003 <150000")

# mydata={"crop":["Rice","Wheat","Barley",'Maize'],
#         "Yield":[1010,1025.2,1404,1251.7],
#         "cost":[102,np.nan,20,68]}
# crops=pd.DataFrame(mydata)
# print(crops)
# print(crops.isnull())
# print(crops.notnull())
# print(crops.isnull().sum())
# print(crops.dropna(how="any").shape)#drop a row if 1 col data is missing
# print(crops.dropna(how="all").shape)#drop entire row if all column data is null
# print(crops.dropna(subset=["Yield","cost"],how="all").shape)#if yield and cost data missing it will drop
# crops["cost"].fillna(value="Unknown",inplace=True)
# print(crops)
# print(df.loc[df.duplicated(),:])
# print(df.loc[df.duplicated(keep="first"),:])
# df.frop_duplicates()
# df.frop_duplicates(keep="FIrst")# keep only first other will be deleted

#********************iris**************************
# iris=pd.read_csv("iris.csv")
# print(iris)
# iris["Setosa"]=iris.Species.map({"setosa":1,"versicolor":0,"verginica":0})#map and add new series
# print(iris.head())
# pd.get_dummies(iris.Species,prefix="Species")
# print(Species)
# pd.get_dummies(iris.Species,prefix="Species").iloc[:,0:]
# pd.get_dummies(iris.Species,prefix="Species").iloc[:,0:]
# species_dummies=pd.get_dummies(iris.Species,prefix="Species").iloc[:,0:]
# print(species_dummies)
# iris=pd.concat([iris,specific_dummies],axis=1)
# print(iris.head())

#Ranking

# print(iris.rank())
#
# #cumulative sum
# iris['cum_sum']=iris["sepal.length"].cumsum()
# print(iris.head())
# print(iris.quantile(0.5))