#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
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
file_name = "scene3_variation_grows_1_toKanji"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # SEE: https://gist.github.com/takuma7/44f9ecb028ff00e2132e
out = cv2.VideoWriter('outputs/2018summer_art_project/{}.mp4'.format(file_name),fourcc, 30, (700, 400))


# 初期化
# bit_map_label_and_img = game_of_life_patterns.NUM_ALPH
# bit_map_label_and_img = game_of_life_patterns.NUM_ALPH_KANA
bit_map_label_and_img = game_of_life_patterns.NUM_ALPH_KANA_KANJI

l1 = Letter(bit_map_label_and_img)
l2 = Letter(bit_map_label_and_img)

letter_height = l1.current_letter.shape[0]
letter_width = l1.current_letter.shape[1]

state = np.zeros((HEIGHT,WIDTH), dtype=np.int8)
next_state = np.empty((HEIGHT,WIDTH), dtype=np.int8)

state[5: 5 + letter_height, 5: 5 + letter_width] = l1.next()
state[5: 5 + letter_height, 35 : 35 + letter_width] = l2.next()

visualizer.update(1 - state) # 1を黒, 0を白で表示する
# visualizer.update(state)


time.sleep(1)

count = 0
while visualizer:  # visualizerはウィンドウが閉じられるとFalseを返す
    # time.sleep(0.1)
    print(count)

    for i in range(HEIGHT):
        for j in range(WIDTH):

            # 自分と近傍のセルの状態を取得
            # c: center (自分自身)
            # nw: north west, ne: north east, c: center ...
            nw = state[i-1,j-1]
            n  = state[i-1,j]
            ne = state[i-1,(j+1)%WIDTH]
            w  = state[i,j-1]
            c  = state[i,j]
            e  = state[i,(j+1)%WIDTH]
            sw = state[(i+1)%HEIGHT,j-1]
            s  = state[(i+1)%HEIGHT,j]
            se = state[(i+1)%HEIGHT,(j+1)%WIDTH]
            neighbor_cell_sum = nw + n + ne + w + e + sw + s + se
            if c == 0 and neighbor_cell_sum == 3:
                next_state[i,j] = 1
            elif c == 1 and neighbor_cell_sum in (2,3):
                next_state[i,j] = 1
            else:
                next_state[i,j] = 0



    count += 1

    l1_h_rand = 0
    l1_w_rand = 0
    l2_h_rand = 0
    l2_w_rand = 0

    # if np.random.randint(1,11) % 4 == 0:  # 70%の割合で文字を再注入
    if 1:
        next_state[5 + l1_h_rand: 5 + l1_h_rand + letter_height, 5 + l1_w_rand: 5 + l1_w_rand+ letter_width] \
            = next_state[5 + l1_h_rand: 5 + l1_h_rand + letter_height, 5 + l1_w_rand: 5 + l1_w_rand+ letter_width] + l1.next()

    # if np.random.randint(1, 11) % 4 == 0:  # 70%の割合で文字を再注入
    if 1:
        next_state[5 + l2_h_rand: 5 + l2_h_rand + letter_height, 35 + l2_w_rand: 35 + l2_w_rand + letter_width] \
            += l2.next()


    state, next_state = next_state, state

    # 表示をアップデート
    visualizer.update(1 - state) # 1を黒, 0を白で表示する
    print(visualizer.render().shape)

    # 録画
    frame = visualizer.render()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    print(frame_rgb.shape)
    out.write(frame_rgb)

    if count > 1000:
        break


# Release everything if job is finished
out.release()
cv2.destroyAllWindows()