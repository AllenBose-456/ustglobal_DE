import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("titanic - titanic.csv")
print(data)
null_less_data=data.dropna(subset=['Age'])
print(null_less_data)
# plot=sns.relplot(data=data,x="Age",y="Survived",hue="Survived",kind="scatter",palette=["r","g"])
# plot=sns.relplot(data=data,x="Age",y="Survived",hue="Survived",palette=["r","g"],kind="line",marker="o")
plot=sns.lineplot(data=data,x="Age",y="Survived",hue="Sex",palette=["r","g"],marker="o")
plt.savefig("assaingment_plot.png")
plt.show()

