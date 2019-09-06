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


def process_line_chart(table):
    axises = {}

    for i, col in enumerate(table['chart_data']):
        if col['mode'] != "lines":
            continue
        if col['yaxis'] in axises.keys():
            axises[col['yaxis']].append(i)
        else:
            axises[col['yaxis']] = [i]
    documents = []
    for yaxis, ids in axises.items():
        if len(ids) == 1:
            i = ids[0]
            column_x = table['df'].columns[2 * i]
            column_y = table['df'].columns[2 * i + 1]
            document = {
                'dataset_id': table['dataset_id'],
                'order': i,
                'locator': table['locator'],
                'type': 'singleseq',
                'name': table['chart_data'][i]['name'],
                'column_x': column_x,
                'column_y': column_y,
                'x': list(table['df'][column_x]),
                'y': list(table['df'][column_y]),
                'col': table['chart_data'][i]
            }
            documents.append(document)
        else:
            min_value = ids[0]
            for i in ids:
                if min_value > i:
                    min_value = i
            document = {
                'dataset_id': table['dataset_id'],
                'order': min_value,
                'orders': ids,
            }
            data = []
            for i in ids:
                column_x = table['df'].columns[2 * i]
                column_y = table['df'].columns[2 * i + 1]
                data.append({
                    'order': i,
                    'column_x': column_x,
                    'column_y': column_y,
                    'x': list(table['df'][column_x]),
                    'y': list(table['df'][column_y]),
                    'col': table['chart_data'][i]
                })
            document['data'] = data
            documents.append(document)






tables = get_plotly_dfs(limit=1)
line_count = 0
count = 0
types = []
client = MongoClient()
collection = client['vis_data'].viznet
for i, table in enumerate(tables):
    print(i)
# try:
#     for table in tables:
#         categories = get_category(table)
#         for col in table['chart_data']:
#             category = None
#             if 'type' in col:
#                 category = col['type']
#             elif 'mode' in col:
#                 category = col['mode']
#         if 'line' in categories:
#             line_count += 1
#         count += 1
#         if count % 1000 == 0:
#             print("finished: ", count)
#         # table['df'][]
#         # try:
#         #     if table['chart_data'][0]['type'] == "line":
#         #         count += 1
#         # except:
#         #     if table['chart_data'][0]['mode'] == "line":
#         #         count += 1
#         # print(table['chart_data'])
# except:
#     print("sa")
# print(count)
# print(types)