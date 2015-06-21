#!/usr/bin/python
import json

with open('./web_app/management/commands/freeformatter-out.json') as f:
    text = f.read()
    text.replace('\n', '').replace('\r', '')

text = json.loads(text.replace('\r\n', ''))

for item in text['channel']['item']:
    if "lesson" in item["link"]:
        if item['encoded'][0]:
            filename = item["link"][37:].split("/")[0] + " - " + item["link"][37:].split("/")[1]
            w = open("{0}.txt".format(filename), 'w')
            w.write(item['encoded'][0].encode('utf-8').strip())
            w.close()
