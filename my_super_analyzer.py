import argparse
import time
import os
import pandas as pd
import requests
import re

parser = argparse.ArgumentParser(description='CVE')
parser.add_argument('--link', type=str, help='--link URL')
parser.add_argument('--keywords', type=str, help='--keywords "keyword1,keyword2..."')
parser1 = parser.parse_args()

URL = parser1.link

response = requests.get(URL)

with open('thrlist.xlsx', 'wb') as file:
    file.write(response.content)

pd.set_option('display.max_colwidth', None)
df = pd.read_excel('thrlist.xlsx', header = 1)

KEYWORDS_SPLIT = parser1.keywords.split(',')
search_keywords = '|'.join(map(re.escape, KEYWORDS_SPLIT))

matches = df['Наименование УБИ'].str.contains(search_keywords, case=False, na=False, regex=True)

filter = df[matches]

columns_to_display = ['Идентификатор УБИ', 'Наименование УБИ', 'Нарушение конфиденциальности', 'Нарушение целостности', 'Нарушение доступности']

filtered_columns = [col for col in columns_to_display if col in filter.columns]

print(filter[filtered_columns].to_string(index=False))

os.remove('thrlist.xlsx')