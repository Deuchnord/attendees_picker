#!/usr/bin/env python3

from doctest import testmod, NORMALIZE_WHITESPACE

import attendees_picker

if __name__ == "__main__":
    (f, t) = testmod(attendees_picker, optionflags=NORMALIZE_WHITESPACE)

    if f == 0:
        print("All %d tests successfully passed." % t)
    else:
        exit(1)
