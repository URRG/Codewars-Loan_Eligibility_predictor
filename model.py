import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import GradientBoostingClassifier

df = pd.read_csv('a.csv')
print(df.head())
print(df.isnull().sum())
df.fillna(df.mean(), inplace=True)
print(df.isnull().sum())
df.Gender.fillna(df.Gender.mode()[0], inplace=True)
df.Married.fillna(df.Married.mode()[0], inplace=True)
df.Dependents.fillna(df.Dependents.mode()[0], inplace=True)
df.Self_Employed.fillna(df.Self_Employed.mode()[0], inplace=True)
print(df.isnull().sum())
df.Loan_Amount_Term=np.log(df.Loan_Amount_Term)
df = df.drop('Loan_ID', axis=1)
X = df.drop('Loan_Status', 1)
Y = df.Loan_Status
X = pd.get_dummies(X)
df = pd.get_dummies(df)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)
model=GradientBoostingClassifier()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print(classification_report(Y_test, Y_pred))

import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
