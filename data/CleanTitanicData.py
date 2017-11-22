import pandas as pd
import numpy as np

input_data = "E:\\Projects\\datavisualization\\data\\titanic-data.csv"
output_data = "E:\\Projects\\datavisualization\\data\\clean_titanic-data.csv"


df = pd.read_csv(input_data,dtype=str)

df = df.fillna(method='bfill')

df.columns = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']

#df = pd.DataFrame({'Survived': {'0': 'False', '1':'True'}})

df['Survived'] = df['Survived'].map({'0': 'False', '1': 'True'})

#output a TSV
df.to_csv(output_data,sep='\t', encoding='utf-8')

print(df)