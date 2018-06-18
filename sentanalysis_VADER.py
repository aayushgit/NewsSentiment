import csv
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

news = []
with open("fin_news.csv") as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]
    data.pop(0)  # remove header
    x = 0
    while x < len(data):
        news.append(data[x]['content'])
        x = x + 1
# print(news)

sia = SIA()
results = []
for line in news:
    pol_score = sia.polarity_scores(line)
    pol_score['news'] = line
    results.append(pol_score)

pprint(results,width=100)
# x=0
# while x < len(results):
#     if results[x]['compound']<0:
#         print(results[x])
#     x=x+1


