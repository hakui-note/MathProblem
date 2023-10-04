from gensim.models import word2vec
import bz2

with bz2.BZ2File('jawiki-latest-pages-articles.xml.bz2', 'r') as f:
    content = f.read()

with open('jawiki-latest-pages-articles.xml', 'wb') as f:
    f.write(content)

# Wikipedia日本語版のダンプデータから学習する
sentences = word2vec.LineSentence('jawiki-latest-pages-articles.xml')

# word2vecのモデルを学習する
model = word2vec.Word2Vec(sentences, vector_size=100, window=5, min_count=5, workers=4)

# 学習したモデルを保存する
model.save('jawiki.model')
