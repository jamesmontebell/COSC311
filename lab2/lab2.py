# %%
import pandas as pd
import numpy as np

# %%
df_b = pd.read_csv("/Users/jamesmontebell/Github/cosc311/lab2/Bejaia_Region.csv")
df_s = pd.read_csv("/Users/jamesmontebell/Github/cosc311/lab2/Sidi-Bel_Abbes_Region.csv")

print(df_b.info())


# %%
print(df_b[' Ws'].unique())

# %%
print(df_s[' Ws'].unique())

# %%
print(len(df_b))

# %%
print(len(df_s))

# %%
from matplotlib import pyplot as plt

# %%
plt.plot(range(len(df_b['day'])), df_b['Temperature'])
plt.title('Change in temperature with time.')
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.figure()
plt.show()
plt.close()

# %%

plt.plot(range(len(df_s['day'])), df_s['Temperature'])
plt.title('Change in temperature with time.')
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.figure()
plt.show()
plt.close()

# %%
plt.scatter(df_s['Temperature'], df_s['FWI'])
plt.title("Temperature & FWI")
plt.xlabel('Temperature')
plt.ylabel('FWI')
plt.yticks(np.arange(df_s['FWI'].min(), df_s['FWI'].max(), 2))
plt.figure()
plt.show()
plt.close()



# %%
# june = df_b[' RH'][df_b['month'] == 6]
# july = df_b[' RH'][df_b['month'] == 7]
# august = df_b[' RH'][df_b['month'] == 8]
# september = df_b[' RH'][df_b['month'] == 9]
import numpy as np

y = 0
avgs = [sum([y + x for x in df_b[' RH'][df_b['month'] == month]])/len(df_b[' RH'][df_b['month'] == month]) for month in df_b['month'].unique()]

plt.bar(range(len(avgs)), avgs)
plt.xlabel("Month")
plt.ylabel('Average')
plt.title("Average RH Per Month")
plt.xticks(np.arange(0, 3.5, 1), [6, 7, 8, 9])
plt.yticks(np.arange(60, 75, 1))
plt.axis([-.5, 3.5, 60, 75])
plt.figure()
plt.show()
plt.close()

# I'm not quite sure which way you wanted it

plt.hist(avgs)
plt.xlabel("Averages")
plt.ylabel('Occurance of Averages')
plt.title("Average RH Per Month")
plt.figure()
plt.show()
plt.close()




# %%
rain = [max([rain for rain in df_b['Rain '][df_b['month'] == month]]) for month in df_b['month'].unique()]

plt.bar(range(len(rain)), rain)
plt.xlabel("Month")
plt.ylabel('Rain')
plt.title("Most Rain in a Day Per Month")
plt.xticks(np.arange(0, 3.5, 1), [6, 7, 8, 9])
plt.figure()
plt.show()
plt.close()


# %%
wind = df_s[' Ws']

plt.hist(wind, bins=5)
plt.xlabel('Wind Speed Value')
plt.ylabel('Occurance of Wind Speed Value')
plt.title('Wind Speed Distribution')
plt.figure()
plt.show()
plt.close()



# %%
plt.plot(range(len(df_s[' RH'])), df_s['Temperature'] )
plt.xlabel("Relative Humidity")
plt.ylabel('Temperature')
plt.title('Correlation between Relative Humidity and Temperature')
plt.figure()
plt.show()
plt.close()

# %%
rh = df_b[' RH']
plt.bar(rh, df_b['day'])
plt.xticks(range(40, 100, 10))
plt.xlabel("Relative Humidity")
plt.ylabel("Days")
plt.title("Distribution of Relative Humidity")
plt.figure()
plt.show()
plt.close()

# %% [markdown]
# 

# %%
# avgs = [sum([y + x for x in df_b['Temperature'][df_b['month'] == month]])/len(df_b[' RH'][df_b['month'] == month]) for month in df_b['month'].unique()]
# print(avgs)

# avg = df_b['Temperature'][(df_b['month'] == 6) & df_b['Classes  '] == 'not fire'] 
# print(avg)

noFire = [df_b[['Temperature', 'month', 'Classes  ']][(df_b['month'] == month) & (df_b['Classes  '] == 'not fire   ')].mean() for month in df_b['month'].unique()]
withFire = [df_b[['Temperature', 'month', 'Classes  ']][(df_b['month'] == month) & (df_b['Classes  '] == 'fire   ')].mean() for month in df_b['month'].unique()]

# plt.bar(6, noFire[0][0])
# plt.bar(7, noFire[1][0])
# plt.bar(8, noFire[2][0])
# plt.bar(9, noFire[3][0])

noFireList = []
noFireList.append(noFire[0][0])
noFireList.append(noFire[1][0])
noFireList.append(noFire[2][0])
noFireList.append(noFire[3][0])

withFireList = []
withFireList.append(withFire[0][0])
withFireList.append(withFire[1][0])
withFireList.append(withFire[2][0])
withFireList.append(withFire[3][0])

plt.subplot(1, 2, 1)
plt.bar(range(6, 10), noFireList, label='No Fire', color='g')
plt.xticks(range(6, 10))
plt.legend(loc='lower center')
plt.xlabel('Months')
plt.ylabel('Average Temperature')
plt.title('Average Temperature Each Month no fire')

plt.subplot(1, 2, 2)
plt.bar(range(6, 10), withFireList, label='Fire')
plt.xticks(range(6, 10))
plt.legend(loc='lower center')

plt.xlabel('Months')
plt.ylabel('Average Temperature')
plt.title('Average Temperature Each Month fire')
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=1,
                    wspace=1.5)
plt.figure()
plt.show()
plt.close()




# %%


# %%



