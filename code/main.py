import pandas as pd
from db import conn
import matplotlib.pyplot as plt
import seaborn as sns
cursor = conn.cursor()
import matplotlib.pyplot as plt
df= pd.read_csv('Case Study\DATASET FOR CASESTUDY.csv')
# print(df.describe())

cursor.execute('SELECT * FROM bad_psychological_health_frequency')
data = cursor.fetchall()
states = [item[0] for item in data]
counts = [item[1] for item in data]
plt.figure(figsize=(10, 6))
plt.bar(states, counts, color='skyblue')
plt.xlabel('States')
plt.ylabel('Frequency of Bad Psychological Health')
plt.title('Frequency of Bad Psychological Health State-wise')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
# print(data)
cursor.close()
conn.close()
