import pandas as pd

iris = pd.read_csv("IRIS.csv")

print("head: = ")
print(iris.head())

print("-----------------------------------------------------------")

print("iris['Species'].value_counts() = \n", iris["Species"].value_counts())

print("-----------------------------------------------------------")

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="white", color_codes=True)

df_setosa = iris[iris["Species"] == "setosa"]
print(df_setosa)

df_setosa["Sepal.Width"].hist()

plt.show()

"""
sns.FacetGrid(iris, hue="Species",height=5).map(plt.scatter, "Sepal.Length", "Sepal.Width").add_legend()
sns.boxplot(x="Species", y="Petal.Width", data=iris)
plt.show()
"""
