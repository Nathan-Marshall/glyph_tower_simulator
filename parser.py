import argparse

parser = argparse.ArgumentParser(
                    prog="Glyph Tower Simulator",
                    description="Simulates Tunic's Glyph Tower puzzle.\n"
                                "\n"
                                "If you have not solved the puzzle, use this tool to efficiently test input sequences "
                                "and save a record of your inputs and results.\n"
                                "\n"
                                "Use the arrow keys to manually enter inputs.\n"
                                "\n"
                                "Or use -i to specify an input file. The first "
                                "4 characters of the file are called the \"key\". The key should be immediately "
                                "followed by a semicolon (;). These 4 characters will be used to interpret the rest of "
                                "the file. They represent the directions LEFT, RIGHT, UP, DOWN in that order. Any "
                                "occurrences of those characters in the file appearing after the semicolon (;) will "
                                "be parsed as directional inputs. All other characters will be ignored, so feel free "
                                "to include spaces, newlines, commas, etc.\n"
                                "\n"
                                "Examples of good keys: \"LRUD\", \"EWNS\", \"wasd\", \"←→↑↓\"",
                    epilog="")

parser.add_argument("-i", dest="input_file", type=str, nargs=1, metavar="INPUT_FILE",
                    help="Input file containing directional instructions")

parser.add_argument("-o", dest="output_image", type=str, nargs=1, default=["glyph_tower_output.jpg"], metavar="OUTPUT_IMAGE",
                    help="Output file to save an image of the result window")

parser.add_argument("-l", dest="output_log", type=str, nargs=1, default=["glyph_tower_output.log"], metavar="OUTPUT_LOG",
                    help="Output file to save a log of all valid inputs since the program started or the last time the "
                         "log was written to. Does not display errors or other program output.")

parser.add_argument("--start-visible", dest="start_visible", action="store_true",
                    help="Show glyphs in their initial state if no input is entered")

parser.add_argument("--hide-labels", dest="hide_labels", action="store_true",
                    help="Hide the labels that interpret each glyph")

args = parser.parse_args()

if args.input_file is not None:
    with open(args.input_file[0], encoding="utf-8") as f:
        input_file_text = "".join(f.readlines())
        input_file_parse_key = input_file_text[0:4]
        assert input_file_text[4] == ";", "INPUT_FILE is missing semicolon (;). " \
                                          "This should be the fifth character in the file, " \
                                          "immediately succeeding the parse key."
        input_file_directions = filter(input_file_parse_key.__contains__, input_file_text[5:])
else:
    input_file_text = None
    input_file_parse_key = None
    input_file_directions = None

if input_file_directions is not None:
    assert input_file_parse_key is not None and len(input_file_parse_key) == 4,\
        "INPUT_FILE parse key is invalid: \"" + input_file_parse_key + "\""
