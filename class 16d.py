import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import seaborn as sns
import pandas as pd
'''
x = np.linspace(0, np.pi * 2, 100)

plt.style.use('Solarize_Light2')
plt.title('Sin cos curve')
plt.plot(x, np.sin(x), 'r-', label='sin curve')
plt.plot(x, np.cos(x), 'b:', label ='cos curve')
plt.xlabel('x value')
plt.ylabel('y value')
plt.legend()
plt.show()

print(plt.style.available)
'''

'''
fig, ax = plt.subplots(2,2)
X = np.random.randn(100)
Y = np.random.randn(100)
'''
'''
fig, ax = plt.subplots(2, 3)
grid = plt.GridSpec(2, 3, wspace = 0.4, hspace=0.3)
X = np.random.rand(100)
Y = np.random.randn(100)
ax[0,0].scatter(X,Y)
X = np.arange(10)
Y = np.random.uniform(1, 10, 10)
ax[0, 1].bar(X, Y)
X = np.linspace(0, 10, 100)
Y = np.cos(X)
ax[1, 0].plot(X, Y)
Z = np.random.uniform(0,1,(5,5))
ax[1, 1].imshow(Z)
plt.show()
'''
'''
N = 30
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2

plt.scatter(x, y, s=area, c= colors, alpha=0.5, marker = 'p')
plt.show()
'''
'''
x = np.arange(3)
years = ['2010', '2011', '2012']
domestic = [6801, 7695, 8010]
foreign = [777, 1046, 1681]

plt.bar(x, domestic, width = 0.25)
plt.bar(x + 0.3, foreign, width = 0.25)
plt.xticks(x, years)
plt.show()
'''
'''
data = [5,4,6,11]
clist = ['cyan', 'gray', 'orange', 'red']
plt.pie(data, autopct = '%.2f', colors = clist)
plt.show()
'''
'''
data = np.random.random((10,10))
plt.imshow(data, cmap = 'cool')
plt.show()
plt.colorbar()
plt.show()

'''
'''
heights = np.array([175, 165,164, 164, 171, 165,
                    160, 169, 164, 159, 163, 167, 163, 172,
                    159,160, 156, 162, 166, 162, 158, 167,
                    160, 161, 156, 172, 168, 165, 165, 177])
plt.hist(heights, bins=6, label='cumulative=True', cumulative=True)
plt.hist(heights, bins=6, label='cumulative=False', cumulative=False)
plt.legend(loc='upper left')
plt.xlabel("height")
plt.ylabel("frequency")
plt.show()
'''
'''
f1 = np.random.randn(100000)
plt.hist(f1, bins=200, color='red', alpha=.7, label = 'avg = 0, std = 1')
plt.axis([-8, 8, -2, 2500])
plt.legend()
plt.show()
'''
'''
f1 = np.random.normal(loc=0, scale=1, size=100000)
f2 = np.random.normal(loc=3, scale=1, size=100000)

plt.hist(f1, bins=200, color='red', alpha=.4, label='avg = 0, std = 1')
plt.hist(f2, bins=200, color='green', alpha=.4, label='avg = 3, std = 1')
plt.axis([-8,8,-2,2500])
plt.legend()
plt.show()
'''
'''
rand_data = np.random.randn(100)
plt.boxplot(rand_data)
plt.show()
'''
'''
np.random.seed(85)
data1 = np.random.normal(100,10,200)
data2 = np.random.normal(100,40,200)
data3 = np.random.normal(80, 40, 200)
data4 = np.random.normal(80, 60, 200)

plt.boxplot([data1, data2, data3, data4])
plt.show()
'''

'''
np.random.seed(85)
x = np.arange(0,10)
y1 = x * 2
y2 = x ** 3
y3 = np.random.randint(0, 100, size=10)
np.corrcoef(x, y1)
np.corrcoef(x, y2)
print(np.corrcoef(x,y1))
print(np.corrcoef(x,y2))
print(np.corrcoef(x,y3))

result = np.corrcoef((x, y2, y3))
print(result)
plt.imshow(result)
plt.colorbar()
plt.show()


df = pd.DataFrame({'x':x, 'y2':y2, 'y3':y3})
sns.pairplot(df)
plt.show()
'''
'''
sns.set_theme(style="darkgrid")
tips = sns.load_dataset("tips")

#sns.relplot(data=tips, x="total_bill", y="tip", col = "time", hue="smoker", style="smoker", size="size")
print(tips.shape)
sns.histplot(tips['tip'], kde=False, bins=10)
plt.show()
'''
'''anscombe = sns.load_dataset('anscombe')
print(anscombe.head())
'''
'''
anscombe = sns.load_dataset("anscombe")
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"), ci=None, scatter_kws={"s": 80})
plt.show()
'''

flights = sns.load_dataset("flights")
plt.figure(figsize=(10,3))
sns.relplot(data=flights, x="year", y="passengers", kind="line")
plt.show()


