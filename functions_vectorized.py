import numpy as np
from PIL import Image


def prod_non_zero_diag(x: np.ndarray):
    a = x.diagonal()
    a = a[a != 0]
    return np.prod(a)


def are_multisets_equal(x, y):
    return np.array_equal(np.sort(x), np.sort(y))


def max_after_zero(x: np.ndarray):
    a = np.concatenate(([False], x[:-1] == 0))
    b = x[a]
    return b.max()


def convert_image(img: np.ndarray, coefs: np.ndarray):
    return img @ coefs


def run_length_encoding(x):
    k = np.concatenate(([True], x[1:] != x[:-1]))
    a = x[k]
    k2 = np.where(k)[0]
    b = np.diff(np.append(k2, x.size))
    return a, b


def pairwise_distance(x: np.ndarray, y: np.ndarray):
    x2 = (x * x).sum(axis=1, keepdims=True)
    y2 = (y * y).sum(axis=1, keepdims=True).T
    xy = np.dot(x, y.T)
    ans = (x2 + y2 - 2 * xy) ** 0.5
    return ans


img = Image.open('Снимок экрана 2025-11-06 134940.png').convert("RGB")
res = convert_image(np.array(img), np.array([0.299, 0.587, 0.114]))
a = res.clip(0, 255).astype(np.uint8)
Image.fromarray(a).save('a.jpg')