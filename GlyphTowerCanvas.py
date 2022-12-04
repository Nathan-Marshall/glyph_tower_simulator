import math
import tkinter

from GlyphRenderer import GlyphRenderer

# (consonant_index, vowel_index, inversion_index)
default_glyph_indices = (
    (12, 2, 3),
    (0, 16, 3),
    (13, 15, 6),
    (14, 5, 7),
    (14, 7, 5),
    (8, 13, 6),
    (8, 8, 0),
    (3, 8, 1),
    (7, 2, 2),
    (12, 6, 2),
    (18, 18, 4),
    (8, 15, 5),
)


class GlyphTowerCanvas(tkinter.Canvas):
    def __init__(self, *args, **kwargs):
        consonants = kwargs.pop("consonants")
        vowels = kwargs.pop("vowels")
        initial_glyph_indices = kwargs.pop("initial_glyph_indices", default_glyph_indices)
        self.start_visible = kwargs.pop("start_visible", False)
        hide_labels = kwargs.pop("hide_labels", False)

        super().__init__(*args, **kwargs)

        num_glyphs = 12
        center_x = kwargs["width"] * 0.5
        center_y = kwargs["height"] * 0.5
        glyph_distance_from_center = center_x * 0.8
        burst_radius = glyph_distance_from_center * 0.75
        circle_radius = burst_radius * 0.125
        burst_line_thickness = 2

        # Create glyph renderers and lines extending outward from the center toward each glyph
        self.glyph_renderers = []
        for i in range(num_glyphs):
            angle = math.pi / 2 - 2 * math.pi / 12 * i

            glyph_x = center_x + glyph_distance_from_center * math.cos(angle)
            glyph_y = center_y + glyph_distance_from_center * math.sin(angle)

            renderer = GlyphRenderer(self, consonants, vowels, x=glyph_x, y=glyph_y)
            self.glyph_renderers.append(renderer)

            self.create_line(center_x, center_y,
                             center_x + math.cos(2*math.pi * i/num_glyphs) * burst_radius,
                             center_y + math.sin(2*math.pi * i/num_glyphs) * burst_radius, width=burst_line_thickness)

        # Create a small circle covering the center of the burst
        self.create_oval(center_x - circle_radius, center_y - circle_radius,
                         center_x + circle_radius, center_y + circle_radius, fill="grey", width=burst_line_thickness)

        # Initialize consonant, vowel, and inversion indices
        self.initial_indices = initial_glyph_indices
        self.init_indices(initial_glyph_indices)

        # Hide glyphs if start_visible is false
        self.set_glyphs_visible(self.start_visible)

        # Hide glyph labels if hide_labels is true
        self.set_labels_visible(not hide_labels)

        self.update_glyph_renderers()

    def init_indices(self, initial_indices):
        self.initial_indices = initial_indices
        for renderer, indices in zip(self.glyph_renderers, initial_indices):
            renderer.set_indices(*indices)

    def reset(self):
        self.init_indices(self.initial_indices)
        self.set_glyphs_visible(self.start_visible)
        self.update()

    def update_glyph_renderers(self):
        for renderer in self.glyph_renderers:
            renderer.update()

    def set_glyphs_visible(self, visible):
        for renderer in self.glyph_renderers:
            renderer.visible = visible

    def set_labels_visible(self, visible):
        for renderer in self.glyph_renderers:
            renderer.label_visible = visible

    def update(self):
        self.update_glyph_renderers()
        super().update()
