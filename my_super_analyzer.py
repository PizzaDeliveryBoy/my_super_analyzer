import argparse
import time
import os
import pandas as pd
import webbrowser
import re

parser = argparse.ArgumentParser(description='CVE')
parser.add_argument('--link', type=str, help='--link URL')
parser.add_argument('--keywords', type=str, help='--keywords "keyword1,keyword2..."')
parser1 = parser.parse_args()

FILE_URL = parser1.link
FILE_PATH = os.path.expanduser("~/Downloads/thrlist.xlsx")

webbrowser.open(FILE_URL)
time.sleep(5)

pd.set_option('display.max_colwidth', None)
df = pd.read_excel(FILE_PATH, header = 1)

KEYWORDS_SPLIT = parser1.keywords.split(',')
search_keywords = '|'.join(map(re.escape, KEYWORDS_SPLIT))

matches = df['Наименование УБИ'].str.contains(search_keywords, case=False, na=False, regex=True)

filter = df[matches]

print(filter['Наименование УБИ'].to_string(index=False))

os.remove(FILE_PATH)