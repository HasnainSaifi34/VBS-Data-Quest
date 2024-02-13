import pandas as pd
from db import conn
import matplotlib.pyplot as plt
import seaborn as sns
cursor = conn.cursor()
df= pd.read_csv('Case Study\DATASET FOR CASESTUDY.csv')
print(df.describe())

cursor.close()
conn.close()
