import json
def load_data(filename):
    data = []
    with open(filename, encoding='utf-8') as f:
        for l in f:
           # print("**: ", l)
            data.append(l)
    return data


with open("summary.json",'r') as load_f:
     ss = json.load(load_f)
# text = load_data(text_json)
# summary = load_data("summary.json")
print(len(ss))
print(ss[2])

