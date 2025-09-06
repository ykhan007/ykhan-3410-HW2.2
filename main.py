# main.py
# Lesson 2.2 – Pixel Manipulation Part 1
# Uses PixelFunctions module, iterative quicksort on RED channel, and user threshold.
# Python 3 only

from PixelFunctions import open_image_jpeg, store_pixels, to_grayscale, pixels_to_points_on
from SortFunctions import quicksort_iterative
from SearchFunctions import lower_bound

def main():
    # 1) open jpeg (place a small image like 200x200 named 'input.jpg' next to this file)
    img = open_image_jpeg("input.jpg")

    # 2) capture pixels as ((r,g,b),(x,y))
    pixels = store_pixels(img)

    # 3) sort by RED channel using our iterative quicksort (replacing selection sort from 2.1)
    #    compare like we did with selection sort: key looks at the red value of the rgb tuple.
    quicksort_iterative(pixels, key=lambda p: p[0][0])

    # 4) prompt user for threshold (e.g., 200). If invalid, default politely.
    raw = input("Enter red threshold (0–255): ").strip()
    try:
        thr = int(raw)
        if not (0 <= thr <= 255):
            raise ValueError
    except Exception:
        print("Invalid threshold. Using 200.")
        thr = 200

    # 5) build the sorted list of REDS for searching, then lower_bound
    reds = [p[0][0] for p in pixels]  # in same order as 'pixels' (sorted)
    start = lower_bound(reds, thr)

    # choose every pixel with red >= threshold
    selected = pixels[start:] if start < len(pixels) else []

    # 6) grayscale base
    gray = to_grayscale(img)

    # 7) paint selected colored pixels onto grayscale base
    out = pixels_to_points_on(gray, selected)

    # show and save
    out.show()              # preview
    out.save("output.jpg")  # write result

if __name__ == "__main__":
    main()
