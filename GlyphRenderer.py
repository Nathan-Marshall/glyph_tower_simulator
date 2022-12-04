import math

sqrt3 = math.sqrt(3)


class GlyphRenderer:
    # consonant line coordinates, top-to-bottom, left-to-right
    consonant_line_coords = (
        (0, -1, -2 * sqrt3, -3),
        (0, -1, 2 * sqrt3, -3),
        (0, -4, 0, 1),
        (0, -1, 0, 4),
        (0, 1, -2 * sqrt3, 3),
        (0, 1, 2 * sqrt3, 3),
    )

    # vowel line coordinates, counter-clockwise
    vowel_line_coords = (
        (0, -5, 2 * sqrt3, -3),
        (0, -5, -2 * sqrt3, -3),
        (-2 * sqrt3, -3, -2 * sqrt3, 3),
        (0, 5, -2 * sqrt3, 3),
        (0, 5, 2 * sqrt3, 3),
    )

    # inversion accent coordinates
    inversion_accent_coords = (-1, 5, 1, 7)

    # label coordinates
    label_coords = (0, 9)

    line_options = {
        "width": 5,
        "capstyle": "round"
    }

    oval_options = {
        "width": line_options["width"]
    }

    label_options = {
    }

    def __init__(self, canvas, consonants, vowels, consonant_index=0, vowel_index=0, inversion_index=0,
                 x=0, y=0, scale=5, visible=True, label_visible=True):
        self.canvas = canvas

        self.consonant_labels = tuple(c[0] for c in consonants)
        self.consonant_definitions = tuple(c[1:] for c in consonants)

        self.vowel_labels = tuple(v[0] for v in vowels)
        self.vowel_definitions = tuple(v[1:] for v in vowels)

        self.consonant_index = consonant_index
        self.vowel_index = vowel_index
        self.inversion_index = inversion_index

        self.x = x
        self.y = y
        self.scale = scale

        self.consonant_lines = []
        for i in range(6):
            self.consonant_lines.append(canvas.create_line(x, y, x, y, **self.line_options))

        self.vowel_lines = []
        for i in range(5):
            self.vowel_lines.append(canvas.create_line(x, y, x, y, **self.line_options))

        self.inversion_accent = canvas.create_oval(x, y, x, y, **self.oval_options)

        self.label = canvas.create_text(x, y, **self.label_options)

        self.visible = visible
        self.label_visible = label_visible

        self.update()

    # tuple of booleans indicating which lines to show
    def get_consonant(self):
        self.consonant_index %= len(self.consonant_definitions)
        return self.consonant_definitions[self.consonant_index]

    # tuple of booleans indicating which lines to show
    def get_vowel(self):
        self.vowel_index %= len(self.vowel_definitions)
        return self.vowel_definitions[self.vowel_index]

    def is_inverted(self):
        self.inversion_index %= 8
        return self.inversion_index == 0

    def set_indices(self, consonant_index, vowel_index, inversion_index):
        self.consonant_index = consonant_index
        self.vowel_index = vowel_index
        self.inversion_index = inversion_index

    def local_to_global(self, x0, y0, x1=0, y1=0):
        x0, y0, x1, y1 = tuple(n * self.scale for n in (x0, y0, x1, y1))
        return self.x + x0, self.y + y0, self.x + x1, self.y + y1

    def update(self):
        # update consonant line coordinates and visibility
        for consonant_line, local_coords, has_line in zip(self.consonant_lines, self.consonant_line_coords, self.get_consonant()):
            self.canvas.coords(consonant_line, self.local_to_global(*local_coords))
            self.canvas.itemconfig(consonant_line, state="normal" if self.visible and has_line else "hidden")

        # update vowel line coordinates and visibility
        for vowel_line, local_coords, has_line in zip(self.vowel_lines, self.vowel_line_coords, self.get_vowel()):
            self.canvas.coords(vowel_line, self.local_to_global(*local_coords))
            self.canvas.itemconfig(vowel_line, state="normal" if self.visible and has_line else "hidden")

        # update inversion accent coordinates and visibility
        self.canvas.coords(self.inversion_accent, self.local_to_global(*self.inversion_accent_coords))
        self.canvas.itemconfig(self.inversion_accent, state="normal" if self.visible and self.is_inverted() else "hidden")

        # update label coordinates and text
        self.canvas.coords(self.label, self.local_to_global(*self.label_coords)[0:2])
        consonant_text = self.consonant_labels[self.consonant_index]
        vowel_text = self.vowel_labels[self.vowel_index]
        label_text = consonant_text + vowel_text if not self.is_inverted() else vowel_text + consonant_text
        self.canvas.itemconfig(self.label, text=label_text, state="normal" if self.visible and self.label_visible else "hidden")
