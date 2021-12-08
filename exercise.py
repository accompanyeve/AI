# import pandas as pd
# import numpy as np
# df = pd.read_csv("./testdata/train_dataset.csv",sep = '|', names = ['a', 'b'])
# df.drop(df.columns[[0,]], axis=1, inplace=True)
# df = df['b'].str.split('.',3, expand = True).rename(columns={0:'d0', 1:'d1',2:'d2',3:'data'})
# df.drop(df.columns[[0,1,2]], axis=1, inplace=True)
# df = df.dropna()
# df.to_csv("./testdata/pretreatment_train_dataset.csv",index=False,sep='|')

#df.drop(df.columns[[0,]], axis=1, inplace=True)
#print(df.head())
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
import pandas as pd
import numpy as np
import spacy
nlp = spacy.load('en_core_web_sm')
df = pd.read_csv("./testdata/test.csv",sep = '|')
doc = nlp("He went to play basketball")
#print(nlp.pipe_names)
#词性标注
for token in doc:
    # Print the token and its part-of-speech tag
    print(token.text, "-->", token.pos_)
# 依存分析
for token in doc:
    print(token.text, "-->", token.dep_)
print(spacy.explain("nsubj"), spacy.explain("ROOT"), spacy.explain("aux"), spacy.explain("advcl"), spacy.explain("dobj"))
