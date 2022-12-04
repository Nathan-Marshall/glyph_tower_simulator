from datetime import datetime
from time import sleep
from PIL import ImageGrab

from GlyphTowerCanvas import GlyphTowerCanvas

output_log = ""

shared_variable_shift = 0
right_consonant_fixed_shift = 1
up_consonant_fixed_shift = 2
up_vowel_fixed_shift = 1
down_vowel_fixed_shift = 2


def process_direction(glyph_renderers, direction, parse_key=range(4)):
    """
    :type glyph_renderers: Iterator[GlyphRenderer]
    :type direction: object
    :type parse_key: collections.Sequence[type(direction)]
    """
    global output_log
    global shared_variable_shift

    if direction not in parse_key:
        return

    rng = range(len(glyph_renderers))

    consonant_shifts = []
    vowel_shifts = []
    inversion_shifts = []

    if direction == parse_key[0]:
        # left
        for i in rng:
            consonant_shifts.append(i + shared_variable_shift)
            vowel_shifts.append(i + shared_variable_shift)
            inversion_shifts.append(i)
    elif direction == parse_key[1]:
        # right
        for i in rng:
            consonant_shifts.append(i + right_consonant_fixed_shift)
            vowel_shifts.append(shared_variable_shift)
            inversion_shifts.append(shared_variable_shift)
    elif direction == parse_key[2]:
        # up
        for i in rng:
            consonant_shifts.append(i + up_consonant_fixed_shift)
            vowel_shifts.append(i + up_vowel_fixed_shift)
            inversion_shifts.append(shared_variable_shift)
    else:
        # down
        for i in rng:
            consonant_shifts.append(shared_variable_shift)
            vowel_shifts.append(i + down_vowel_fixed_shift)
            inversion_shifts.append(i)

    for renderer, c_shift, v_shift, i_shift in zip(glyph_renderers, consonant_shifts, vowel_shifts, inversion_shifts):
        renderer.consonant_index -= c_shift
        renderer.vowel_index -= v_shift
        renderer.inversion_index -= i_shift

    shared_variable_shift += 1

    for renderer in glyph_renderers:
        renderer.visible = True
        renderer.update()

    print(direction, end=" ")
    output_log += str(direction) + " "


def process_all(root, canvas, directions, parse_key="←→↑↓", screenshot_path=None):
    """
    :type root: Tk
    :type canvas: GlyphTowerCanvas
    :type directions: collections.Iterator
    :type parse_key: collections.Sequence
    :type screenshot_path: str
    """
    for direction in directions:
        process_direction(canvas.glyph_renderers, direction, parse_key)

    root.update()

    if screenshot_path is not None and screenshot_path != "":
        sleep(0.5)
        save_image(root, canvas, screenshot_path)


def save_image(root, canvas, path):
    if path is None:
        return

    x0 = root.winfo_rootx() + canvas.winfo_x()
    y0 = root.winfo_rooty() + canvas.winfo_y()
    x1 = x0 + canvas.winfo_width()
    y1 = y0 + canvas.winfo_height()

    ImageGrab.grab().crop((x0, y0, x1, y1)).save(path)


def save_log(path):
    if path is None:
        return

    global output_log

    with open(path, "a", encoding="utf-8") as f:
        f.writelines([str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), "\n", output_log, "\n\n"])
        output_log = ""
