import pandas as pd
from db import conn
import matplotlib.pyplot as plt
import seaborn as sns
cursor = conn.cursor()
import matplotlib.pyplot as plt
df= pd.read_csv('Case Study\DATASET FOR CASESTUDY.csv')
# print(df.describe())
year=2019
cursor.execute('SELECT * FROM bad_psychological_health_frequency2017')
data = cursor.fetchall()
states = [item[0] for item in data]
counts = [item[1] for item in data]
plt.figure(figsize=(10, 6))
plt.bar(states, counts, color='skyblue')
plt.xlabel('States')
plt.ylabel(f'Frequency of Bad Psychological Health {year}')
plt.title(f'Frequency of Bad Psychological Health State-wise {year}')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
print(data)
cursor.close()
conn.close()
