import numpy as np
dataset=np.random.randint(1,300,size=(30,10))
print("Dataset of the company",dataset)
closing_price=dataset[:,-1:]

maxi=closing_price.max()
print("maximum closing price in a month",maxi)
orderd=np.concatenate((closing_price),axis=None)
print("closing price on each day",orderd)
std=np.std(dataset[:,-1:])
print("the day with the highest closing price and its value",std)
for i in range(0,30):
    if orderd[i]==maxi:
        print("the day with the highest closing price is",i+1,"and its value is",orderd[i])


days_of=[]

for i in range(0,len(orderd)-1):
    if(orderd[i]*0.05+orderd[i] < orderd[i+1]):
        days_of.append(i+2)
print("the days where the closing price increased by more than 5% compared to the previous day",days_of)

