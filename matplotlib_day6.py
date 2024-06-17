# import matplotlib.pyplot as plt
# weight=[90,40,60,77,88,99,66]
# height=[1.5,2,2.5,3,3.5,4,4.5]
# fig,ax=plt.subplots()
# ax.bar(weight,height)
# plt.show()

# fig,ax=plt.subplots()
# months=["jan","feb","march","april","may","june"]
# temp_recorded=[36,42,40,48,49,36]
# bar_labels=["cool","hot","hot","super hot","super hot","hot"]
# bar_colors=["tab:blue","tab:red","tab:red","tab:orange","tab:orange","tab:blue"]
# ax.bar(months,temp_recorded,label=bar_labels,color=bar_colors)
# ax.set_label("temperature of the month")
# ax.set_title("Month wise temp recorded")
# ax.legend(title=("temerature by month"))
# plt.show()
import numpy as np
#
# species=("adelie\n $\\mu=$3700.66g","Chinstrap\n $\\mu=$3733.09g","Gentoo\n $\\mu=5076.02g$")
#
# weight_counts={
#     "Below":np.array([70,31,58]),
#     "above":np.array([70,31,58])
# }
# width=0.5
# bottom=np.zeros(3)
# fig,ax=plt.subplots()
# for boolean,weight_count in weight_counts.items():
#     p=ax.bar(species,weight_count,width,label=boolean,bottom=bottom)
#     bottom+=weight_count
# ax.set_title("Number of penguins with average body mass")
# ax.legend(loc="upper right")
# plt.show()

# species=["adelie","Chinstrap","Gento"]
# penguin_means={
#     "Billdepth":(18.5,18.43,14.98),
#     "Bill Length":(38.79,48.83,47.50),
#     "Flipper Length":(189.95,195.82,217.19)
# }
# x=np.arange(len(species))# label locationse\
# width=.25
# multiplier=0
#
# fig,ax=plt.subplots(layout="constrained")
# for attribute,measurement in penguin_means.items():
#     offset=width*multiplier
#     rects=ax.bar(x+offset,measurement,width,label=attribute)
#     ax.bar_label(rects,padding=3)
#     multiplier+=1
# ax.set_label("length(mm)")
# ax.set_title("penguine Attribute by species")
# ax.set_xticks(x+width,species)
# ax.legend(loc="upper left",ncols=3)
# ax.set_ylim(0,250)
# plt.show()
#
# fig,ax=plt.subplots(figsize=(6,3),subplot_kw=dict(aspect="equal"))
# recipe=["375 g flour","75 g sugar","250 g butter","300 g berries"]
# data=[float(x.split()[0]) for x in recipe]
# incredients=[x.split()[-1] for x in recipe]
# print(data, incredients)
#
# def fun(pct,alvals):
#     absolute=int(np.round(pct/100.*np.sum(alvals)))
#     return f'{pct:.1f}%\n({absolute:d}g)'
#
# wedges,texts,autotexts=ax.pie(data,autopct=lambda pct : fun(pct,data),textprops=dict(color="w"))
# ax.legend(wedges,incredients,title="Ingredients",loc="center left",bbox_to_anchor=(1,0,0.5,1))
# plt.setp(autotexts,size=8,weight="bold")
# ax.set_title("Bakery:A pie")
# plt.show()

import pandas as pd
# df=pd.read_csv("Case.csv")
# x_axis=df.groupby("province")["confirmed"].sum()
# a=x_axis.index
# b=x_axis.values
# plt.xticks(rotation=79)
# plt.title("Covid Positive cases")
# plt.bar(a,b)
# plt.show()
 # plot a graph with the age of the people with the count of values with same age print grapg from patient info

# total_matches_played=[100,40,60,35,19,100]
# average_scores=[4000,3500,3800,1400,2000,6000]
# plt.hist(average_scores)
# plt.show()

#seaborn-powerful python datavisualisation
import numpy as numpy
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
#
print(sns.get_dataset_names())
tips=sns.load_dataset('tips')
print(tips.head())
gap=px.data.gapminder()
print(gap)
""""
sns.relplot(data=tips,x="total_bill",y="tip",kind="scatter")
plt.title("Total Bill vs Tip")
plt.show()"""

g=sns.scatterplot(data=tips,x="total_bill",y="tip")
g.set_title("Total Bill vs Tip")
plt.show()
india=gap[(gap["country"]=="India")]
sns.relplot(data=india,y="lifeExp",x="year",kind="line")
plt.title("YoY life Expatancy of india")
plt.show()

sns.histplot(data=tips,x="tip",hue="sex",kde=True)
sns.relplot(data=tips,x="sex",y="tip",kind="line")
g=sns.barplot(data=tips,x="day",y="total_bill",estimator=np.median,errorbar=None)
g.set_title("Daywise Total Bill")
g=sns.pointplot(data=tips,x="day",y="tip",hue="sex")
g.set_title("Day_Wise Tip")
plt.show()


