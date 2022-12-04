# This file isn't used by the application, but I thought some people might be interested in seeing how I used these
# transformation functions to quickly test variants of the golden path.

arrows = "←→↑↓"

golden_path = (
    "↑←"       # 12
    "↓←↑←"     # 16
    "↓←↑→↑"    # 34
    "→↑←↑→"    # 46
    "↓→↑←↑"    # 28
    "←↑→↑←"    # 22
    "↓←↑→↑"    # 15
    "↑"        # 27
    "←↑→↓→"    # 48
    "↓→↑→↓"    # 11
    "←↓→"      # 21
    "↑"        # 4
    "→→↓"      # 2
    "→"        # 4
    "↑"        # 50
    "→↓→"      # 6
    "↑→→↓←↓"   # 52
    "←"        # 42
    "↓→"       # 50
    "↓"        # 42
    "→↓←←"     # 33
    "↓→↓"      # 31
    "←↓→↑→↓→"  # 40
    "↑→→↓"     # 18
    "↓←↑→↑←"   # 44
    "↓←↑←"     # 39
    "↑"        # 12
    "←↑→→↑←↑"  # 9
)


def transform_directions(directions, direction_set, tf):
    return map(direction_set.__getitem__, map(tf.index, map(direction_set.index, filter(direction_set.__contains__, directions))))


def flip_x(directions, direction_set):
    return transform_directions(directions, direction_set, (1, 0, 2, 3))


def flip_y(directions, direction_set):
    return transform_directions(directions, direction_set, (0, 1, 3, 2))


def flip_xy(directions, direction_set):
    return transform_directions(directions, direction_set, (1, 0, 3, 2))


# When reversing the path, we also need to flip each input, hence the flip_xy in here.
def reverse_path(directions, direction_set):
    return reversed(tuple(flip_xy(directions, direction_set)))


# Reverse the golden path and also mirror it horizontally
solution_directions = flip_x(reverse_path(golden_path, arrows), arrows)
