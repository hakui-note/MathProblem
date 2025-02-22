import random

# ピョンの針問題の近似解を求める関数
def pi_approximation(num_trials):
    # 円内にある点の数をカウントする変数
    count = 0
    # num_trials回の試行を行う
    for i in range(num_trials):
        # 0から1までの乱数を生成する
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        # 点 (x, y) が単位円内にあるか判定する
        if x**2 + y**2 <= 1:
            count += 1
    # 円周率（π）を近似する値を計算する
    return 4 * count / num_trials

print(pi_approximation(1000000))
