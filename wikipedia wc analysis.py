import wikipedia
from wordcloud import WordCloud, STOPWORDS
lang=input("사용할 언어 입력 : ")

if lang=="한국어":
    wikipedia.set_lang("ko")
    title=input("분석할 문서 입력 : ")
    wiki=wikipedia.page(title)
    text=wiki.content

    from konlpy.tag import Okt
    okt=Okt()
    text=okt.nouns(text)

    wordcloud=WordCloud(font_path='NanumBarunGothic',background_color='white')

    stopwords=['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
    clean_text=[word for word in text if not word in stopwords]
    from collections import Counter
    c=Counter(clean_text)
    wordcloud.generate_from_frequencies(c)
elif lang=="영어":
    wikipedia.set_lang("en")
    title=input("분석할 문서 입력 : ")
    wiki=wikipedia.page(title)
    text=wiki.content

    s_words=STOPWORDS.union({'one','using','first','two','make','use'})
    wordcloud=WordCloud(stopwords=s_words,background_color='white').generate(text)

import matplotlib.pyplot as plt
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()