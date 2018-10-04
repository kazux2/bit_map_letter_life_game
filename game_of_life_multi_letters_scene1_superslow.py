#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
np.set_printoptions(threshold=np.nan)
from alifebook_lib.visualizers import MatrixVisualizer
import game_of_life_patterns

import time
import cv2

from letter import Letter


HEIGHT = 40
WIDTH = 70

# visualizerの初期化 (Appendix参照)
visualizer = MatrixVisualizer(width=WIDTH*10, height=HEIGHT*10)
print('resolution:', visualizer.render().shape)

# 録画の設定
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # SEE: https://gist.github.com/takuma7/44f9ecb028ff00e2132e
out = cv2.VideoWriter('outputs/2018summer_art_project/scene1_breathing_dot_num500.mp4',fourcc, 30, (700, 400))

state = np.zeros((HEIGHT,WIDTH), dtype=np.int8)
next_state = np.empty((HEIGHT,WIDTH), dtype=np.int8)


from breathing_dot import BreathingDot

dot_num = 500
coordinates = [[np.random.randint(0,71), np.random.randint(0,41)] for i in range(0,dot_num)]

dots = {}

for i in range(0,dot_num):
    b = BreathingDot()
    dots[str(i)] = [coordinates[i],b]

for key, value in dots.items():
    coor = value[0]
    b = value[1]
    state[coor[1]:coor[1]+1, coor[0]:coor[0]+1] = b.next()

visualizer.update(1 - state) # 1を黒, 0を白で表示する



time.sleep(1)
count = 0
while visualizer:  # visualizerはウィンドウが閉じられるとFalseを返す
    # time.sleep(0.5)
    count += 1
    print("count:", count)
    # if np.random.randint(1,11) % 4 == 0:  # 70%の割合で文字を再注入
    #     next_state[5:6, 5: 6] \
    #         += dot

    # _b = b.next()
    # print(_b)
    # state[5:6, 5: 6] = _b

    for key, value in dots.items():
        coor = value[0]
        b = value[1]
        state[coor[1]:coor[1] + 1, coor[0]:coor[0] + 1] = b.next()

    # state, next_state = next_state, state

    # 表示をアップデート
    visualizer.update(1 - state) # 1を黒, 0を白で表示する

    # 録画
    frame = visualizer.render()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    print(frame_rgb.shape)
    out.write(frame_rgb)

    if count > 100000:
        break



# Release everything if job is finished
out.release()
cv2.destroyAllWindows()