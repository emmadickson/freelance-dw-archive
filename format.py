import json

formatted_pages = open('index.js', 'w')
pages = open('resources/pages.jsonl', 'r')

test = {}
index = 0
lines = pages.read().split("\n")
for line in lines:
    if (index != 0 and line != ''):
        json_line = json.loads(line)
        test[json_line['text']] = [json_line['url'], json_line['title']]
    index = index + 1
formatted_pages.write("var index = ");
formatted_pages.write(json.dumps(test))
formatted_pages.write(";");