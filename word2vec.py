# モデルを読み込む
from gensim.models import Word2Vec

#単語を入力
a,b,c = input().split()

#学習済みモデルをロード
model = Word2Vec.load('word2vec/jawiki.model')

# 単語同士の類似度を計算する
similarity = model.wv.similarity(a, b)
print('類似度:', similarity)

# 単語同士の距離を計算する
distance = model.wv.distance(a, b)
print('距離:', distance)

# 類似した単語を検索する
similar_words = model.wv.most_similar(a)
print('類似した単語:', similar_words)

# 2つの単語の足し算、引き算を計算する
result1 = model.wv.most_similar(positive=[a, b], negative=[c])
print('単語1 + 単語2 - 単語3:', result1)

result2 = model.wv.most_similar(positive=[a, b])
print('単語1 + 単語2:', result2)