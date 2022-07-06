## importing necessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
data= pd.read_csv("https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv")
y= data["Scores"]
x= data["Hours"]

## scatter plot
plt.scatter(data.Hours, data.Scores)
plt.title("Hours Studied vs. Exam Score")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.show()

## boxplot
data.boxplot(column=["Scores"])
plt.show()

## 
model= sm.OLS(y, x).fit()
print(model.summary())