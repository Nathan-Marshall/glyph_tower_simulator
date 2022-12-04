# CONSONANTS

# Each 1 indicates the presence of a line. Tuple is ordered as follows:
# (label, upper left branch, upper right branch, upper trunk, lower trunk, lower left branch, lower right branch)
# \ /
#  |
#  |
# / \
consonants = (
    ("",   0, 0, 0, 0, 0, 0),  # 0: blank

    ("m",  0, 0, 0, 0, 1, 1),  # 1: [m] m
    ("n",  1, 0, 0, 0, 1, 1),  # 2: [n] n
    ("ng", 1, 1, 1, 1, 1, 1),  # 3: [ŋ] ng
    ("p",  0, 1, 0, 1, 0, 0),  # 4: [p] p
    ("b",  0, 0, 1, 0, 0, 1),  # 5: [b] b
    ("t",  1, 1, 0, 1, 0, 0),  # 6: [t] t

    ("d",  0, 0, 1, 0, 1, 1),  # 7: [d] d
    ("k",  0, 1, 1, 0, 0, 1),  # 8: [k] k, hard c
    ("g",  0, 1, 0, 1, 0, 1),  # 9: [g] hard g
    ("j",  0, 0, 1, 0, 1, 0),  # 10: [dʒ] j, soft g
    ("ch", 1, 0, 0, 1, 0, 0),  # 11: [tʃ] ch (as in "choose")
    ("f",  0, 1, 0, 1, 1, 0),  # 12: [f] f

    ("v",  1, 0, 1, 0, 0, 1),  # 13: [v] v
    ("th", 1, 1, 1, 1, 0, 0),  # 14: [θ] th (unvoiced, as in "path")
    ("th", 0, 0, 1, 1, 1, 1),  # 15: [ð] th (voiced, as in "father")
    ("s",  0, 1, 1, 1, 1, 0),  # 16: [s] hard s, soft c
    ("z",  1, 0, 1, 1, 0, 1),  # 17: [z] z, soft s
    ("sh", 1, 1, 0, 1, 1, 1),  # 18: [ʃ] sh

    ("zh", 1, 1, 1, 0, 1, 1),  # 19: [ʒ] zh (fuzzy s, as in "television")
    ("h",  0, 0, 1, 1, 0, 1),  # 20: [h] h
    ("r",  0, 1, 1, 1, 0, 0),  # 21: [r] r
    ("y",  1, 0, 1, 1, 0, 0),  # 22: [j] y
    ("w",  1, 1, 0, 0, 0, 0),  # 23: [w] w
    ("l",  0, 0, 1, 1, 0, 0),  # 24: [l] l
)

# "ANCIENT" CONSONANT VARIANTS

# For some reason, the alphabet used in Glyph Tower has a couple consonant glyphs that differ from standard Trunic.
# I'm speculating, but these could be explained as ancient variants of those consonants, since writing systems evolve
# over time. These two "ancient" consonants replace the standard "p" and "th (unvoiced)" and appear in the same indices
# as the replaced consonants. I presume the "ancient" consonants mean the same thing as the standard consonants in their
# respective indices, so I use the standard labels in my program, but I can't confirm whether this is actually true,
# as those consonants don't appear in the Glyph Tower solution.
consonants_ancient = list(consonants)
consonants_ancient[4] = ("p", 0, 0, 0, 1, 1, 0)  # 4: this "short backwards h" symbol replaces the regular "p"
consonants_ancient[14] = ("th", 1, 1, 1, 0, 1, 0)  # 14: this "bent th" symbol replaces the regular "th (unvoiced)"

# VOWELS

# Each 1 indicates the presence of a line. Lines are ordered counter-clockwise, starting from the upper right:
# (label, upper right shell, upper left shell, center left shell, lower left shell, lower right shell)
#  / \
# |
#  \ /
vowels = (
    ("",    0, 0, 0, 0, 0),  # 0: blank

    ("a",   1, 1, 1, 0, 0),  # 1: [æ] short a (cat)
    ("o",   0, 1, 1, 0, 0),  # 2: [ɑː, ɒ] short o (dog, maul, saw, tall)
    ("i",   0, 0, 0, 1, 1),  # 3: [ɪ] short i (pig)
    ("e",   0, 0, 1, 1, 1),  # 4: [e] short e (elk)
    ("ou",  0, 0, 1, 1, 0),  # 5: [ʊ] short oo/u/ou (book, put, bull, would)
    ("u",   1, 1, 0, 0, 0),  # 6: [ʌ, ə] short u (duck, alive, mother)

    ("ee",  0, 1, 1, 1, 1),  # 7: [iː] long e/ee (eel, eat, discrete)
    ("oo",  1, 1, 1, 1, 0),  # 8: [uː] long u/oo (dude, fool, tomb, puma)
    ("er",  1, 0, 1, 1, 1),  # 9: [ɝː, ɜː, ər] er/ur (panther, turkey, shirt)
    ("or",  1, 1, 1, 0, 1),  # 10: [ɔːr, ɔː] or (boar, horn, door, gore)
    ("ar",  1, 1, 0, 1, 1),  # 11: [ɑːr, ɑː] ar (tart)
    ("eer", 0, 1, 1, 0, 1),  # 12: [ɪr, ɪə, ɪər] eer (deer, clear, revere)

    ("ay",  0, 1, 0, 0, 0),  # 13: [eɪ] long a (late, wait, stay, hey)
    ("ie",  1, 0, 0, 0, 0),  # 14: [aɪ] long i (bite, tie, sigh, fly, bye)
    ("oy",  0, 0, 0, 1, 0),  # 15: [ɔɪ] oi/oy (boy, foil)
    ("ow",  0, 0, 0, 0, 1),  # 16: [aʊ] ow/ou (cow, house)
    ("oh",  1, 1, 1, 1, 1),  # 17: [oʊ, əʊ] long o (hose, crow, doe, boat)
    ("air", 0, 0, 1, 0, 1),  # 18: [er, eə, eər] air/are (hair, wear, dare, terrible)
)
