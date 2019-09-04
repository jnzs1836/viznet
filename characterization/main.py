from read_raw_data import get_plotly_dfs
from pymongo import MongoClient
def get_axis(name):
    return [name + ', x', name + ', y']
def get_category(table):
    categories = []
    for col in table['chart_data']:
        category = None
        if 'type' in col:
            category = col['type']
        elif 'mode' in col:
            category = col['mode']
        if category:
            if category not in types:
                categories.append(category)
    return categories

tables = get_plotly_dfs()
line_count = 0
count = 0
types = []
client = MongoClient()
collection = client['vis_data'].viznet

try:
    for table in tables:
        categories = get_category(table)
        for col in table['chart_data']:colle
            category = None
            if 'type' in col:
                category = col['type']
            elif 'mode' in col:
                category = col['mode']
        if 'line' in categories:
            line_count += 1
        count += 1
        if count % 1000 == 0:
            print("finished: ", count)
        # table['df'][]
        # try:
        #     if table['chart_data'][0]['type'] == "line":
        #         count += 1
        # except:
        #     if table['chart_data'][0]['mode'] == "line":
        #         count += 1
        # print(table['chart_data'])
except:
    print("sa")
print(count)
print(types)