import pandas as pd
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.preprocessing import OneHotEncoder
df=pd.read_csv('housing.csv')
df=pd.get_dummies(df,columns=['ocean_proximity'])
plt.figure(figsize=(6,5))
df=df.fillna(df.mean())
X = df.drop(columns=['median_house_value'])
y=df['median_house_value']
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.7,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
model.predict(x_test)
print(model.score(x_test,y_test)  crate a repo and upload r2 =64
