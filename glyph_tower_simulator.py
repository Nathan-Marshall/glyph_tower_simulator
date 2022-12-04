from functools import partial
import tkinter

from alphabet import consonants_ancient, vowels
from GlyphTowerCanvas import GlyphTowerCanvas
from input_processing import process_direction, process_all, save_image, save_log
from parser import args, input_file_directions, input_file_parse_key

# Init tk
root = tkinter.Tk()
root.title("Glyph Tower Simulator")
root.iconbitmap("glyph_icon.ico")

# Create canvas
canvas = GlyphTowerCanvas(root, bg="white", height=600, width=600, consonants=consonants_ancient, vowels=vowels,
                          start_visible=args.start_visible, hide_labels=args.hide_labels)

# Create Save Log button
save_log_button = tkinter.Button(root, text="Save Log", command=partial(save_log, args.output_log[0]))

# Create Save Image button
save_image_button = tkinter.Button(root, text="Save Image", command=partial(save_image, root, canvas, args.output_image[0]))

# Create Reset button
reset_button = tkinter.Button(root, text="Reset", command=canvas.reset)

# Add to window
canvas.grid(column=0, columnspan=3, row=0)
save_log_button.grid(column=0, row=1)
save_image_button.grid(column=1, row=1)
reset_button.grid(column=2, row=1)

# Bind key presses to key_down
root.bind("<KeyPress>", lambda e: process_direction(canvas.glyph_renderers, e.keysym[0], "LRUD"))

# Input solution parsed from file
if input_file_directions is not None:
    process_all(root, canvas, input_file_directions, input_file_parse_key)

# Main loop. Prevents the window from closing immediately, and allows it to respond to input.
root.mainloop()
