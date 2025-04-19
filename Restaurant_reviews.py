import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

df = pd.read_csv("Restaurant_reviews.csv")

df.drop('7514', axis=1, inplace=True)
#Drop the null values from reviewer and review columns
df.dropna(subset=['Reviewer', 'Review'], inplace=True)

df['Rating'] = df['Rating'].replace('Like', 1.5)
df['Rating'] = df['Rating'].astype(float)
df['Time'] = pd.to_datetime(df['Time'])

# Example: assuming your column is named 'Metadata'
df[['no_of_reviews', 'followers']] = df['Metadata'].str.extract(r'(\d+) Review[s]? , (\d+) Follower[s]?')

# Convert the extracted values to integers
df['no_of_reviews'] = df['no_of_reviews'].fillna(0).astype(int)
df['followers'] = df['followers'].fillna(0).astype(int)

df.drop('Metadata', axis=1, inplace=True)

#VADER lexicon
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

#classify sentiment
def get_sentiment(text):
  score = sia.polarity_scores(str(text))['compound']
  if score >= 0.05:
    return 'Positive'
  elif score <= -0.05:
    return 'Negative'
  else:
    return 'Neutral'

df['Sentiment'] = df['Review'].apply(get_sentiment)
#Show output
df[['Review', 'Sentiment']].head(5)

df['Sentiment'].value_counts()

#save clean file in csv file 
df.to_csv("Restaurant_review_cln.csv")

# ----------------------Save to MySQL server -------------------------------------
import pymysql

connection = pymysql.connect(host='localhost', user='root', password="GKB@mysql_ds07", database='codeit') 
cursor = connection.cursor()

df = pd.read_csv('Restaurant_review_cln.csv')
#insert into MySQL table
for _, row in df.iterrows():
    cursor.execute("""INSERT INTO Restaurant_review_cln (Restaurant, Reviewer, Review, Rating, Time, Pictures,
        no_of_reviews, followers, Sentiment)
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (row["Restaurant"], row["Reviewer"], row["Review"], row["Rating"],row["Time"],row["Pictures"],row["no_of_reviews"],row["followers"], row["Sentiment"]))

connection.commit()
print("Data inserted successfully")

querry = "SELECT * FROM Restaurant_review_cln"
cursor.execute(querry)
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()