import numpy as np

#生成一個整數2維陣列大小為10x10，名稱為map
map = np.zeros((10, 10), dtype=int)

#生成一個整數1維陣列大小為10，名稱為rowMap
rowMap = np.zeros(10, dtype=int)

#設定rowMap的值
rowMap = np.array([0, 7, 13, 28, 44, 62, 74, 75, 87, 90])

#在map中對應rowMap裡面的值標記炸彈
for index in rowMap:
    row, col = divmod(index, 10)  # 將一維索引轉為二維索引
    map[row, col] = -1  # 使用-1來表示炸彈

#統計炸彈周圍的數量
def count_bombs(map):
    rows, cols = map.shape
    bomb_map = np.zeros((rows, cols), dtype=int)
    
    for r in range(rows):
        for c in range(cols):
            if map[r, c] == -1:  # 如果是炸彈
                bomb_map[r, c] = -1  # 標記為炸彈
            else:
                # 統計周圍炸彈的數量
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= r + i < rows and 0 <= c + j < cols:
                            if map[r + i, c + j] == -1:
                                bomb_map[r, c] += 1
    return bomb_map

bomb_map = count_bombs(map)

# 輸出結果
for r in range(10):
    for c in range(10):
        if bomb_map[r, c] == -1:
            print('*', end=' ')
        elif bomb_map[r, c] == 0:
            print(' ', end=' ')
        else:
            print(bomb_map[r, c], end=' ')
    print()
