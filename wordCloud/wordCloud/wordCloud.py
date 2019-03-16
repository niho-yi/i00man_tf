
from konlpy.tag import Okt
okt = Okt()
okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
    
filename = './kr-Report_2018.txt'
with open(filename, 'r', encoding='UTF-8') as f:
    texts = f.read()
texts[:300]

import re
texts = texts.replace('\n','')
tokenizer = re.compile('[^ㄱ-힣]+')
texts = tokenizer.sub('',texts)
texts
from nltk.tokenize import word_tokenize
tokens = word_tokenize(texts)
tokens[:7]

noun_token = []
for token in tokens:
    token_pos = okt.pos(token)
    temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
    if len(''.join(temp)) > 1:
        noun_token.append(" ".join(temp))
texts = " ".join(noun_token)
texts[:300]

#불용어
with open('./stopwords.txt', 'r', encoding='UTF-8') as f:
    stopwords = f.read()
stopwords

stopwords = stopwords.split(' ')
stopwords[:10]

#원본에서 불용어 파일에 존재하지 않는 단어들만 추출하라
texts = [text for text in texts if text not in stopwords]
import pandas as pd
from nltk import FreqDist
freqtxt = pd.Series(dict(FreqDist(texts))).sosort_values(ascending=False)
freqtxt[:25]