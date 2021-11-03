#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PIL import Image
import pytesseract

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: " + sys.argv[0] + " <image-file>")
        sys.exit(0)
    elif len(sys.argv) >= 2:
        image_file = sys.argv[1]

    text = pytesseract.image_to_string(Image.open(image_file))
    print(text)