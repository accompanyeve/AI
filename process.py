import numpy as np
import pandas as pd 
import re
import warnings
import json
pd.set_option("display.max_colwidth", 200)
warnings.filterwarnings("ignore")
data = pd.read_csv("./testdata/train_dataset.csv",index_col = 0,sep='\t',names=['index','Text','Summary'])

data.drop_duplicates(subset=['Text'],inplace=True)#dropping duplicates
data.dropna(axis=0,inplace=True)#dropping na
data.info()
contraction_mapping = {"ain't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not",
                           "didn't": "did not",  "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not",
                           "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",
                           "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would",
                           "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would",
                           "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam",
                           "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have",
                           "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock",
                           "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have",
                           "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is",
                           "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as",
                           "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would",
                           "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have",
                           "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have",
                           "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are",
                           "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",
                           "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is",
                           "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have",
                           "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have",
                           "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all",
                           "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have",
                           "you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have",
                           "you're": "you are", "you've": "you have"}
                
#stop_words = set(stopwords.words('english')) 

def text_cleaner(text,num):
    newString = text.lower()
    #newString = BeautifulSoup(newString, "lxml").text
    newString = re.sub(r'\([^)]*\)', '', newString)
    newString = re.sub('"','', newString)
    newString = re.sub('^.*?\|','',newString)
    newString = re.sub('.\supdated\s:\s.\s\d{2}:\d{2}\sest\s,\s\d+\s(february|march|april|may|june|july|august|september|october|november|december)\s\d+\s.','',newString)
    newString = ' '.join([contraction_mapping[t] if t in contraction_mapping else t for t in newString.split(" ")])    
    newString = re.sub(r"'s\b","",newString)
    newString = re.sub("[^a-zA-Z]", " ", newString) 
    newString = re.sub('[m]{2,}', 'mm', newString)
    if(num==0):
        tokens=newString.split()
        #tokens = [w for w in newString.split() if not w in stop_words]
    else:
        tokens=newString.split()
    # long_words=[]
    # for i in tokens:
    #     if len(i)>1:                                                 #removing short word
    #         long_words.append(i)   
    # return (" ".join(long_words)).strip()
    return (" ".join(tokens)).strip()

#call the function
cleaned_text = []
for t in data['Text']:
    cleaned_text.append(text_cleaner(t,0)) 

#call the function
cleaned_summary = []
for t in data['Summary']:
    cleaned_summary.append(text_cleaner(t,1))

data['cleaned_text']=cleaned_text
data['cleaned_summary']=cleaned_summary

data.replace('', np.nan, inplace=True)
data.dropna(axis=0,inplace=True)



text_word_count = []
summary_word_count = []
max_text_len=1000
max_summary_len=70
cnt=0
for i in data['cleaned_summary']:
    if(len(i.split())<=max_summary_len):
        cnt=cnt+1
print("max_summary_len "+str(max_summary_len)+"  "+str(cnt/len(data['cleaned_summary'])))
cnt=0
for i in data['cleaned_text']:
    if(len(i.split())<=max_text_len):
        cnt=cnt+1
print("max_text_len "+str(max_text_len)+"  "+str(cnt/len(data['cleaned_text'])))

cleaned_text =np.array(data['cleaned_text'])
cleaned_summary=np.array(data['cleaned_summary'])


short_text=[]
short_summary=[]

for i in range(len(cleaned_text)):
    if(len(cleaned_summary[i].split())<=max_summary_len and len(cleaned_text[i].split())<=max_text_len):
        tmp_text=[]
        tmp_summary=[]
        tmp_text.append(cleaned_text[i])
        tmp_summary.append(cleaned_summary[i])
        short_text.append(tmp_text)
        short_summary.append(tmp_summary)
        
#df=pd.DataFrame({'text':short_text,'summary':short_summary})

# dic_summary={}
# dic_text={}
# import json
# for i in range(len(short_summary)):
#     dic_summary[i]=short_summary[i]

# for j in range(len(short_text)):
#     dic_text[j]=short_text[j]

# summary = json.dump(short_summary)
# text = json.dump(short_text)


with open("summary.json","w") as f:
     json.dump(short_summary,f)

with open("text.json","w") as f1:
     json.dump(short_text,f1)
# with open('summary.json','w',encoding='utf-8') as f:
#     f.write(summary)
# with open('text.json','w',encoding='utf-8') as f1:
#     f1.write(text)    
# s = json.loads(summary)
# print(len(s))
# print(s[0])