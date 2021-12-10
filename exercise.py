from os import sep
import pandas as pd
# import numpy as np
df = pd.read_csv("./testdata/train_dataset.csv",sep='&',names=['ab'])
tmp1 = pd.DataFrame()
tmp2 = pd.DataFrame()
i = 0
t = 0
# if i<10:
#     t=0
# print(df.iloc[0]['ab'][0:6])
# print(df.iloc[22]['ab'][0:7])
# print(df.iloc[111]['ab'][0:8])
# print(df.iloc[1111]['ab'][0:9])

#str = "by ."
#print(df.iloc[101]['ab'][0:7])
# def creat(t):
#     print(t)
# df[0].apply(creat)

for i in range(9000):
    if i<10:
        t = 0
    elif i < 100:
        t = 1
    elif i < 1000:
        t = 2
    else:
        t = 3
    if df.iloc[i]['ab'][0:6+t].replace("\t","") == str(str(i)+"by ."):
        tmp1 = tmp1.append(df.iloc[i])
    else:
        tmp2 = tmp2.append(df.iloc[i])
tmp1.to_csv("./testdata/tmp1.csv",sep="｜")
tmp2.to_csv("./testdata/tmp2.csv",sep="｜")


# print(df.iloc[0]['a'][2:6])
#df.drop(df.columns[[1,]], axis=1, inplace=False)
#df.drop(df.columns[[0,]], axis=1, inplace=True)
# df = df['b'].str.split('.',3, expand = True).rename(columns={0:'d0', 1:'d1',2:'d2',3:'data'})
# df.drop(df.columns[[0,1,2]], axis=1, inplace=True)
# df = df.dropna()
# df.to_csv("./testdata/p_train_dataset.csv",index=False,sep='|')

#df.drop(df.columns[[0,]], axis=1, inplace=True)

# import pandas as pd

# df = pd.DataFrame([
#         [6, "a: 1, b: 2"],
#         [6, "a: 1, b: 2"],
#         [6, "a: 1, b: 2"],
#         [6, "a: 1, b: 2"],
#     ], columns=['ID', 'dictionary'])
# print(df)
# df = df['dictionary'].str.split(':',2, expand = True).rename(columns={0:'d1', 1:'d2',2:'d3'})
# print(df)
# print(df['d3'])
# import pandas as pd
# import numpy as np
# import spacy
# from spacy.matcher import Matcher
# nlp = spacy.load('en_core_web_sm')
# df = pd.read_csv("./testdata/test.csv",sep = '|')
#doc = nlp("Tim went to play basketball")
#print(nlp.pipe_names)
#词性标注
# for token in doc:
#     # Print the token and its part-of-speech tag
#     print(token.text, "-->", token.pos_)
# # 依存分析
# for token in doc:
#     print(token.text, "-->", token.dep_)
# print(spacy.explain("nsubj"), spacy.explain("ROOT"), spacy.explain("aux"), spacy.explain("advcl"), spacy.explain("dobj"))
# # 命名实体
# for ent in doc.ents:
#     print(ent.text, ent.label_)
# #用spaCy词汇表初始化Matcher
# matcher = Matcher(nlp.vocab)
# doc = nlp("Some people start their day with lemon water")
# # 定义规则
# pattern = [{'TEXT': 'lemon'}, {'TEXT': 'water'}]
# # 添加规则
# matcher.add('rule_1', None, pattern)
# df = pd.read_csv("./testdata/train_dataset.csv",sep = '|', names = ['a', 'b'])
# print(df.info())