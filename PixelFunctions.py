"""
PixelFunctions.py
Lesson 2.2 – Pixel helpers moved out of main.
Python 3 only.
"""

from typing import List, Tuple

try:
    from PIL import Image  # pip install pillow
except ImportError as e:
    raise ImportError(

    ) from e

# Public API (helps avoid accidental name collisions on import *)
__all__ = [
    "open_image_jpeg",
    "store_pixels",
    "to_grayscale",
    "pixels_to_points_on",
]

# Type aliases
RGB = Tuple[int, int, int]
# Each pixel entry is ((r, g, b), (x, y))
Pix = Tuple[RGB, Tuple[int, int]]


def open_image_jpeg(path: str) -> Image.Image:
    
    img = Image.open(path).convert("RGB")
    return img


def store_pixels(img: Image.Image) -> List[Pix]:
    
    w, h = img.size
    src = img.load()
    out: List[Pix] = []
    for y in range(h):
        for x in range(w):
            r, g, b = src[x, y]
            out.append(((int(r), int(g), int(b)), (x, y)))
    return out


def to_grayscale(img: Image.Image) -> Image.Image:
    
    w, h = img.size
    src = img.load()
    gray = Image.new("RGB", (w, h))
    dst = gray.load()

    for y in range(h):
        for x in range(w):
            r, g, b = src[x, y]
            m = (int(r) + int(g) + int(b)) // 3
            dst[x, y] = (m, m, m)
    return gray


def pixels_to_points_on(base_img: Image.Image, pixels: List[Pix]) -> Image.Image:
    """
    Paint only the provided pixels (original colors) onto a copy of base_img.
    Useful for overlaying selected pixels on a grayscale base.
    """
    out = base_img.copy()
    put = out.load()
    for (r, g, b), (x, y) in pixels:
        put[x, y] = (int(r), int(g), int(b))
    return out
