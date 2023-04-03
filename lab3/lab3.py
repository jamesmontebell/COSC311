# %%
import numpy as np
import pandas as pd
import stats
from matplotlib import pyplot as plt

# %%
df_b = pd.read_csv("Bejaia_Region.csv")
df_s = pd.read_csv("Sidi-Bel_Abbes_Region.csv")

# %%
temp = df_b['Temperature'][df_b['Classes  '] == 'fire   '].mean()
rh = df_b[' RH'][df_b['Classes  '] == 'fire   '].mean()
ws = df_b[' Ws'][df_b['Classes  '] == 'fire   '].mean()
rain = df_b['Rain '][df_b['Classes  '] == 'fire   '].mean()

means_fire_y = sorted([temp, rh, ws, rain])
means_fire = sorted({"temp":temp, "rh":rh, "ws":ws, "rain":rain})

tempN = df_b['Temperature'][df_b['Classes  '] == 'not fire   '].mean()
rhN = df_b[' RH'][df_b['Classes  '] == 'not fire   '].mean()
wsN = df_b[' Ws'][df_b['Classes  '] == 'not fire   '].mean()
rainN = df_b['Rain '][df_b['Classes  '] == 'not fire   '].mean()

means_nofire_y = sorted([tempN, rhN, wsN, rainN])
means_nofire = sorted({"temp":tempN, "rh":rhN, "ws":wsN, "rain":rainN})


# %%
plt.subplot(1, 2, 1)
plt.bar(means_fire,means_fire_y)
plt.xticks([means_fire[0], means_fire[1], means_fire[2], means_fire[3]])
plt.xlabel("Attributes")
plt.ylabel("Means")
plt.title("Mean values of the 'Bejaia Region Dataset' with fire")

plt.subplot(1, 2, 2)
plt.bar(means_nofire,means_nofire_y)
plt.xticks([means_nofire[0], means_nofire[1], means_nofire[2], means_nofire[3]])
plt.xlabel("Attributes")
plt.ylabel("Means")
plt.title("Mean values of the 'Bejaia Region Dataset' with no fire")
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.01, right=1.20, hspace=1,
                    wspace=1.5)
plt.show()

#Observations: both plots are very similar, no fire shows more rain with no fire

# %%
ffmc = df_s['FFMC'].mean()
dmc = df_s['DMC'].mean()
# dc = df_s['DC'].max() weird error with finding mean of DC
isi = df_s['ISI'].mean()   

means = [ffmc, dmc, isi]

print(means)

# %%
temp = df_b['Temperature'].quantile(.25)
rh = df_b[' RH'].quantile(.25)
ws = df_b[' Ws'].quantile(.25)
rain = df_b['Rain '].quantile(.25)

tf = [temp, rh, ws, rain]
print(tf)

temp = df_b['Temperature'].quantile(.60)
rh = df_b[' RH'].quantile(.60)
ws = df_b[' Ws'].quantile(.60)
rain = df_b['Rain '].quantile(.60)

sixty = [temp, rh, ws, rain]
print(sixty)

temp = df_b['Temperature'].quantile(.75)
rh = df_b[' RH'].quantile(.75)
ws = df_b[' Ws'].quantile(.75)
rain = df_b['Rain '].quantile(.75)

sf = [temp, rh, ws, rain]
print(sf)

# %%
temp = df_s['Temperature'].std()
rain = df_s['Rain '].std()
bui = df_s['BUI'].std()
fwi = df_s['FWI'].std()

std = [temp, rain, bui, fwi]
print(std)

# %%
print(stats.correlation(df_s[' RH'], df_s['Temperature']))
print(stats.correlation(df_s[' RH'], df_s[' Ws']))
print(stats.correlation(df_s[' RH'], df_s['Rain ']))
print(stats.correlation(df_s[' RH'], df_s['FFMC']))
print(stats.correlation(df_s[' RH'], df_s['DMC']))
# print(stats.correlation(df_s[' RH'], df_s['DC'])) Weird error with this column
print(stats.correlation(df_s[' RH'], df_s['ISI']))
print(stats.correlation(df_s[' RH'], df_s['BUI']))
print(stats.correlation(df_s[' RH'], df_s['FWI']))

#strongest positive: RH and Rain
#strongest negative: RH and ISI

# %%
temp1 = df_b['Temperature'][df_b['Classes  '] == 'fire   '].values
temp2 = df_b['Temperature'][df_b['Classes  '] == 'not fire   '].values

rain1 = df_b['Rain '][df_b['Classes  '] == 'fire   '].values
rain2 = df_b['Rain '][df_b['Classes  '] == 'not fire   '].values

print(stats.correlation(temp1, rain1))
print(stats.correlation(temp2, rain2))

#correlation between temperature and rain with fire and without fire


# %%



