import pandas as pd
df=pd.read_csv("mtcars - mtcars.csv")
print(df.keys())
print("*"*100)
print(df.columns)
print("*"*100)
print(df["cyl"])
print("*"*100)
print(df.head())
print("*"*100)
print(df.tail())
print("*"*100)
print(df.iloc[:15,:4])
print("*"*100)
print(df.sample(n=10))
print("*"*100)
print(df.rank())
print("*"*100)
print(df.dtypes)
datas=({

    "Allen":[20,0,40],
    "Albert":[40,30,20]

})
data=pd.DataFrame(datas)
print(data)
data.columns=["Allen","Bose"]
print(data)
data.rename(columns={"Allen":"Albert"},inplace=True)
print(data)
data.set_index("Albert",inplace=True)
print(data)
data.reset_index(inplace=True)
print(data)

df.drop(index=0,axis=0,inplace=True)
print(df.head())


df.drop([1,2,3,4,5,6,7],axis=0,inplace=True)
print(df.head())
df.sort_values("hp",ascending=False,inplace=True)
print(df.head())
df.sort_values((["hp","wt"]))
print(df.head())
da=df.assign(ratio=(df.hp/df.wt))
print(da)

print(df.loc[:,["mpg","wt"]].min())
print(df.mpg==10.400)

print(df.loc[(df.mpg==10.400):].mpg)
print(df.query(("mpg==10.400")))
print("&"*70)
print(data.dropna(how="any").shape)


