import pandas as pd
from datetime import date
import time

import preprocessing
import prompt

today = date.today().strftime('%d/%m/%Y')

data = pd.read_csv('data.csv', delimiter='|', encoding='latin_1')

filtered_data = data[data.date == str(today)]

for type in filtered_data.type.unique().tolist():
    mask_data = filtered_data[filtered_data.type == type]
    all_sumaries = '\n'.join(mask_data.summary.tolist())
    chunks = preprocessing.chop(all_sumaries)
    flag, summary = prompt.summarize_all_articles(chunks, type=type)
    print('\n')
    print("***********************")
    print(type)
    print(summary)
    print(flag)
    time.sleep(15)