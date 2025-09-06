# YourInitials-3410-HW2.2

## Lesson 2.2 – Pixel Manipulation

**What this does**
- Moves all pixel helpers into **`PixelFunctions.py`** (cleaner `main.py`).
- Implements an **iterative quicksort** in `SortFunctions.py` and uses a `key` that compares the **red** channel of each pixel tuple `((r,g,b),(x,y))`.
- Prompts the user for a **red threshold** (0–255), finds all pixels with `red >= threshold` using an iterative **lower_bound** search, and overlays them on a grayscale version of the image.
