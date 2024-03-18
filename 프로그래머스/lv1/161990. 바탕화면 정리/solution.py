"""
드래그 시작점: S (lux, luy)
드래그 끝점: E (rdx, rdy)
반환값: [lux, luy, rdx, rdy]
"""

"""
# 시도 1. (성공)
## 방법
  - lux = x에서 제일 작은 값
  - luy = y에서 제일 작은 값
  - rdx = x에서 제일 큰 값 + 1
  - rdy = y에서 제일 큰 값 + 1  
"""
def solution(wallpaper):
    xs = []
    ys = []
    for x_i, wallpaper_x in enumerate(wallpaper):
        for y_i, y in enumerate(wallpaper_x):
            if y == '.':
                continue
            xs.append(x_i)
            ys.append(y_i)
    return [min(xs), min(ys), max(xs) + 1, max(ys) + 1]
