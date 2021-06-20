import vk
import requests
import json
import pandas as pd

session = vk.Session(access_token='afdbff07da35ea82487539fb67d95f3a8420b9d3fe19ea65bf91311f7064f50f3eeafc5d3d18ef5f15adc')
vk_api = vk.API(session)
response = requests.get('https://api.vk.com/method/newsfeed.get?filters=post&count=1000&access_token=0622eec3c92465def820080150740dfe95b6bf3446118d711981d7dc761c7ea769c726c2c23d2582a332b&v=5.21')
dct = dict()
dct['posts'] = []
todos = json.loads(response.text)
print(todos)
for todo in todos["response"]["items"]:
    with open("data_file.txt", "a") as write_file:
        write_file.write(todo["text"])
        dct['posts'].append(todo["text"])
       # json.dump(todo["text"], write_file)
print(todos == response.json()) # True
# df = pd.DataFrame
print(dct["posts"])
df = pd.DataFrame(dct["posts"])
print(df)
df.to_excel('./teams.xlsx')

