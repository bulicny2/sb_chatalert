

import os
import pandas as pd
import requests
import json

data = pd.read_csv('../local/le-records-by-keyword.csv')
def get_html(data):
    links = {}
    count = 0
    for url in data['url']:
        count += 1
        r = requests.get(url)
        links[url] = r.text
        print("url complete: {}, count: {}".format(url, count))
    return links

with open('getHtml.json', 'w') as outfile:
    json.dump(get_html(data), outfile)
    outfile.close()
    

