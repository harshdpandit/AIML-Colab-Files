# -*- coding: utf-8 -*-
"""AIML Project H036 & H037 sem6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O5IC05pdQmXtx4r9c-Fx8VbJpU48eSb_
"""

import pandas as pd
#importing the dataset
data_frame=pd.read_csv('IMDB dataset.csv')
#dropping the poster link column in dataset
data_frame=data_frame.drop([data_frame.index[966]])
data_frame=data_frame.drop('Poster_Link',axis=1)
#dropping all null values from the dataset
data_frame=data_frame.dropna()
#creating a new column
data_frame['Movie score']=data_frame['Meta_score']*data_frame['IMDB_Rating']
#dropping the meta score and imdb rating column
data_frame=data_frame.drop('Meta_score',axis=1)
data_frame=data_frame.drop('IMDB_Rating',axis=1)
#replacing all the values of U/A with UA
data_frame['Certificate']=data_frame['Certificate'].replace('U/A','UA')

def convert_string_to_ascii(string_list):
  list_num=[]
  pronunciation_chars=(' ',',','-','/')
  for values in string_list:
    temp=0
    for char in values:
      if char not in pronunciation_chars:
      #converting the characters in string into number
      #ord(char) converts the string character into its associated ascii value
      #adding the ascii values of characters present into name excpet for
      # blankspace and comma
        temp+=ord(char)
    list_num.append(temp)
  return list_num

data_frame['Director']=convert_string_to_ascii(data_frame['Director'])
data_frame['Star1']=convert_string_to_ascii(data_frame['Star1'])
data_frame['Star2']=convert_string_to_ascii(data_frame['Star2'])
data_frame['Star3']=convert_string_to_ascii(data_frame['Star3'])
data_frame['Star4']=convert_string_to_ascii(data_frame['Star4'])
data_frame['Certificate']=convert_string_to_ascii(data_frame['Certificate'])
data_frame['Genre']=convert_string_to_ascii(data_frame['Genre'])

data_frame.head()

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import one_hot
#vocabulary size
voc_size=10000
import string
import numpy as np
temp_lst=data_frame['Overview']
another_lst=[]
for i in temp_lst:
  s = i.translate(str.maketrans('', '', string.punctuation))
  another_lst.append(s)
data_frame['Overview']=another_lst
#maximum length of a sentence
sent_length=300

sentences=data_frame['Overview']
one_hot_rep=[one_hot(words,voc_size)for words in sentences]
print(one_hot_rep)

embedded_docs=pad_sequences(one_hot_rep,padding='pre',maxlen=sent_length)

dim=15
model=Sequential()
model.add(Embedding(voc_size,dim,input_length=sent_length))
model.compile('adam','mse')

temp=model.predict(embedded_docs)
print(temp)

lst2=[]
sum=0
for vals in temp:
  lst1=[]
  for subvals in vals:
    sum=0
    for furthersuvals in subvals:
      sum+=furthersuvals
    lst1.append(sum)
  lst2.append(lst1)
data_frame['Overview']=lst2

lst2=[]
sum=0
for vals in data_frame['Overview']:
  lst1=[]
  for subvals in vals:
    sum=0
    sum+=subvals
  lst2.append(sum)
data_frame['Overview']=lst2

runtime=[]
for time_vals in data_frame['Runtime']:
  runtime.append(int(time_vals.replace(' min','')))
data_frame['Runtime']=runtime

data_frame.head()

movie_names=data_frame['Series_Title']
data_frame=data_frame.drop('Series_Title',axis=1)

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt

y1=data_frame['Movie score']
lst=[]
for values in data_frame['Gross']:
  lst.append(int(values.replace(',','')))
data_frame['Gross']=lst
y2=data_frame['Gross']

x=data_frame.drop(['Gross','Movie score'],axis=1)

x_train,x_test,y1_train,y1_test=train_test_split(x,y1,test_size=0.2)
x_train,x_test,y2_train,y2_test=train_test_split(x,y2,test_size=0.2)

#using linear regression model to find the value of movie score
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y2_train)

slope=model.coef_
intercept=float(model.intercept_)
r_sq=model.score(x_train,y2_train)
print('The r-squared value is : {}'.format(r_sq))
print('The value of intercept is : {}'.format(intercept))
print('The value of slope is : {}'.format(slope))

model=LinearRegression()
model.fit(x_train,y1_train)
slope=model.coef_
intercept=float(model.intercept_)
r_sq=model.score(x_train,y1_train)
print('The r-squared value is : {}'.format(r_sq))
print('The value of intercept is : {}'.format(intercept))
print('The value of slope is : {}'.format(slope))

from sklearn.tree import DecisionTreeRegressor
model_tree=DecisionTreeRegressor(random_state=0)
model_tree.fit(x_train,y1_train)
y1_pred=model.predict(x_test)
error= sqrt(mean_squared_error(y1_test, y1_pred))
print('The error value is: {}'.format(error))

model_tree.fit(x_train,y2_train)
y2_pred=model.predict(x_test)
error= sqrt(mean_squared_error(y2_test, y2_pred))
print('The error value is: {}'.format(error))

data_frame.head()

x=data_frame.drop('Overview',axis=1)
x_train,x_test,y1_train,y1_test=train_test_split(x,y1,test_size=0.2)
x_train,x_test,y2_train,y2_test=train_test_split(x,y2,test_size=0.2)

model=LinearRegression()
model.fit(x_train,y2_train)

slope=model.coef_
intercept=float(model.intercept_)
r_sq=model.score(x_test,y2_test)
print('The r-squared value is : {}'.format(r_sq))
print('The value of intercept is : {}'.format(intercept))
print('The value of slope is : {}'.format(slope))

model.fit(x_train,y1_train)
slope=model.coef_
intercept=float(model.intercept_)
r_sq=model.score(x_train,y1_train)
print('The r-squared value is : {}'.format(r_sq))
print('The value of intercept is : {}'.format(intercept))
print('The value of slope is : {}'.format(slope))

model_tree=DecisionTreeRegressor(random_state=0)
model_tree.fit(x_train,y1_train)
y1_pred=model.predict(x_test)
error= sqrt(mean_squared_error(y1_test, y1_pred))
print('The error value is: {}'.format(error))

model_tree.fit(x_train,y2_train)
y2_pred=model.predict(x_test)
error= sqrt(mean_squared_error(y2_test, y2_pred))
print('The error value is: {}'.format(error))

