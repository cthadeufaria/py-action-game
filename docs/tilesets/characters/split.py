# Adapted from https://github.com/whiplashoo/split-image/blob/main/src/split_image/split.py
import os
from PIL import Image


def split_image(image_path, rows=10, cols=10):
    im = Image.open(image_path)
    im_width, im_height = im.size
    row_width = int(im_width / cols)
    row_height = int(im_height / rows)
    name, ext = os.path.splitext(image_path)
    name = os.path.basename(name)

    os.mkdir(name)
    os.mkdir(os.path.join(name, "male"))
    os.mkdir(os.path.join(name, "female"))

    actions = ["idle", "rest", "walk", "attack", "die"]

    n = 0
    for i in range(0, rows):
        for j in range(0, cols):
            box = (
                j * row_width,
                i * row_height,
                j * row_width + row_width,
                i * row_height + row_height,
            )
            outp = im.crop(box)
            outp_name = f"{actions[n // cols]}_{n % cols}{ext}"
            print("Exporting image tile: " + outp_name)
            if i < rows // 2:
                outp.save(os.path.join(name, "male", outp_name))
            else:
                outp.save(os.path.join(name, "female", outp_name))
            n += 1
            n = n % ((rows * cols) // 2)


if __name__ == "__main__":
    base = "."
    for file in os.listdir(base):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            split_image(os.path.join(base, file))
