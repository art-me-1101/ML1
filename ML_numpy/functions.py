from PIL import Image
import numpy as np


def prod_non_zero_diag(x: list):
    n, m = len(x), len(x[0])
    ans = 1
    for i in range(min(n, m)):
        if x[i][i]:
            ans *= x[i][i]
            f = True
    return ans

def are_multisets_equal(x, y):
    return sorted(x) == sorted(y)


def max_after_zero(x):
    ans = min(x)
    for i in range(len(x) - 1):
        if x[i] == 0:
            ans = max(ans, x[i + 1])
    return ans


def convert_image(img, coefs):
    h, w, c = len(img), len(img[0]), len(coefs)
    ans = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            for k in range(c):
                ans[i][j] += img[i][j][k] * coefs[k]
    return ans

def run_length_encoding(x):
    a, b = [x[0]], [1]
    for i in range(1, len(x)):
        if x[i] != a[-1]:
            a.append(x[i])
            b.append(0)
        b[-1] += 1
    return a, b


def pairwise_distance(x, y):
    n, m = len(x), len(y)
    ans = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for a, b in zip(x[i], y[j]):
                ans[i][j] += (a - b) ** 2
            ans[i][j] **= 0.5

    return ans


img = Image.open('Снимок экрана 2025-11-06 134940.png').convert("RGB")

arr = np.array(
    convert_image(np.array(img).tolist(), [0.299, 0.587, 0.114]),
    dtype=np.uint8
)
res = Image.fromarray(arr, mode="L")
res.save('a.jpg')