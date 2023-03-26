import random

# 1回のゲームをシミュレートする関数
def monty_hall(change_door):
    # 奨賞が隠されているドアをランダムに選択
    prize_door = random.randint(1, 3)
    # 最初に選ぶドアをランダムに選択
    first_choice = random.randint(1, 3)
    
    # 最初に選んだドアが奨賞を隠している場合
    if first_choice == prize_door:
        # 開けないドアを選択
        remaining_doors = [door for door in [1, 2, 3] if door != first_choice]
        open_door = random.choice(remaining_doors)
    else:
        # 最初に選んだドアが奨賞を隠していない場合、奨賞を隠していないドアを開ける
        open_door = [door for door in [1, 2, 3] if door != first_choice and door != prize_door][0]
    
    # ドアを変更するかどうか
    if change_door:
        # ドアを変更する場合、最初に選んだドアと開かれたドア以外のドアを選択
        final_choice = [door for door in [1, 2, 3] if door != first_choice and door != open_door][0]
    else:
        # ドアを変更しない場合、最初に選んだドアを選択
        final_choice = first_choice
    
    # 最終的な選択が奨賞を隠しているかどうか
    return final_choice == prize_door

# 勝率を算出する関数
def simulate(change_door, num_simulations):
    win = 0
    # 指定された回数分ゲームを繰り返す
    for i in range(num_simulations):
        win += monty_hall(change_door)
    # 勝率を計算して返す
    return win / num_simulations

# ドアを変更する場合と変更しない場合の勝率を比較する
print("Win rate when changing door:", simulate(True, 10000))
print("Win rate when not changing door:", simulate(False, 10000))
