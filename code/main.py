import pandas as pd
from db import conn
import matplotlib.pyplot as plt
import seaborn as sns
cursor = conn.cursor()
import matplotlib.pyplot as plt
df= pd.read_csv('Case Study\DATASET FOR CASESTUDY.csv')
# print(df.describe())
year=2019
def Show_Bad_psychologocal_health_frequency():
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
def Punjab_psychosocial_factors_PIECHART(): 
        
 query=""" 
 SELECT psychosocial_factors, family_living_status , COUNT(*) AS psychosocial_factors_count 
 FROM dataquest 
 WHERE indian_states = 'Punjab' 
   AND psychological_health = 'Bad'
   AND psychosocial_factors IS NOT NULL 
   AND education IS NOT NULL
 GROUP BY psychosocial_factors, family_living_status;
 
 """
 cursor.execute(query)
 data = cursor.fetchall()

 labels = list(set([item[0] for item in data]))  # Unique psychosocial factors
 family_status = list(set([item[1] for item in data]))  # Unique family statuses

 # Create a dictionary to store the count of each family status for each psychosocial factor
 counts = {factor: {status: 0 for status in family_status} for factor in labels}
 for item in data:
    factor, status, count = item
    counts[factor][status] += count

 # Plotting the pie chart
 plt.figure(figsize=(10, 8))
 colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink']
 explode = (0.1, 0, 0)  # explode 1st slice
 for i, factor in enumerate(labels):
    plt.subplot(2, 2, i+1)
    sizes = [counts[factor][status] for status in family_status]
    plt.pie(sizes, labels=family_status, colors=colors, autopct='%1.1f%%', startangle=140)
    if (factor=="Smoking"):
        plt.title(factor +"="+"692")
    elif (factor=="Alcohol and Smoking"):
        plt.title(factor +"="+"953")
    elif(factor=="Alcohol"):
        plt.title(factor +"="+"1083")
    else:
        plt.title(factor +"="+"3311")
            


     
    

 plt.suptitle('Distribution of Family Status by Psychosocial Factors in Punjab (Bad Mental Health)')
 plt.tight_layout()
 plt.show()

Punjab_psychosocial_factors_PIECHART()
Show_Bad_psychologocal_health_frequency()
cursor.close()
conn.close()
