import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data="https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang',
'oldpeak', 'slope', 'ca', 'thal', 'target']
dataset=pd.read_csv(data, names=columns)
for column in dataset.columns:
    dataset[column]=pd.to_numeric(dataset[column],errors="coerce")
print(dataset.info())
print(dataset.describe())
dataset["ca"].replace("?",float("nan"),inplace=True)
dataset["target"].where(dataset["target"] < 1, 1, inplace=True)
dataset=dataset.dropna()
print(dataset)


print("*"*30,"Task 1","*"*30)
# dataset["sex"].replace(float(0.0),str("Female"),inplace=True)
# dataset["sex"].replace(float(1.0),str("Male"),inplace=True)
print(dataset)
male=dataset[dataset["sex"]==0.0]['age']
print(male)
female=dataset[dataset["sex"]==1.0]['age']
plt.hist(female,color="g",bins=20,edgecolor="blue",label="female")
plt.hist(male,color="r",bins=20,edgecolor="black",label="Male")

plt.title(" age distribution")
plt.legend(title="sex")
plt.xlabel("verity of male and female age")
plt.savefig("task1.png")
plt.show()
"""
here we get the  male and female of different ages Females of age above 55-60 is going to hospital more and
in Males its seen between 50-70 range
"""


print("*"*30,"Task 2","*"*30)
# dataset["sex"].replace(float(0.0),str("Female"),inplace=True)
# dataset["sex"].replace(float(1.0),str("Male"),inplace=True)
count=dataset.groupby("sex")["sex"].count().reset_index(name="count")
print(count)
print("*"*30,"Task 2","*"*30)
count["gender"]=count.sex.map({0:"Female",1:"Male"})
print(count)

sns.barplot(data=count,x=count["sex"],y=count["count"],palette=["r","g"],hue=count["gender"])

plt.xlabel("gender")
plt.ylabel("Count")
# sns.countplot(data=dataset,x="sex",palette=["y","g"],hue="sex")

plt.title("Count of Males and Females")
plt.savefig("task2.png")
plt.show()
"""
Males are seen the most at the hopital and comparitively females are seen ath the least
"""
print("*"*30,"Task 3","*"*30)
print(dataset)
dataset["target"].where(dataset["target"] < 1, 1, inplace=True)
dataset["cp"].where(dataset["cp"] <=3,0, inplace=True)
print(dataset)
plt.title("Chest Pain Type vs. Heart Disease")
sns.countplot(data=dataset,x="cp",hue="target",palette=["r","y"])
plt.savefig("task3.png")
plt.show()
"""
type of chest pain 0 has the change of becoming patient and other types has the least
"""
print("*"*30,"Task 4","*"*30)
dataset["target"].where(dataset["target"] < 1, 1, inplace=True)

sns.boxplot(data=dataset,y="chol",hue="target")
plt.legend(title="Patients",labels=["non-patients","patents"])
plt.title("cholostrol level for patients and non patients")
plt.ylabel("Cholostrol level")
plt.savefig("task4.png")
plt.show()
"""
persons with colestrol level has the high chance of affecting heart diseace and if cholostrol level is at 
median there is amore chance of getting heart disease
"""

print("*"*30,"Task 5","*"*30)
dataset["target"].where(dataset["target"] < 1, 1, inplace=True)
var=["thalach","chol","age","target","trestbps"]
sns.pairplot(dataset[var],hue="target")
plt.savefig("task5.png")
plt.show()
"""
pople with ago greater than 45 are more prone to heart disease have lower resting blood pressure than the heart disease patients minimum hesrt rate observed in people with
heart disease
"""

print("*"*30,"Task 6","*"*30)

sns.heatmap(dataset.corr(),annot=True,fmt=".2f",cmap=["red","yellow","green","hotpink","orange","blue","white"])
plt.savefig("task6.png")
plt.show()
"""
Thalassemmia is related with the presence of heart disease.Slope of the peak exercise ST segment is related with ST depression
induced by exercise relative to rest
"""
print("*"*30,"Task 7","*"*30)
plt.scatter(x=dataset["exang"].where(dataset["target"]==1),y=dataset["thalach"].where(dataset["target"]==1))
plt.scatter(x=dataset["exang"].where(dataset["target"]==0),y=dataset["thalach"].where(dataset["target"]==0))
plt.legend(["non-patient","patient"],)
plt.title("to visualize the relationship between exercise-induced angina and maximum heart rate.")
plt.xlabel("exercise-induced angina")
plt.ylabel("maximum heart rate")
plt.savefig("task6.png")
plt.show()

"""
Minimum heart rates are observed in heart diseases patients observed to be more in exercise induced angina
"""