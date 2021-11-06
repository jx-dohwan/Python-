# 내장모듈
# : 파이썬 설치 시 자동으로 설치되는 모듈

import math
print(math.pi)
print(math.ceil(2.7))

from math import pi, ceil
print(pi)
print(ceil(2.7))

from math import pi, ceil as C
print(pi)
print(C(2.7))

# 외부모듈
# : 다른 사람이 만든 파이썬 파일을 pip로 설치해서 사용
# pyautogui

import pyautogui as pg

pg.moveTo(500,500, duration=2)
