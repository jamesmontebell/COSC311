# %%
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
import numpy as np

# %%
df = pd.read_csv('FoodTypeDataset.csv')
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

depth = np.arange(1, 25)
accuracy = np.empty(len(depth))

for i, k in enumerate(depth):
    DT = DecisionTreeClassifier(max_depth=k)
    DT.fit(X_train, y_train)
    accuracy[i] = DT.score(X_train, y_train)
    
print(accuracy)

DT = DecisionTreeClassifier(max_depth = 20, random_state = 0)
DT.fit(X, y)
score = DT.score(X_test, y_test)
print(score)

y_pred = DT.predict(X_test)
report = classification_report(y_test, y_pred)
print(report)

cm = confusion_matrix(y_test,y_pred)
print(cm)

plt.imshow(cm)

# Add a colorbar
plt.colorbar()

# Show the plot
plt.show()

# %%



