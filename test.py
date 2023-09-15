import json


query = {'type': {"$in": ["IMAGE", "IMAGE_DIAGRAM"]}, 'status': 'READY', 'ocr.image_status': 'OCR_DONE'}
query.update({'ocr.priority':'Y'})
#print(query)

#print("this is a test string!".split(' '))

path = "./result2.json"
with open(path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    table: list[dict] = list(filter(lambda x: x.get('label') == "table", data['result'][0]['prediction']))
    #print(table)

    part_count = table[0]['cells'][-1]['row'] if table else 0
    #print(part_count)

    table_dict: list[dict] = next(
        filter(lambda x: x.get('label') == "table", data['result'][0]['prediction']), None)
    print(table_dict)

    last_row = table_dict['cells'][-1]['row']
    print(last_row)

    # for i in data['result'][0]['prediction']:
    #     if data['result'][0]['prediction'][i].get('cells'):
    #         print(data['result'][0]['prediction'][i]['cells'][-1]['row'])