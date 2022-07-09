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

def model(h):
  s_cap= 10.1743*h
  print("The estimated score of a student who studies for {} hours per day is {}".format(h, round(s_cap, 2)))
  
h= 9.25
model(h)        
