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


HEIGHT = 70
WIDTH = 70

l1 = Letter()
l2 = Letter()
l3 = Letter()
l4 = Letter()

def gen_rands():
    return np.random.randint(-5, 6)

letter_height = l1.current_letter.shape[0]
letter_width = l1.current_letter.shape[1]

# visualizerの初期化 (Appendix参照)
visualizer = MatrixVisualizer(width=WIDTH*5, height=HEIGHT*5)

state = np.zeros((HEIGHT,WIDTH), dtype=np.int8)
next_state = np.empty((HEIGHT,WIDTH), dtype=np.int8)

# 初期化
bit_map_label_and_img = game_of_life_patterns.bit_map_label_and_img

# l1_h_rand = gen_rands()
# l1_w_rand = gen_rands()
# l2_h_rand = gen_rands()
# l2_w_rand = gen_rands()
# l3_h_rand = gen_rands()
# l3_w_rand = gen_rands()
# l4_h_rand = gen_rands()
# l4_w_rand = gen_rands()

l1_h_rand = 0
l1_w_rand = 0
l2_h_rand = 0
l2_w_rand = 0
l3_h_rand = 0
l3_w_rand = 0
l4_h_rand = 0
l4_w_rand = 0

state[5 + l1_h_rand: 5 + l1_h_rand + letter_height, 5 + l1_w_rand: 5 + l1_w_rand + letter_width] = l1.next()
state[5 + l2_h_rand: 5 + l2_h_rand + letter_height, 35 + l2_w_rand: 35 + l2_w_rand + letter_width] = l2.next()
state[35 + l3_h_rand: 35 + l3_h_rand + letter_height, 5 + l3_w_rand: 5 + l3_w_rand + letter_width] = l3.next()
state[35 + l4_h_rand: 35 + l4_h_rand + letter_height, 35 + l4_w_rand: 35 + l4_w_rand + letter_width] = l4.next()

visualizer.update(1 - state) # 1を黒, 0を白で表示する
# visualizer.update(state)


time.sleep(5)

def varied_step_range(start,stop,stepiter):
    step = iter(stepiter)
    while start < stop:
        yield start
        start += next(step)



count = 0
while visualizer:  # visualizerはウィンドウが閉じられるとFalseを返す
    time.sleep(0.1)
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
    # l1_h_rand = gen_rands()
    # l1_w_rand = gen_rands()
    # l2_h_rand = gen_rands()
    # l2_w_rand = gen_rands()
    # l3_h_rand = gen_rands()
    # l3_w_rand = gen_rands()
    # l4_h_rand = gen_rands()
    # l4_w_rand = gen_rands()

    l1_h_rand = 0
    l1_w_rand = 0
    l2_h_rand = 0
    l2_w_rand = 0
    l3_h_rand = 0
    l3_w_rand = 0
    l4_h_rand = 0
    l4_w_rand = 0

    if np.random.randint(1,11) % 4 == 0:  # 70%の割合で文字を再注入
        next_state[5 + l1_h_rand: 5 + l1_h_rand + letter_height, 5 + l1_w_rand: 5 + l1_w_rand+ letter_width] \
            = next_state[5 + l1_h_rand: 5 + l1_h_rand + letter_height, 5 + l1_w_rand: 5 + l1_w_rand+ letter_width] + l1.next()

    if np.random.randint(1, 11) % 4 == 0:  # 70%の割合で文字を再注入
        next_state[5 + l2_h_rand: 5 + l2_h_rand + letter_height, 35 + l2_w_rand: 35 + l2_w_rand + letter_width] \
            += l2.next()

    if np.random.randint(1, 11) % 4 == 0:  # 70%の割合で文字を再注入
        next_state[35 + l3_h_rand: 35 + l3_h_rand + letter_height, 5 + l3_w_rand: 5 + l3_w_rand + letter_width] \
            += l3.next()

    if np.random.randint(1, 11) % 4 == 0:  # 70%の割合で文字を再注入
        next_state[35 + l4_h_rand: 35 + l4_h_rand + letter_height, 35 + l4_w_rand: 35 + l4_w_rand + letter_width] \
            += l4.next()


    state, next_state = next_state, state

    # 表示をアップデート
    visualizer.update(1 - state) # 1を黒, 0を白で表示する
    print(visualizer.render().shape)

    cv2.imshow('frame', visualizer.render())



# Release everything if job is finished

cv2.destroyAllWindows()