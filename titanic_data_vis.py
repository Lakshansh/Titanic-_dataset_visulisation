# -*- coding: utf-8 -*-
"""Titanic_data_vis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L8oF_XWaC1wHMdjCL9CgMqC_kFjeT9jr
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import sklearn as sk
from sklearn.model_selection import train_test_split



train = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
lables = train.Survived

train .info()

train.isnull().sum()

def bar_chart(feature):
  survived = train[train['Survived']==1][feature].value_counts()
  dead = train[train['Survived']==0][feature].value_counts()
  df = pd.DataFrame([Survived,dead])
  df.index = ['Survived','Dead']
  df.plot(kind='bar',stacked=True,figsize=(10,5))
  plt.show()

sns.countplot(x='Sex', hue='Survived', data=train)

def bar_chart(feature):
    ax = sns.countplot(x=feature, data=train, hue='Survived')
    ax.set_title(f'{feature} vs Survived')
    for p in ax.patches:
        ax.annotate(format(p.get_height()),
                    (p.get_x() + p.get_width() / 2., p.get_height() + 1),
                    ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                    textcoords='offset points')
bar_chart('Sex')

bar_chart('Pclass')

print("Survival percentage of pessenger in 1st class -",(136/(134+80)*100))
print("Survival percentage of pessenger in 1st class -",(87/(87+97)*100))
print("Survival percentage of pessenger in 2nd class -",(119/(119+372)*100))

plt.figure(figsize=(20, 5))
sns.set(style="darkgrid")
sns.distplot(train['Age'], bins=40, kde=True)

# Adding labels and title for better visualization
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')
plt.show()

def age_pie(x, y, title):
    # Calculate the total count and survived count in the given age range
    total_010 = train.loc[(train['Age'] >= x) & (train['Age'] <= y), 'Survived'].count()
    survived_010 = train.loc[(train['Age'] >= x) & (train['Age'] <= y), 'Survived'].sum()

    # Prepare data for the pie chart
    dead_010 = total_010 - survived_010
    labels = ['Dead', 'Survived']
    values = [dead_010, survived_010]

    # Create the pie chart
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title(title)
    plt.show()

# Call the function with different age ranges
age_pie(0, 10, 'Percentage of people who died and survived (Age 0-10)')
age_pie(10, 20, 'Percentage of people who died and survived (Age 10-20)')

age_pie(20, 30, 'Percentage of people who died and survived (Age 20-30)')

train['SibSp'].nunique()

ax = sns.countplot(x='SibSp', data=train, hue='Survived')
for p in ax.patches:
    ax.annotate(format(p.get_height()),
                (p.get_x(), p.get_height() + 1))

plt.figure(figsize=(20, 5))
plt.subplot(122)
sns.barplot(x='SibSp', y='Survived',data=train)
plt.subplot(122)
sns.barplot(x='Parch', y='Survived',data=train)
plt.subplots_adjust(wspace=0.5)

plt.figure(figsize=(20, 5))
sns.set(style="darkgrid")
sns.distplot(train['Fare'])

facet = sns.FacetGrid(train, hue="Survived",aspect=4)
facet.map(sns.kdeplot,'Fare',shade= True)
facet.set(xlim=(0, train['Fare'].max()))
facet.add_legend()

#Data Cleaning and processing
plt.figure(figsize=(12,8))
sns.heatmap(train.isnull(),annot=True,cmap='viridis')

train.Age.mean()

train.Age.isnull().sum()

train.groupby('Pclass').Age.mean()

def input_age(cols):
  Age = cols[0]
  Pclass = cols[1]

  if pd.isnull(Age):
    if Pclass == 1:
      return 38
    elif Pclass == 2:
      return 30
    else:
      return 25
  else:
    return Age

train['Age']=train[['Age','Pclass']].apply(input_age,axis=1)

plt.figure(figsize=(12,8))
sns.heatmap(train.isnull(),annot=True,cmap='viridis')

train.drop('Cabin',axis=1,inplace=True)

plt.figure(figsize=(12,8))
sns.heatmap(train.isnull(),annot=True,cmap='viridis')

train.info()

train['Male'] = pd.get_dummies(train['Sex'],drop_first=True)

train.drop(['PassengerId','Name','Sex','Ticket'],axis=1,inplace=True)

train.head()

train.info()

train = pd.get_dummies(train, columns=['Embarked'], drop_first=True)

X = train.drop('Survived',axis=1)
y = train['Survived']

X.info()

y

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=0)

from sklearn.ensemble import RandomForestClassifier
cfl = RandomForestClassifier(n_jobs=-1, n_estimators=14)
cfl.fit(x_train, y_train)

