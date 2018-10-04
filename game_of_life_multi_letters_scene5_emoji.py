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
from emoji import Emoji

HEIGHT = 480
WIDTH = 840

l_ratio = 0
e_ratio = 10
w_ratio = 10 - l_ratio - e_ratio

# 録画の設定
file_name = "scene5_emoji_l{}e{}w{}".format(l_ratio, e_ratio, w_ratio)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # SEE: https://gist.github.com/takuma7/44f9ecb028ff00e2132e
out = cv2.VideoWriter('outputs/2018summer_art_project/{}.mp4'.format(file_name),fourcc, 30, (WIDTH, HEIGHT))

# 初期化
bit_map_label_and_img = game_of_life_patterns.NUM_ALPH_KANA_KANJI

l1 = Letter(bit_map_label_and_img)
l2 = Letter(bit_map_label_and_img)

e1 = Emoji()
e2 = Emoji()

letter_height = l1.current_letter.shape[0]*12
letter_width = l1.current_letter.shape[1]*12

emoji_height = 360

state = np.ones((HEIGHT,WIDTH,3), dtype=np.int8) * 255
next_state = np.ones((HEIGHT,WIDTH,3), dtype=np.int8) *255

# visualizer.update(1 - state) # 1を黒, 0を白で表示する
# visualizer.update(state)

time.sleep(1)

count = 0

while (count <= 1000):
    # time.sleep(0.1)
    print(count)
    count += 1

    # 左
    left_dice = np.random.randint(1,11)
    if left_dice <= l_ratio:  # 20%の割合で文字を再注入
        state[60: 60 + emoji_height, 60: 60 + emoji_height] \
            = np.ones((emoji_height, emoji_height, 3), dtype=np.int8) * 255  # 前のe1(>l1)が残ってるかもなんで一回255で上書き
        l1_next = l1.next()
        grayscale_l1_next = (1 - l1_next) * 255 # 反転
        rgb_l1_next = cv2.cvtColor(np.uint8(grayscale_l1_next), cv2.COLOR_GRAY2BGR)
        state[72: 72 + letter_height, 72: 72 + letter_width] \
            = cv2.resize(np.uint8(rgb_l1_next), (336, 336), interpolation=cv2.INTER_NEAREST)

    elif left_dice <= l_ratio + e_ratio:
        state[60: 60 + emoji_height, 60: 60 + emoji_height] \
            = cv2.resize(e1.next(), (emoji_height, emoji_height), interpolation=cv2.INTER_NEAREST)

    else:
        state[60: 60 + emoji_height, 60: 60 + emoji_height] \
            = np.ones((emoji_height, emoji_height, 3), dtype=np.int8) *255

    # 右
    rigt_dice = np.random.randint(1, 11)

    if rigt_dice <= l_ratio:  # 20%の割合で文字を再注入
        state[60: 60 + emoji_height, 420: 420 + emoji_height] \
            = np.ones((emoji_height, emoji_height, 3), dtype=np.int8) * 255
        l1_next = l1.next()
        grayscale_l1_next = (1 - l1_next) * 255 # 反転
        rgb_l1_next = cv2.cvtColor(np.uint8(grayscale_l1_next), cv2.COLOR_GRAY2BGR)
        state[72: 72 + letter_height, 432: 432 + letter_width] \
            = cv2.resize(np.uint8(rgb_l1_next), (336, 336), interpolation=cv2.INTER_NEAREST)

    elif rigt_dice <= l_ratio + e_ratio:
        state[60: 60 + emoji_height, 420: 420 + emoji_height] \
            = cv2.resize(e2.next(), (emoji_height, emoji_height), interpolation=cv2.INTER_NEAREST)

    else:
        state[60: 60 + emoji_height, 420: 420 + emoji_height] \
            = np.ones((emoji_height, emoji_height, 3), dtype=np.int8) *255



    # 録画
    out.write(np.uint8(state))

    # opencvnize
    # cv2.imshow("penice", state)
    # cv2.waitKey(0)




# Release everything if job is finished
out.release()
cv2.destroyAllWindows()