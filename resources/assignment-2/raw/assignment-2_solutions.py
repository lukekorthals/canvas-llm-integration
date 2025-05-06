
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


#Python1

numbers = np.random.uniform(-10, 10, 100)

plt.figure()
plt.boxplot(numbers)

plt.figure()
sns.violinplot(data=numbers)
sns.stripplot(data=numbers, jitter=True, color='red')


#Python2

df = pd.read_csv('https://raw.githubusercontent.com/hannesrosenbusch/schiphol_class/master/titanic.csv')
plt.figure()
plt.boxplot([df[df['Survived'] == 0]['Age'].dropna(), df[df['Survived'] == 1]['Age'].dropna()], labels=['Not Survived', 'Survived'])
plt.xlabel('Survived')
plt.ylabel('Age')
plt.title('Age Distribution by Survival')
plt.show()





#Python3

df = sns.load_dataset("tips")

fig, ax = plt.subplots(figsize=(9, 9))
ax.scatter(df.total_bill, df.tip, s=60, alpha=0.7, edgecolors="k")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")
b, a = np.polyfit(df.total_bill, df.tip, deg=1)
xseq = np.linspace(0, 50, num=100)
ax.plot(xseq, a + b * xseq, color="k", lw=2.5)
plt.show()


#Python4

df = sns.load_dataset("diamonds")
df = df.loc[:, ["carat","depth","table","price", "x", "y", "z"]]

fig, ax = plt.subplots(figsize=(10, 5), ncols=2)
sns.heatmap(df.corr(), ax=ax[0])
sns.kdeplot(x=df.carat, y=df.price, ax=ax[1])
plt.show() 



#Python5
df = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(9, 9))
ax.scatter(df.total_bill, df.tip, s=60, alpha=0.7, edgecolors="k")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")
b, a = np.polyfit(df.total_bill, df.tip, deg=1)
xseq = np.linspace(0, 50, num=100)
ax.plot(xseq, a + b * xseq, color="k", lw=2.5)
plt.show()

fig, ax = plt.subplots()
ax.scatter(df.total_bill, df.tip, s=60, alpha=0.7, edgecolors="k")
b, a = np.polyfit(df.total_bill, df.tip, deg=1)
xseq = np.linspace(0, 50, num=100)
ax.plot(xseq, a + b * xseq)
plt.show()

#Python6
#I used more informative variable names
#I got rid of spacing errors

#Python7
#question is whether we shouldnt use camelCase as it's shorter

#Python8
def add(a,b):
  return(a + b)

result1 = add( 2,3)
result2 = 4 *result1
print(result2)
#improved spacing and linebreaks

